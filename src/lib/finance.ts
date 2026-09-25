/**
 * Money Agenda hesaplama motorlarının TypeScript portu.
 *
 * Kaynak: uygulama deposundaki `domain/engine/LoanEngine.kt` ve `StatementEngine.kt`.
 * Buradaki her fonksiyon oradakinin birebir karşılığı olmak zorunda — site "uygulamanın
 * hesabı" diye bir sonuç gösteriyorsa, gerçekten o hesap olmalı.
 *
 * Doğrulama tahmine bırakılmadı: `src/data/vectors.json` gerçek Kotlin motorlarının
 * ürettiği çıktı, `tests/vectors.test.mjs` bu portun her satırını yeniden ürettiğini
 * kontrol ediyor ve dağıtım hattında koşuyor. Ayrışma olursa yayın durur.
 *
 * ## Yuvarlama
 *
 * Kotlin'de `Double.roundToLong()` = `Math.round(double)` = `floor(x + 0.5)`.
 * JavaScript'te `Math.round` de aynı şeyi yapıyor. Tutarlar pozitif olduğu için ikisi
 * birebir örtüşüyor — negatif değerlerde ayrışırlardı ama burada negatif tutar yok.
 *
 * ## Tam sayı bölme
 *
 * Kotlin'de `Long / Long` sıfıra doğru kırpar. JavaScript'te `/` ondalık verir, bu yüzden
 * faizsiz kredide `Math.trunc` gerekiyor. Unutulsaydı faizsiz kredinin taksiti kuruşlu
 * çıkardı ve vektör testi bunu yakalardı.
 *
 * ## Para birimi
 *
 * Bütün tutarlar **kuruş** (minor unit) cinsinden tam sayı. Uygulamadaki kural aynı
 * (CLAUDE.md §3): `Double` ile para tutulmaz.
 */

export interface ScheduleRow {
  seq: number;
  paymentMinor: number;
  interestMinor: number;
  principalPartMinor: number;
  remainingMinor: number;
}

/** Vergili aylık oran: `r × (1 + BSMV + KKDF)`. Konut kredisinde vergi yok. */
export function effectiveRate(
  monthlyRate: number,
  bsmv: number,
  kkdf: number,
  includeTaxes: boolean,
): number {
  return includeTaxes ? monthlyRate * (1 + bsmv + kkdf) : monthlyRate;
}

/**
 * Aylık eşit taksit (anüite): `P × i × (1+i)^n / ((1+i)^n − 1)`.
 * Faizsiz kredide anapara eşit bölünür.
 */
export function monthlyPayment(
  principalMinor: number,
  monthlyRate: number,
  termMonths: number,
): number {
  if (termMonths <= 0) throw new Error(`Vade pozitif olmalı: ${termMonths}`);
  if (monthlyRate <= 0) return Math.trunc(principalMinor / termMonths);

  const factor = (1 + monthlyRate) ** termMonths;
  return Math.round((principalMinor * monthlyRate * factor) / (factor - 1));
}

/**
 * Amortisman tablosu.
 *
 * Son satır özel: kalan anaparanın tamamı kapatılır. Aksi hâlde yuvarlama artıkları
 * birikip tablonun sonunda birkaç kuruşluk hayalet borç bırakır.
 */
export function schedule(
  principalMinor: number,
  monthlyRate: number,
  termMonths: number,
): ScheduleRow[] {
  const payment = monthlyPayment(principalMinor, monthlyRate, termMonths);
  let remaining = principalMinor;
  const rows: ScheduleRow[] = [];

  for (let seq = 1; seq <= termMonths; seq++) {
    const interest = Math.round(remaining * monthlyRate);
    const isLast = seq === termMonths;
    const principalPart = isLast ? remaining : payment - interest;
    const actualPayment = isLast ? remaining + interest : payment;

    remaining -= principalPart;

    rows.push({
      seq,
      paymentMinor: actualPayment,
      interestMinor: interest,
      principalPartMinor: principalPart,
      remainingMinor: Math.max(remaining, 0),
    });
  }
  return rows;
}

