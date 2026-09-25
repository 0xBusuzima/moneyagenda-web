// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

/**
 * Money Agenda — moneyagenda.com.tr
 *
 * Statik çıktı, varsayılan sıfır JS. Sayfa başına JS yalnızca hesaplayıcılarda ve
 * orada da `client:visible` ile; pazarlama sayfası JavaScript beklememeli.
 */
export default defineConfig({
  site: 'https://moneyagenda.com.tr',
  trailingSlash: 'always',
  i18n: {
    defaultLocale: 'tr',
    locales: ['tr', 'en'],
    routing: {
      // Türkçe kök dizinde: /gizlilik/ — İngilizce /en/privacy/ altında.
      prefixDefaultLocale: false,
    },
  },
  /**
   * Eski adresler kirilmiyor.
   *
   * `gizlilik.html`, `kosullar.html` ve `hesap-silme.html` Play Console'a girili ve
   * disaridan baglanti almis olabilir. Statik barindirmada 301 donemiyoruz; Astro bu
   * yonlendirmeleri meta-refresh + canonical tasiyan sayfalar olarak uretiyor, Google
   * da bunu kalici yonlendirme gibi degerlendiriyor.
   */
  redirects: {
    '/gizlilik.html': '/gizlilik/',
    '/kosullar.html': '/kosullar/',
    '/hesap-silme.html': '/hesap-silme/',
  },
  integrations: [
    sitemap({
      i18n: {
        defaultLocale: 'tr',
        locales: { tr: 'tr-TR', en: 'en-US' },
      },
    }),
  ],
  build: {
    // Her sayfa kendi dizininde index.html — URL'ler .html uzantısı taşımıyor.
    format: 'directory',
  },
  compressHTML: true,
});
