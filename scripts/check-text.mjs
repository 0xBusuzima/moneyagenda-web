/**
 * Metinlerde yabanci alfabe karakteri var mi?
 *
 * Kiril "а" ile Latin "a" ekranda ayni gorunur ama farkli karakterlerdir. Yazarken
 * kazayla karisan boyle bir harf sessizce yayina cikar: sayfa dogru gorunur, fakat o
 * kelime aramada eslesmez ve kimse sebebini anlamaz.
 *
 * 2026-09-26'da bir blog yazisinda "Eklenmiyorsa" kelimesinin ortasinda Kiril "len"
 * bulundu. Gozle yakalanmasi mumkun degildi; bu denetim o yuzden hattin parcasi.
 *
 * Emoji, matematik isaretleri ve tipografik tirnaklar sorun degil - yalnizca Latin
 * disindaki *alfabeler* araniyor.
 */
import { readdir, readFile } from 'node:fs/promises';
import { join, sep } from 'node:path';

const KLASORLER = ['src/content', 'src/copy', 'src/pages'];
const UZANTILAR = ['.md', '.ts', '.astro'];

/** Kiril, Yunan, Ermeni, Ibrani, Arap bloklari. */
const YABANCI = /[Ͱ-ϿЀ-ӿ԰-֏֐-׿؀-ۿ]/g;

async function walk(dir) {
  const out = [];
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return out;
  }
  for (const e of entries) {
    const p = join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else if (UZANTILAR.some((u) => e.name.endsWith(u))) out.push(p);
  }
  return out;
}

const bulgular = [];
for (const kok of KLASORLER) {
  for (const dosya of await walk(kok)) {
    const metin = await readFile(dosya, 'utf8');
    for (const m of metin.matchAll(YABANCI)) {
      const satir = metin.slice(0, m.index).split('\n').length;
      const baglam = metin.slice(Math.max(0, m.index - 30), m.index + 30).replace(/\n/g, ' ');
      const kod = m[0].codePointAt(0).toString(16).toUpperCase().padStart(4, '0');
      bulgular.push(`${dosya.split(sep).join('/')}:${satir}  U+${kod} "${m[0]}"  …${baglam}…`);
    }
  }
}

if (bulgular.length) {
  console.error(`Latin disi alfabe karakteri: ${bulgular.length}`);
  for (const b of bulgular.slice(0, 30)) console.error('  ' + b);
  console.error('Bunlar genellikle kopyala-yapistir kazasidir; Latin karsiligiyla degistirin.');
  process.exit(1);
}
console.log('Metinlerde yabanci alfabe karakteri yok.');
