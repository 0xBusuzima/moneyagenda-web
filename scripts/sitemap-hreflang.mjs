/**
 * Sitemap'e tam hreflang haritasini isler.
 *
 * Astro'nun sitemap eklentisi dilleri **yol benzerligiyle** esliyor: `/x/` ile `/en/x/`.
 * Bizim Ingilizce yollarimiz ceviri oldugu icin (`/ozellikler/` -> `/en/features/`)
 * eslestiremiyor ve sitemap yalnizca ana sayfa cifti icin alternatif yaziyor.
 *
 * Sayfalarin kendi `<link rel="alternate" hreflang>` etiketleri dogru ve eksiksiz;
 * Google icin bu tek basina yeterli. Yine de sitemap'te de bulunmasi daha guclu bir
 * sinyal - ozellikle henuz taranmamis sayfalar icin.
 *
 * Dogruluk kaynagi cogaltilmiyor: harita uretilen HTML'den okunuyor, yani sayfalarda ne
 * yaziyorsa sitemap'te de o var. Ayri bir liste tutulsaydi ikisi ayrisabilirdi.
 *
 * Derlemeden sonra calisir: npm run build
 */
import { readdir, readFile, writeFile } from 'node:fs/promises';
import { join, relative, sep } from 'node:path';

const DIST = 'dist';

async function walk(dir) {
  const out = [];
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

/** Her sayfanin kendi HTML'inde ilan ettigi dil alternatifleri. */
const harita = new Map();
for (const dosya of await walk(DIST)) {
  const html = await readFile(dosya, 'utf8');
  if (/<meta name="robots" content="noindex/.test(html)) continue;

  const canonical = html.match(/<link rel="canonical" href="([^"]+)"/)?.[1];
  if (!canonical) continue;

  const alts = [...html.matchAll(/<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"/g)].map(
    (m) => ({ lang: m[1], href: m[2] }),
  );
  if (alts.length) harita.set(canonical, alts);
}

const yol = join(DIST, 'sitemap-0.xml');
let xml = await readFile(yol, 'utf8');
let islenen = 0;

xml = xml.replace(/<url>([\s\S]*?)<\/url>/g, (blok, ic) => {
  const loc = ic.match(/<loc>([^<]+)<\/loc>/)?.[1];
  const alts = loc && harita.get(loc);
  if (!alts) return blok;

  // Eklentinin kendi (eksik) alternatiflerini atip tam listeyi yaziyoruz.
  const temiz = ic.replace(/<xhtml:link[^>]*\/>/g, '');
  const satirlar = alts
    .map((a) => `<xhtml:link rel="alternate" hreflang="${a.lang}" href="${a.href}"/>`)
    .join('');
  islenen++;
  return `<url>${temiz}${satirlar}</url>`;
});

await writeFile(yol, xml, 'utf8');
console.log(`Sitemap hreflang: ${islenen} adrese tam harita islendi.`);