export function totalPayableMinor(rows: ScheduleRow[], feesMinor = 0): number {
  return rows.reduce((a, r) => a + r.paymentMinor, 0) + feesMinor;
}

export function totalInterestMinor(rows: ScheduleRow[]): number {
  return rows.reduce((a, r) => a + r.interestMinor, 0);
}

/* ------------------------------------------------------------------ *
 * Ekstre motoru
 * ------------------------------------------------------------------ */

export type DueMode = 'OFFSET_DAYS' | 'FIXED_DAY';

export interface CardRules {
  statementDay: number;
  dueMode: DueMode;
  dueDay?: number | null;
  dueOffsetDays?: number | null;
  minPaymentRate?: number;
}

/** Son ödeme ile kesim arasında en az kaç gün olmalı; altındaysa kullanıcı uyarılır. */
export const MIN_DUE_GAP_DAYS = 10;

const DEFAULT_DUE_OFFSET = 10;
const DEFAULT_DUE_DAY = 10;

/** `YYYY-MM-DD`. Tarihler UTC üzerinden tutuluyor; yerel saat dilimi kaydırma yapmasın. */
export type ISODate = string;

function daysInMonth(year: number, month: number): number {
  return new Date(Date.UTC(year, month, 0)).getUTCDate();
}

function iso(year: number, month: number, day: number): ISODate {
  const mm = String(month).padStart(2, '0');
  const dd = String(day).padStart(2, '0');
  return `${year}-${mm}-${dd}`;
}

function parse(date: ISODate): { year: number; month: number; day: number } {
  const [y, m, d] = date.split('-').map(Number);
  return { year: y, month: m, day: d };
}

export function addDays(date: ISODate, days: number): ISODate {
  const { year, month, day } = parse(date);
  const t = new Date(Date.UTC(year, month - 1, day + days));
  return iso(t.getUTCFullYear(), t.getUTCMonth() + 1, t.getUTCDate());
}

export function daysBetween(from: ISODate, to: ISODate): number {
  const a = parse(from);
  const b = parse(to);
  const ms = Date.UTC(b.year, b.month - 1, b.day) - Date.UTC(a.year, a.month - 1, a.day);
  return Math.round(ms / 86_400_000);
}

function addMonths(year: number, month: number, delta: number): { year: number; month: number } {
  const total = year * 12 + (month - 1) + delta;
  return { year: Math.floor(total / 12), month: (total % 12) + 1 };
}

/**
 * Ayın [day] günü — o ayda yoksa ayın son günü.
 *
 * `statementDay = 31` "ay sonu" demek: şubatta 28/29'a çekilir ama çapa 31 kalır, bir
 * sonraki ay yine 31'inde keser. Elle takip edenlerin en sık kaçırdığı ayrıntı bu.
 */
export function clampToMonthEnd(year: number, month: number, day: number): ISODate {
  if (day < 1 || day > 31) throw new Error(`Ayın günü 1..31 aralığında olmalı: ${day}`);
  return iso(year, month, Math.min(day, daysInMonth(year, month)));
}

/** [year]-[month] ayının kesim tarihi. */
export function statementDate(card: CardRules, year: number, month: number): ISODate {
  return clampToMonthEnd(year, month, card.statementDay);
}

/**
 * Kesim tarihine karşılık gelen son ödeme tarihi.
 *
 * `FIXED_DAY`: son ödeme günü kesim gününden **büyükse** aynı ay, değilse sonraki ay.
 * `OFFSET_DAYS`: kesimden N gün sonra — ay sınırını kendiliğinden aşar.
 */
export function dueDate(card: CardRules, statement: ISODate): ISODate {
  if (card.dueMode === 'OFFSET_DAYS') {
    return addDays(statement, card.dueOffsetDays ?? DEFAULT_DUE_OFFSET);
  }
  const dueDay = card.dueDay ?? DEFAULT_DUE_DAY;
  const s = parse(statement);
  const target = dueDay > card.statementDay ? { year: s.year, month: s.month } : addMonths(s.year, s.month, 1);
  return clampToMonthEnd(target.year, target.month, dueDay);
}

