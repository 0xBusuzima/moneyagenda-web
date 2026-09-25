/**
 * Uretilen sitedeki ic baglantilarin hepsi gercekten var mi?
 *
 * Kirik bir ic baglanti derlemeyi bozmaz, sessizce yayina cikar ve ziyaretci 404 gorur.
 * Bu yuzden denetim dagitim hattinda: kirik baglanti varsa yayin durur.
 */
import { readdir, readFile } from 'node:fs/promises';
import { join, relative, sep } from 'node:path';

const DIST = 'dist';

async function walk(dir) {
  const out = [];
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else out.push(p);
  }
  return out;
}

const files = await walk(DIST);
const urls = new Set();
for (const f of files) {
  const rel = '/' + relative(DIST, f).split(sep).join('/');
  urls.add(rel);
  if (rel.endsWith('/index.html')) urls.add(rel.slice(0, -10));
}

const broken = [];
for (const f of files.filter((f) => f.endsWith('.html'))) {
  const html = await readFile(f, 'utf8');
  const from = '/' + relative(DIST, f).split(sep).join('/');
  for (const m of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const href = m[1];
    if (/^(https?:|mailto:|#|data:)/.test(href)) continue;
    const target = href.split('#')[0].split('?')[0];
    if (!target) continue;
    if (!urls.has(target)) broken.push(`${from} -> ${target}`);
  }
}

if (broken.length) {
  console.error(`Kirik ic baglanti: ${broken.length}`);
  for (const b of [...new Set(broken)].slice(0, 40)) console.error('  ' + b);
  process.exit(1);
}
console.log('Ic baglantilar saglam.');
