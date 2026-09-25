import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Metin sayfaları (özellikler, yasal metinler, destek…) Markdown olarak duruyor.
 *
 * Her sayfayı ayrı bir `.astro` dosyası olarak yazmak, yirmi sayfadan sonra yirmi ayrı
 * yerde tekrarlanan `<Base>` sarmalayıcısı demek. Markdown'da yalnızca metin var;
 * yerleşim tek yerde, `Prose.astro`'da.
 *
 * `path` frontmatter'ı sayfanın adresini belirliyor — dosya adı değil. Türkçe ve
 * İngilizce sürümler `route` anahtarıyla eşleşiyor; hreflang bağlantıları bu eşleşmeden
 * üretiliyor ve karşılığı olmayan sayfa için hiç üretilmiyor.
 */
const pages = defineCollection({
  loader: glob({ base: './src/content/pages', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    /** `<title>` etiketi; verilmezse `title` kullanılır. */
    seoTitle: z.string().optional(),
    description: z.string(),
    lang: z.enum(['tr', 'en']),
    /** Yayınlanacak adres, baştaki ve sondaki eğik çizgiyle. */
    path: z.string(),
    /** İki dildeki sürümü birbirine bağlayan anahtar. */
    route: z.string(),
    /** Başlığın altındaki giriş cümlesi. */
    lead: z.string().optional(),
    /** Yasal metinlerde görünen "Son güncelleme". */
    updated: z.string().optional(),
    noindex: z.boolean().optional(),
  }),
});

const blog = defineCollection({
  loader: glob({ base: './src/content/blog', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string().optional(),
    description: z.string(),
    lang: z.enum(['tr', 'en']),
    slug: z.string(),
    published: z.coerce.date(),
    updated: z.coerce.date().optional(),
    /** Yazının bağlandığı hesaplayıcı ya da özellik sayfası. */
    related: z.array(z.object({ label: z.string(), href: z.string() })).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { pages, blog };
