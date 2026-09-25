/**
 * TypeScript portu, uygulamanin Kotlin motorlariyla ayni sonucu veriyor mu?
 *
 * `src/data/vectors.json` gercek motorlarin ciktisi (uretici:
 * app/src/test/.../WebVectorExportTest.kt). Burada satir satir karsilastiriliyor.
 * Bir sapma varsa dagitim durur - sitede uygulamadan farkli bir rakam gostermek,
 * "uygulamanin hesabinin aynisi" vaadini yalan yapar.
 */
import { readFile } from 'node:fs/promises';
import {
  effectiveRate, monthlyPayment, schedule, totalPayableMinor, totalInterestMinor,
  statementDate, dueDate, periodEndingAt, periodOf, minimumPayment, splitInstallments,
} from '../src/lib/finance.ts';

const V = JSON.parse(await readFile('src/data/vectors.json', 'utf8'));
let checks = 0;
const fails = [];

const eq = (got, want, label) => {
  checks++;
  if (got !== want) fails.push(`${label}: beklenen ${want}, gelen ${got}`);
};
const near = (got, want, label) => {
  checks++;
  if (Math.abs(got - want) > 1e-12) fails.push(`${label}: beklenen ${want}, gelen ${got}`);
};

for (const [i, k] of V.kredi.entries()) {
  const tag = `kredi[${i}] ${k.anapara}@${k.aylikOran}x${k.vade}`;
  const rate = effectiveRate(k.aylikOran, k.bsmv, k.kkdf, k.vergiDahil);
  near(rate, k.efektifOran, `${tag} efektifOran`);
  eq(monthlyPayment(k.anapara, rate, k.vade), k.aylikTaksit, `${tag} aylikTaksit`);

  const rows = schedule(k.anapara, rate, k.vade);
  eq(rows.length, k.plan.length, `${tag} plan uzunlugu`);
  eq(totalPayableMinor(rows), k.toplamGeriOdeme, `${tag} toplamGeriOdeme`);
  eq(totalInterestMinor(rows), k.toplamFaiz, `${tag} toplamFaiz`);
  for (const [seq, odeme, faiz, anapara, kalan] of k.plan) {
    const r = rows[seq - 1];
    eq(r.paymentMinor, odeme, `${tag} satir ${seq} odeme`);
    eq(r.interestMinor, faiz, `${tag} satir ${seq} faiz`);
    eq(r.principalPartMinor, anapara, `${tag} satir ${seq} anapara`);
    eq(r.remainingMinor, kalan, `${tag} satir ${seq} kalan`);
  }
}

for (const [i, c] of V.ekstre.entries()) {
  const card = {
    statementDay: c.kesimGunu,
    dueMode: c.mod,
    dueDay: c.sonOdemeGunu,
    dueOffsetDays: c.gunFarki,
  };
  const tag = `ekstre[${i}] kesim ${c.kesimGunu} ${c.mod}`;
  for (const d of c.donemler) {
    const [y, m] = d.ay.split('-').map(Number);
    const cut = statementDate(card, y, m);
    eq(cut, d.kesim, `${tag} ${d.ay} kesim`);
    const p = periodEndingAt(card, cut);
    eq(p.dueDate, d.sonOdeme, `${tag} ${d.ay} sonOdeme`);
    eq(p.periodStart, d.baslangic, `${tag} ${d.ay} baslangic`);
  }
  for (const h of c.harcamalar) {
    const p = periodOf(card, h.tarih);
    eq(p.statementDate, h.kesim, `${tag} harcama ${h.tarih} kesim`);
    eq(p.dueDate, h.sonOdeme, `${tag} harcama ${h.tarih} sonOdeme`);
  }
}

for (const [i, a] of V.asgari.entries()) {
  eq(minimumPayment(a.bakiye, a.oran), a.asgari, `asgari[${i}] ${a.bakiye}@${a.oran}`);
}

for (const [i, t] of (V.taksit ?? []).entries()) {
  const got = splitInstallments(t.toplam, t.adet);
  const tag = `taksit[${i}] ${t.toplam}/${t.adet}`;
  eq(got.length, t.taksitler.length, `${tag} adet`);
  eq(got.reduce((a, b) => a + b, 0), t.toplam, `${tag} toplam tutmuyor`);
  t.taksitler.forEach((want, j) => eq(got[j], want, `${tag} taksit ${j + 1}`));
}

if (fails.length) {
  console.error(`Port ayrismis. ${fails.length} / ${checks} kontrol basarisiz:`);
  for (const f of fails.slice(0, 25)) console.error('  ' + f);
  process.exit(1);
}
console.log(`Port dogrulandi: ${checks} kontrolun hepsi Kotlin motoruyla ayni.`);
