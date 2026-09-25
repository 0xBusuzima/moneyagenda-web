/**
 * Sitenin tek gerçek kaynağı: ad, adresler, gezinme, çeviriler.
 *
 * Buradaki her şey tek yerde duruyor çünkü aynı metin hem `<title>`'da, hem JSON-LD'de,
 * hem Open Graph'ta geçiyor. Üç yere ayrı yazılsaydı biri güncellenip diğerleri
 * unutulurdu; arama motoruna bir şey, kullanıcıya başka şey söyleyen bir site çıkardı.
 */

export const SITE = {
  name: 'Money Agenda',
  domain: 'https://moneyagenda.com.tr',
  packageId: 'com.moneyagenda.app',
  email: 'yzcdev@gmail.com',
  playUrl: 'https://play.google.com/store/apps/details?id=com.moneyagenda.app',
  github: 'https://github.com/0xBusuzima',
} as const;

export type Lang = 'tr' | 'en';

export const LANGS: Lang[] = ['tr', 'en'];

/** `hreflang` ve `og:locale` için tam etiketler. */
export const LOCALE_TAG: Record<Lang, string> = {
  tr: 'tr-TR',
  en: 'en-US',
};

/**
 * Yol eşlemesi: her sayfanın iki dildeki adresi.
 *
 * Türkçe yollar Türkçe, İngilizce yollar İngilizce — `/en/ozellikler/` gibi melez bir
 * adres hem kullanıcıya hem arama motoruna tuhaf gelir. Anahtar, sayfanın kimliği;
 * `hreflang` bağlantıları buradan üretiliyor.
 */
export const ROUTES = {
  home: { tr: '/', en: '/en/' },
  features: { tr: '/ozellikler/', en: '/en/features/' },
  featuresCards: { tr: '/ozellikler/kredi-karti-takibi/', en: '/en/features/credit-cards/' },
  featuresLoans: { tr: '/ozellikler/taksit-ve-kredi/', en: '/en/features/instalments-and-loans/' },
  featuresRenewals: { tr: '/ozellikler/abonelik-ve-yenileme/', en: '/en/features/subscriptions/' },
  featuresBudget: { tr: '/ozellikler/butce-ve-rapor/', en: '/en/features/budget-and-reports/' },
  featuresAlerts: { tr: '/ozellikler/bildirimler/', en: '/en/features/reminders/' },
  why: { tr: '/neden-money-agenda/', en: '/en/why-money-agenda/' },
  tools: { tr: '/araclar/', en: '/en/tools/' },
  blog: { tr: '/blog/', en: '/en/blog/' },
  support: { tr: '/destek/', en: '/en/support/' },
  releases: { tr: '/surum-notlari/', en: '/en/release-notes/' },
  press: { tr: '/basin-kiti/', en: '/en/press-kit/' },
  privacy: { tr: '/gizlilik/', en: '/en/privacy/' },
  terms: { tr: '/kosullar/', en: '/en/terms/' },
  deleteAccount: { tr: '/hesap-silme/', en: '/en/delete-account/' },
} as const;

export type RouteKey = keyof typeof ROUTES;

/** Üst gezinmede görünenler. Sıra bilinçli: önce ne yaptığı, sonra neden, sonra araçlar. */
export const NAV: RouteKey[] = ['features', 'why', 'tools', 'blog', 'support'];

export const UI: Record<Lang, Record<string, string>> = {
  tr: {
    skip: 'İçeriğe geç',
    nav_features: 'Özellikler',
    nav_why: 'Neden Money Agenda',
    nav_tools: 'Araçlar',
    nav_blog: 'Blog',
    nav_support: 'Destek',
    cta: 'Google Play’den indir',
    cta_short: 'Ücretsiz indir',
    footer_legal: 'Yasal',
    footer_product: 'Ürün',
    footer_privacy: 'Gizlilik',
    footer_terms: 'Kullanım koşulları',
    footer_delete: 'Hesap silme',
    footer_releases: 'Sürüm notları',
    footer_press: 'Basın kiti',
    footer_note: 'Verileriniz telefonunuzda kalır. Bulut yedeği isteğe bağlıdır.',
    lang_other: 'English',
    toc: 'İçindekiler',
    updated: 'Güncellenme',
    published: 'Yayımlanma',
    read_more: 'Yazının tamamı',
    all_posts: 'Tüm yazılar',
    related: 'İlgili',
  },
  en: {
    skip: 'Skip to content',
    nav_features: 'Features',
    nav_why: 'Why Money Agenda',
    nav_tools: 'Tools',
    nav_blog: 'Blog',
    nav_support: 'Support',
    cta: 'Get it on Google Play',
    cta_short: 'Download free',
    footer_legal: 'Legal',
    footer_product: 'Product',
    footer_privacy: 'Privacy',
    footer_terms: 'Terms of use',
    footer_delete: 'Delete account',
    footer_releases: 'Release notes',
    footer_press: 'Press kit',
    footer_note: 'Your data stays on your phone. Cloud backup is optional.',
    lang_other: 'Türkçe',
    toc: 'Contents',
    updated: 'Updated',
    published: 'Published',
    read_more: 'Read the full post',
    all_posts: 'All posts',
    related: 'Related',
  },
};

export function t(lang: Lang, key: string): string {
  return UI[lang][key] ?? UI.tr[key] ?? key;
}

/** Bir sayfanın karşı dildeki adresi — `hreflang` ve dil değiştirici için. */
export function altPath(key: RouteKey, lang: Lang): string {
  return ROUTES[key][lang];
}

export function absolute(path: string): string {
  return new URL(path, SITE.domain).href;
}
