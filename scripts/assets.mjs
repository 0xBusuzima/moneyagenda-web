/**
 * Görsel varlıkları siteye hazırlar: ekran görüntülerini WebP'ye çevirir, ikonu
 * boyutlandırır, paylaşım (Open Graph) görselini üretir.
 *
 * Kaynak PNG'ler depoda kalıyor ama siteye WebP gidiyor: aynı ekran görüntüsü
 * PNG olarak ~150 KB, WebP olarak ~35 KB. Sekiz görselde bu, mobil bağlantıda
 * bir saniyeden fazla fark demek.
 *
 * Çalıştırma: npm run assets
 */
import sharp from 'sharp';
import { readdir, mkdir } from 'node:fs/promises';
import { join } from 'node:path';

const SRC = 'assets/screens';
const SCREENS_OUT = 'public/screens';
const BRAND = 'public/brand';

/** Ekran görüntüleri: iki genişlik, WebP. */
async function screens() {
  await mkdir(SCREENS_OUT, { recursive: true });
  const files = (await readdir(SRC)).filter((f) => f.endsWith('.png'));
  for (const file of files) {
    const base = file.replace(/\.png$/, '');
    for (const width of [420, 840]) {
      const out = join(SCREENS_OUT, `${base}-${width}.webp`);
      await sharp(join(SRC, file)).resize({ width }).webp({ quality: 82 }).toFile(out);
    }
  }
  console.log(`ekran goruntusu: ${files.length} dosya x 2 genislik`);
}

/** İkon boyutları: apple-touch-icon ve PWA benzeri kullanımlar için. */
async function icons() {
  const src = join(BRAND, 'icon-512.png');
  for (const size of [180, 192, 256]) {
    await sharp(src).resize(size, size).png({ compressionLevel: 9 }).toFile(join(BRAND, `icon-${size}.png`));
  }
  console.log('ikon: 180, 192, 256');
}

/**
 * Paylaşım görseli.
 *
 * Sıfırdan metin dizmek yerine Play'in öne çıkan grafiği kullanılıyor: o görsel zaten
 * markanın kendi tipografisiyle tasarlandı. Burada yazı tipi raster'lamaya kalksaydık
 * sistemde hangi font varsa ona düşerdi ve paylaşım kartı mağaza sayfasına benzemezdi.
 */
async function og() {
  await mkdir('public/og', { recursive: true });
  const feature = await sharp('assets/feature-1024x500.png').resize({ width: 1140 }).toBuffer();
  await sharp({
    create: { width: 1200, height: 630, channels: 4, background: '#12100d' },
  })
    .composite([{ input: feature, gravity: 'centre' }])
    .png({ compressionLevel: 9 })
    .toFile('public/og/default.png');
  console.log('og: 1200x630');
}

await screens();
await icons();
await og();
