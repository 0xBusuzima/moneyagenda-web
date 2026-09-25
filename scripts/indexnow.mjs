/**
 * Yeni ve degisen sayfalari IndexNow'a bildirir (Bing, Yandex ve digerleri).
 *
 * Google IndexNow'i kullanmiyor; orada Search Console gerekiyor. Turkiye'de Yandex
 * payi yok sayilamayacak kadar buyuk oldugu icin bu adim anlamli.
 *
 * Anahtar dogrulamasi dosya uzerinden: anahtarin kendisi alan adinin kokunde
 * <anahtar>.txt olarak duruyor. Gizli degil, zaten oyle tasarlanmis - "bu alan adina
 * bildirim gonderme yetkim var" demenin yolu o dosyayi koyabilmek.
 *
 * Dagitimi bloke etmez: bildirim basarisiz olursa site yine yayinda kalir.
 */
import { readFile, readdir } from 'node:fs/promises';

const HOST = 'moneyagenda.com.tr';
const SITE = `https://${HOST}`;

const key = (await readdir('public')).find((f) => /^[0-9a-f]{32}\.txt$/.test(f))?.replace('.txt', '');
if (!key) {
  console.error('IndexNow anahtari public/ altinda bulunamadi.');
  process.exit(0);
}

const sitemap = await readFile('dist/sitemap-0.xml', 'utf8');
const urlList = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);

if (!urlList.length) {
  console.error('Sitemap bos, bildirim gonderilmedi.');
  process.exit(0);
}

const res = await fetch('https://api.indexnow.org/indexnow', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json; charset=utf-8' },
  body: JSON.stringify({ host: HOST, key, keyLocation: `${SITE}/${key}.txt`, urlList }),
});

// 200 ve 202 basarili; 422 genellikle anahtar henuz yayinda degil demek.
console.log(`IndexNow: ${res.status} ${res.statusText} — ${urlList.length} adres bildirildi.`);
