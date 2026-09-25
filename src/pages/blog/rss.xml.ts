import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE } from '../../config';

/**
 * Blog akışı.
 *
 * Taslaklar dışarıda: yayımlanmamış bir yazının akışa düşmesi, okuyucuya var olmayan
 * bir adres göstermek demek.
 */
export async function GET(context: { site: URL }) {
  const posts = (await getCollection('blog', (p) => p.data.lang === 'tr' && !p.data.draft)).sort(
    (a, b) => b.data.published.getTime() - a.data.published.getTime(),
  );

  return rss({
    title: SITE.name + ' — Blog',
    description:
      'Kredi kartı takvimi, kredi maliyeti ve bütçe üzerine yazılar. Hesabın nasıl yapıldığı her yazıda açıkça yazıyor.',
    site: context.site,
    customData: '<language>tr-TR</language>',
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.published,
      link: '/blog/' + post.data.slug + '/',
    })),
  });
}
