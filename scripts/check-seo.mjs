/**
 * Baslik ve aciklama uzunluklari arama sonucuna siğiyor mu?
 *
 * Google basligi ~60, aciklamayi ~160 karakterde kirpar. Kirpilan bir aciklama cumlenin
 * ortasinda kesilir; kisa olan ise sonucta bos yer birakir. Ikisi de tiklama oranini
 * dusurur ve derlemede hicbir uyari vermez - sayfa gayet saglikli gorunur.
 *
 * Esikler biraz gevsek tutuldu: Google piksel genisligine bakiyor, karakter sayisina
 * degil, ve bazen basligi kendi yeniden yaziyor. Amac mukemmel uzunluk degil, belirgin
 * sapmalari yakalamak.
 */
import { readdir, readFile } from 'node:fs/promises';
import { join, relative, sep } from 'node:path';

const DIST = 'dist';
const MAX_TITLE = 62;
const MIN_DESC = 110;
const MAX_DESC = 160;

async function walk(dir) {
  const out = [];
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

const sorunlar = [];
for (const dosya of await walk(DIST)) {
  const html = await readFile(dosya, 'utf8');
  // noindex sayfalari ve yonlendirmeler arama sonucunda gorunmuyor.
  if (/<meta name="robots" content="noindex/.test(html)) continue;

  const yol = '/' + relative(DIST, dosya).split(sep).join('/').replace(/index\.html$/, '');
  const title = html.match(/<title>([^<]*)<\/title>/)?.[1] ?? '';
  const desc = html.match(/<meta name="description" content="([^"]*)"/)?.[1] ?? '';
  const h1 = html.match(/<h1[\s>]/g)?.length ?? 0;

  if (!title) sorunlar.push(`${yol}  title yok`);
  else if (title.length > MAX_TITLE) sorunlar.push(`${yol}  title ${title.length} karakter (en fazla ${MAX_TITLE})`);

  if (!desc) sorunlar.push(`${yol}  description yok`);
  else if (desc.length < MIN_DESC) sorunlar.push(`${yol}  description ${desc.length} karakter (en az ${MIN_DESC})`);
  else if (desc.length > MAX_DESC) sorunlar.push(`${yol}  description ${desc.length} karakter (en fazla ${MAX_DESC})`);

  if (h1 !== 1) sorunlar.push(`${yol}  h1 sayisi ${h1} (tam 1 olmali)`);

  if (!/<link rel="canonical"/.test(html)) sorunlar.push(`${yol}  canonical yok`);
}

if (sorunlar.length) {
  console.error(`Arama sonucu meta sorunu: ${sorunlar.length}`);
  for (const s of sorunlar) console.error('  ' + s);
  process.exit(1);
}
console.log('Baslik, aciklama, h1 ve canonical: hepsi yerinde.');