export interface Period {
  periodStart: ISODate;
  statementDate: ISODate;
  dueDate: ISODate;
}

/** Kesim tarihi verilen dönemi kurar. Aralık `(önceki kesim, bu kesim]`. */
export function periodEndingAt(card: CardRules, statement: ISODate): Period {
  const s = parse(statement);
  const prev = addMonths(s.year, s.month, -1);
  const previousCut = statementDate(card, prev.year, prev.month);
  return {
    periodStart: addDays(previousCut, 1),
    statementDate: statement,
    dueDate: dueDate(card, statement),
  };
}

/**
 * Bir harcamanın düştüğü dönem.
 *
 * Kesim gününde yapılan harcama **o döneme** dahildir; ertesi gün yapılan bir sonrakine.
 */
export function periodOf(card: CardRules, txnDate: ISODate): Period {
  const t = parse(txnDate);
  const thisMonthCut = statementDate(card, t.year, t.month);
  let closing = thisMonthCut;
  if (txnDate > thisMonthCut) {
    const next = addMonths(t.year, t.month, 1);
    closing = statementDate(card, next.year, next.month);
  }
  return periodEndingAt(card, closing);
}

/** Asgari ödeme tutarı. Kuruş yuvarlaması yukarı değil, en yakına yapılır. */
export function minimumPayment(statementBalanceMinor: number, minPaymentRate: number): number {
  if (statementBalanceMinor <= 0) return 0;
  return Math.min(Math.round(statementBalanceMinor * minPaymentRate), statementBalanceMinor);
}

/**
 * Kesim ile son ödeme arasında en az [MIN_DUE_GAP_DAYS] gün var mı?
 *
 * Yoksa kart ayarı büyük ihtimalle yanlış girilmiştir. Düzeltmiyoruz, **soruyoruz** —
 * bazı bankalarda gerçekten kısa olabiliyor.
 */
export function isDueTooClose(card: CardRules): boolean {
  const cut = statementDate(card, 2026, 1);
  return daysBetween(cut, dueDate(card, cut)) < MIN_DUE_GAP_DAYS;
}

/* ------------------------------------------------------------------ *
 * Biçimlendirme
 * ------------------------------------------------------------------ */

const TRY = new Intl.NumberFormat('tr-TR', {
  style: 'currency',
  currency: 'TRY',
  minimumFractionDigits: 2,
});

/** Kuruşu okunur tutara çevirir. */
export function money(minor: number): string {
  return TRY.format(minor / 100);
}

const DATE_TR = new Intl.DateTimeFormat('tr-TR', {
  day: 'numeric',
  month: 'long',
  year: 'numeric',
  timeZone: 'UTC',
});

export function formatDate(date: ISODate): string {
  const { year, month, day } = parse(date);
  return DATE_TR.format(new Date(Date.UTC(year, month - 1, day)));
}

/* ------------------------------------------------------------------ *
 * Taksit motoru
 * ------------------------------------------------------------------ */

/**
 * Toplam tutarı [count] taksite böler.
 *
 * Tek kritik kuralı: **taksitlerin toplamı toplam borca kuruşu kuruşuna eşit olmalı.**
 * 100 TL'yi 3'e bölünce 33,33 × 3 = 99,99 eder; kaybolan kuruş kullanıcının "kalan borç"
 * rakamını sonsuza kadar yanlış gösterir. Artık **ilk taksite** eklenir — bankaların
 * yaygın davranışı da bu ve fark en başta ödenir, sonda sürpriz olmaz.
 *
 * `splitInstallments(10000, 3)` → `[3334, 3333, 3333]`
 */
export function splitInstallments(totalMinor: number, count: number): number[] {
  if (count <= 0) throw new Error(`Taksit sayısı pozitif olmalı: ${count}`);
  if (totalMinor < 0) throw new Error(`Taksit tutarı negatif olamaz: ${totalMinor}`);

  const base = Math.trunc(totalMinor / count);
  const remainder = totalMinor % count;
  return Array.from({ length: count }, (_, i) => (i === 0 ? base + remainder : base));
}
