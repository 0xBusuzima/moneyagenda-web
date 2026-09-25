import sharp from 'sharp';
import { readdir } from 'node:fs/promises';
const files = (await readdir('assets/screens')).filter(f => f.endsWith('.png')).sort();
const W = 240, H = 520;
const thumbs = [];
for (let i = 0; i < files.length; i++) {
  const buf = await sharp('assets/screens/' + files[i]).resize(W, H, { fit: 'cover', position: 'top' }).toBuffer();
  thumbs.push({ input: buf, left: (i % 4) * W, top: Math.floor(i / 4) * H });
}
await sharp({ create: { width: W * 4, height: H * 2, channels: 3, background: '#000' } })
  .composite(thumbs).png().toFile('montage.png');
console.log(files.join('  |  '));
