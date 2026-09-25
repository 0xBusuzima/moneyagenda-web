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
