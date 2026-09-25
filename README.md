# moneyagenda-web

[moneyagenda.com.tr](https://moneyagenda.com.tr) — Money Agenda Android uygulamasının
tanıtım sitesi, blog ve yasal sayfalar.

Astro ile üretiliyor, GitHub Actions `dist/` dizinini GitHub Pages'e yayınlıyor.
**Depo kökündeki dosyalar sunulmuyor** — sunulan her şey `public/` ya da `src/` altından
gelir. `CNAME` ve `app-ads.txt` bu yüzden `public/` içinde.

```bash
npm install
npm run dev      # yerel sunucu
npm run build    # dist/ üretir
npm run assets   # ekran görüntülerini WebP'ye çevirir, ikon ve OG görseli üretir
```

Dağıtımdan önce `scripts/check-links.mjs` bütün iç bağlantıları denetler; kırık bağlantı
varsa yayın durur.

Plan ve SEO stratejisi: uygulama deposundaki `docs/15-WEB-SITESI-VE-SEO.md`.
