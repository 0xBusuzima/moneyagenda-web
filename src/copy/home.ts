import type { QA } from '../components/Faq.astro';

/**
 * Ana sayfa metinleri.
 *
 * **Her iddia koddan doğrulanabilir olmalı.** money-agenda deposundaki CLAUDE.md §4.6
 * kuralı sürüm notları için yazılmıştı ama burada daha da önemli: mağaza sayfası
 * kullanıcıyı bir kez yanıltır, site arama sonucunda aylarca durur. Sayı vermekten
 * kaçınılıyor ("14 bildirim kanalı" gibi bir cümle, sayı değiştiğinde yalan olur).
 */

export interface HomeCopy {
  meta: { title: string; description: string };
  hero: { eyebrow: string; h1: string; lead: string; trust: string[] };
  stance: { title: string; body: string; points: { t: string; d: string }[] };
  features: { title: string; lead: string; items: { t: string; d: string; href: string }[] };
  screens: { title: string; lead: string; shots: { file: string; alt: string }[] };
  local: { title: string; body: string; bullets: string[] };
  privacy: { title: string; body: string; bullets: string[] };
  faq: { title: string; items: QA[] };
  close: { title: string; body: string };
}

export const HOME: Record<'tr' | 'en', HomeCopy> = {
  tr: {
    meta: {
      title: 'Money Agenda — kart ekstresi, taksit, kredi ve abonelik takibi',
      description:
        'Kredi kartı kesim ve son ödeme tarihi, taksit, kredi, abonelik ve alan adı yenilemeleri tek takvimde. Vakti gelmeden hatırlatır. Ücretsiz, girişsiz çalışır, veriler telefonda kalır.',
    },
    hero: {
      eyebrow: 'Android · Türkiye için',
      h1: 'Kartın ne zaman kesiliyor, taksitin ne zaman düşüyor?',
      lead: 'Money Agenda geçmişi değil, sırada ne olduğunu gösterir. Kredi kartı kesim ve son ödeme, taksit, kredi, abonelik, alan adı — hepsi tek takvimde toplanır ve vakti gelmeden hatırlatılır.',
      trust: ['Tüm özellikler ücretsiz', 'Giriş gerekmeden çalışır', 'Veriler telefonunuzda kalır'],
    },
    stance: {
      title: 'Finans defteri değil, yükümlülük asistanı',
      body: 'Gelir gider uygulamalarının çoğu size ne harcadığınızı anlatır. Sorun genelde bu değil. Sorun, kartın kesim gününü kaçırıp bir sonraki ekstreye sarkmak, taksiti unutmak, alan adının sessizce düşmesi.',
      points: [
        {
          t: 'Ana ekran ileriye bakar',
          d: 'Bugün ve önümüzdeki günlerde ödenecek ne varsa üstte. Geçen ayın grafiği değil.',
        },
        {
          t: 'Takvim matematiği doğru',
          d: 'Kesim günü, son ödeme, ekstre dönemi, asgari ödeme — hepsi kartın kendi kurallarıyla hesaplanır.',
        },
        {
          t: 'Hatırlatma gerçekten gelir',
          d: 'Kesin alarm kullanılır; cihaz uyku moduna girse de yeniden başlatılsa da plan korunur.',
        },
      ],
    },
    features: {
      title: 'Neleri takip eder',
      lead: 'Hepsi aynı takvimde toplanır; ayrı ayrı uygulama açmanız gerekmez.',
      items: [
        {
          t: 'Kredi kartı',
          d: 'Kesim ve son ödeme tarihleri, ekstre dönemleri, asgari ödeme, kart borcu ve kalan limit.',
          href: '/ozellikler/kredi-karti-takibi/',
        },
        {
          t: 'Taksit ve kredi',
          d: 'Taksitli alışveriş planı, kredi amortismanı ve BSMV/KKDF dahil efektif maliyet.',
          href: '/ozellikler/taksit-ve-kredi/',
        },
        {
          t: 'Abonelik ve yenileme',
          d: 'Abonelik, alan adı, hosting, SSL, sigorta — yenilenen ne varsa tarihiyle birlikte.',
          href: '/ozellikler/abonelik-ve-yenileme/',
        },
        {
          t: 'Bütçe ve rapor',
          d: 'Kategori bütçeleri, hedefler, aylık raporlar; CSV, XLSX ve PDF olarak dışa aktarma.',
          href: '/ozellikler/butce-ve-rapor/',
        },
        {
          t: 'Bildirimler',
          d: 'Vade öncesi ve sonrası uyarılar, sessiz saatler, günlük özet; her tür için ayrı kanal.',
          href: '/ozellikler/bildirimler/',
        },
        {
          t: 'Güvenlik',
          d: 'Şifreli yerel yedek, PIN ve parmak izi kilidi, tutarları gizleme.',
          href: '/ozellikler/butce-ve-rapor/',
        },
      ],
    },
    screens: {
      title: 'Uygulamadan',
      lead: 'Sıcak, sakin bir arayüz: tek vurgu rengi, sayılarda sabit genişlikli yazı tipi, gereksiz süsleme yok.',
      shots: [
        { file: '01-bugun', alt: 'Bugün ekranı: bu ay ödenecek tutar, kullanılabilir bakiye ve yaklaşan yükümlülükler' },
        { file: '05-kart-detay', alt: 'Kart detayı: güncel borç, asgari ödeme, kesim tarihi ve son ödemeye kalan gün' },
        { file: '08-taksitler', alt: 'Taksitler ekranı: bu ay ödenecek taksit tutarı ve kalan taksit planı' },
        { file: '02-raporlar', alt: 'Raporlar ekranı: gelir gider akışı, ay sonu tahmini ve son 12 ayın grafiği' },
      ],
    },
    local: {
      title: 'Türk bankacılık takvimini biliyor',
      body: 'Uygulamanın içindeki hesaplamalar Türkiye’ye özgü kurallara göre yazıldı ve birim testli. Genel bir bütçe uygulamasının yaklaşık cevap verdiği yerde burada kesin cevap var.',
      bullets: [
        'Kesim günü ile son ödeme arasındaki gün farkı karta göre ayarlanır',
        'Ayın 29–31’i gibi her ayda bulunmayan günler doğru kaydırılır',
        'Kredi maliyetinde BSMV ve KKDF hesaba katılır',
        'Döviz tutarları TCMB kuruyla gösterilir',
        'Tutarlar kuruş hassasiyetinde tutulur; ondalık yuvarlama hatası olmaz',
      ],
    },
    privacy: {
      title: 'Verileriniz telefonunuzda',
      body: 'Uygulama giriş yapmadan tam olarak çalışır; hiçbir özellik hesap açmanıza bağlı değil. Bulut yedeği isteğe bağlıdır ve siz açmadan çalışmaz.',
      bullets: [
        'Banka hesabınıza bağlanılmaz — açık bankacılık entegrasyonu yoktur',
        'SMS okuma izni istenmez',
        'Tutar, kart adı, kişi adı gibi finansal veriler reklam ağına ya da analitik servisine gönderilmez',
        'Yapay zekâ kullanılmaz; her hesaplama deterministik ve ekranda açıklanır',
      ],
    },
    faq: {
      title: 'Sık sorulanlar',
      items: [
        {
          q: 'Uygulama ücretsiz mi?',
          a: 'Evet. <strong>Tüm özellikler ücretsiz sürümde açık</strong>; hiçbir şey ödeme duvarının arkasında değil. Ücretsiz sürümde alt barın üstünde bir reklam şeridi var. Pro (aylık, 6 aylık, yıllık veya ömür boyu) yalnızca bu şeridi kaldırır.',
        },
        {
          q: 'Verilerim nereye gidiyor?',
          a: 'Telefonunuzda kalıyor. Uygulama giriş yapmadan tam çalışır. Bulut yedeğini siz açarsanız verileriniz Google hesabınıza bağlı olarak saklanır. Finansal verileriniz reklam ağına veya analitik servisine hiçbir koşulda gönderilmez.',
        },
        {
          q: 'İnternet olmadan çalışır mı?',
          a: 'Evet. Veritabanı telefonda; kayıt, hesaplama ve hatırlatmaların hepsi çevrimdışı çalışır. İnternet yalnızca isteğe bağlı bulut yedeği ve güncel döviz kuru için gerekir.',
        },
        {
          q: 'Banka hesabıma bağlanıyor mu?',
          a: 'Hayır, bilinçli olarak. Açık bankacılık entegrasyonu yok ve SMS okuma izni istenmiyor. Kayıtları siz giriyorsunuz; buna karşılık hiçbir banka kimlik bilgisi paylaşmıyorsunuz.',
        },
        {
          q: 'Hatırlatmalar gerçekten zamanında geliyor mu?',
          a: 'Kesin alarm kullanılıyor, yani cihaz uyku moduna girse bile hatırlatma zamanında çalışıyor. Telefon yeniden başlatıldığında plan otomatik yeniden kuruluyor. Bazı üreticilerin pil yöneticisi uygulamaları kısıtlayabildiği için, uygulamanın içinde cihaz markasına göre adım adım çözüm rehberi ve bir test bildirimi düğmesi var.',
        },
        {
          q: 'iPhone sürümü var mı?',
          a: 'Şu an yok; uygulama Android için geliştiriliyor (Android 8.0 ve üstü).',
        },
      ],
    },
    close: {
      title: 'Bir sonraki ödemeyi kaçırmayın',
      body: 'Google Play’den ücretsiz indirin. Kurulumdan sonra hesap açmanıza gerek yok.',
    },
  },

  en: {
    meta: {
      title: 'Money Agenda — credit card, instalment, loan and subscription tracker',
      description:
        'Credit card statement and due dates, instalments, loans, subscriptions and domain renewals in one calendar, with reminders before they are due. Free, works without sign-in, data stays on your phone.',
    },
    hero: {
      eyebrow: 'Android · built for Turkey',
      h1: 'When does your card close, and when is the instalment due?',
      lead: 'Money Agenda shows what is coming, not what is past. Card statement and due dates, instalments, loans, subscriptions and domain renewals gather in one calendar and remind you before the date arrives.',
      trust: ['Every feature is free', 'Works without signing in', 'Your data stays on your phone'],
    },
    stance: {
      title: 'Not a ledger — an obligation assistant',
      body: 'Most budgeting apps tell you what you spent. That is usually not the problem. The problem is missing the statement date and rolling into the next cycle, forgetting an instalment, letting a domain lapse quietly.',
      points: [
        {
          t: 'The home screen looks forward',
          d: 'Whatever is due today and in the coming days sits at the top — not last month’s chart.',
        },
        {
          t: 'The calendar maths is right',
          d: 'Statement day, due date, billing cycle, minimum payment — all computed by each card’s own rules.',
        },
        {
          t: 'Reminders actually arrive',
          d: 'Exact alarms are used; the schedule survives device idle and a reboot.',
        },
      ],
    },
    features: {
      title: 'What it keeps track of',
      lead: 'All of it in one calendar, so you are not opening separate apps.',
      items: [
        {
          t: 'Credit cards',
          d: 'Statement and due dates, billing cycles, minimum payment, balance and remaining limit.',
          href: '/en/features/',
        },
        {
          t: 'Instalments and loans',
          d: 'Instalment plans, loan amortisation, and effective cost including Turkish BSMV/KKDF levies.',
          href: '/en/features/',
        },
        {
          t: 'Subscriptions and renewals',
          d: 'Subscriptions, domains, hosting, SSL, insurance — anything that renews, with its date.',
          href: '/en/features/',
        },
        {
          t: 'Budgets and reports',
          d: 'Category budgets, goals, monthly reports; export to CSV, XLSX and PDF.',
          href: '/en/features/',
        },
        {
          t: 'Reminders',
          d: 'Alerts before and after the due date, quiet hours, a daily digest, a separate channel per type.',
          href: '/en/features/',
        },
        {
          t: 'Security',
          d: 'Encrypted local backup, PIN and fingerprint lock, amount masking.',
          href: '/en/features/',
        },
      ],
    },
    screens: {
      title: 'From the app',
      lead: 'A warm, calm interface: one accent colour, monospaced figures, no decoration for its own sake.',
      shots: [
        { file: '01-bugun', alt: 'Today screen showing the amount due this month, available balance and upcoming obligations' },
        { file: '05-kart-detay', alt: 'Card detail showing the balance, minimum payment, statement day and days left until the due date' },
        { file: '08-taksitler', alt: 'Instalments screen showing this month’s instalment total and the remaining plan' },
        { file: '02-raporlar', alt: 'Reports screen showing income and spending flow, the month-end estimate and a 12-month chart' },
      ],
    },
    local: {
      title: 'It knows the Turkish banking calendar',
      body: 'The calculations inside the app are written against Turkey-specific rules and covered by unit tests. Where a general budgeting app gives an approximate answer, this one gives an exact one.',
      bullets: [
        'The gap between statement day and due date is set per card',
        'Days that do not exist in every month (the 29th to 31st) shift correctly',
        'Loan cost accounts for the BSMV and KKDF levies',
        'Foreign currency amounts use the Turkish central bank rate',
        'Amounts are held to the kuruş; no decimal rounding drift',
      ],
    },
    privacy: {
      title: 'Your data stays on your phone',
      body: 'The app works fully without signing in; no feature depends on an account. Cloud backup is optional and does nothing until you turn it on.',
      bullets: [
        'No connection to your bank — there is no open banking integration',
        'No SMS read permission is requested',
        'Financial data such as amounts, card names and people’s names is never sent to an ad network or analytics service',
        'No AI is used; every calculation is deterministic and explained on screen',
      ],
    },
    faq: {
      title: 'Frequently asked',
      items: [
        {
          q: 'Is the app free?',
          a: 'Yes. <strong>Every feature is available in the free version</strong>; nothing sits behind a paywall. The free version shows an ad strip above the bottom bar. Pro (monthly, 6-month, yearly or lifetime) only removes that strip.',
        },
        {
          q: 'Where does my data go?',
          a: 'It stays on your phone. The app works fully without signing in. If you turn on cloud backup, your data is stored against your Google account. Your financial data is never sent to an ad network or analytics service.',
        },
        {
          q: 'Does it work offline?',
          a: 'Yes. The database is on the phone; entry, calculation and reminders all work offline. The internet is only needed for optional cloud backup and current exchange rates.',
        },
        {
          q: 'Does it connect to my bank?',
          a: 'No, deliberately. There is no open banking integration and no SMS read permission. You enter the records yourself; in return you share no banking credentials.',
        },
        {
          q: 'Do reminders actually arrive on time?',
          a: 'Exact alarms are used, so a reminder fires on time even when the device is idle. The schedule is rebuilt automatically after a reboot. Because some manufacturers’ battery managers can restrict apps, the app includes a step-by-step guide for your device brand and a test notification button.',
        },
        {
          q: 'Is there an iPhone version?',
          a: 'Not at the moment; the app is built for Android (8.0 and above).',
        },
      ],
    },
    close: {
      title: 'Do not miss the next payment',
      body: 'Download it free from Google Play. You do not need an account after installing.',
    },
  },
};
