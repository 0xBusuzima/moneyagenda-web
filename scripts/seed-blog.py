# -*- coding: utf-8 -*-
"""İlk blog yazılarını yazar.

**Rakam kuralı:** bu yazılardaki her sayı ya uygulamanın kodundan doğrulanmış bir
varsayılandır (BSMV/KKDF %15, `LoanEngine`) ya da açıkça "örnek" diye işaretlenmiştir.
Mevzuatla değişen oranlar (asgari ödeme oranı, kredi kartı azami faizi) güncel değer
olarak sunulmuyor — bugün doğru yazılan bir oran altı ay sonra yanlış olur ve yazı
sayfada durmaya devam eder.

Çalıştırma: python scripts/seed-blog.py
"""
import io
import os

OUT = 'src/content/blog'
POSTS = {}

POSTS['kredi-karti-kesim-tarihi-nedir'] = '''---
title: Kredi kartı kesim tarihi nedir, son ödeme tarihi nasıl hesaplanır
seoTitle: Kredi kartı kesim tarihi ve son ödeme tarihi nasıl hesaplanır
description: Kesim günü ekstrenin kapandığı, son ödeme günü borcun ödenmesi gereken tarihtir. İkisi arasındaki fark kartına göre değişir ve bu fark harcamanın ne zaman ödeneceğini belirler.
lang: tr
slug: kredi-karti-kesim-tarihi-nedir
published: 2026-09-25
related:
  - label: Kredi kartı takibi
    href: /ozellikler/kredi-karti-takibi/
  - label: Bugün yaptığım harcama hangi ekstreye düşer
    href: /blog/ekstre-donemi-hangi-harcama/
---

Kredi kartıyla ilgili en çok karıştırılan iki tarih bunlar. İkisi farklı şeydir ve
aralarındaki mesafe, bir harcamanın cebinizden ne zaman çıkacağını belirler.

## Kesim tarihi

**Kesim (hesap kesim) tarihi**, kartın o dönemki ekstresinin kapandığı gündür. O güne
kadar yapılan harcamalar bu ekstrede toplanır ve bir borç tutarı çıkar. Kesimden sonra
yaptığınız harcamalar **bir sonraki** ekstreye yazılır.

Kesim günü her ay aynıdır: ayın 12'siyse her ayın 12'sinde keser.

## Son ödeme tarihi

**Son ödeme tarihi**, kesilen ekstredeki borcun gecikmeye düşmeden ödenmesi gereken son
gündür. Kesimden sonra gelir ve aradaki süre bankaya ve karta göre değişir — genellikle
10 ila 15 gün arasındadır ama bu bir kural değil, kartın kendi ayarıdır.

> Bu yüzden "kredi kartlarının son ödemesi kesimden 10 gün sonradır" gibi genel bir
> varsayım işe yaramaz. Kendi kartınızın ekstresinde yazan iki tarihi bir kez bakıp not
> etmeniz gerekir.

## Aradaki farkın işinize yarayan tarafı

Harcamayı kesim gününden **hemen sonra** yaparsanız, o harcama bir sonraki ekstreye
düşer ve ödemesi neredeyse iki ay sonraya kadar uzar. Kesimden hemen **önce** yaparsanız
ödeme günü çok yakındır.

Bir örnek. Kesim günü ayın 12'si, son ödeme kesimden 10 gün sonra olsun:

| Harcama tarihi | Hangi ekstre | Ödeme günü |
|---|---|---|
| 11 Ocak | 12 Ocak ekstresi | 22 Ocak |
| 13 Ocak | 12 Şubat ekstresi | 22 Şubat |

İki gün arayla yapılan aynı harcamanın ödeme tarihi bir ay ötelendi. Büyük bir alışverişi
kesim gününü bilerek planlamak, faizsiz bir vade kazandırır.

## Ayın 29, 30 ve 31'i meselesi

Kesim günü ayın 31'i olan bir kartta şubat ne olur? Ya da 30'u olan bir kartta?

O ayda bulunmayan gün, **ayın son gününe kaydırılır**. Kesim günü 31 olan bir kart şubatta
28'inde (artık yılda 29'unda) keser. 1 Mart'a taşınmaz.

Bu, elle takip edenlerin en sık kaçırdığı ayrıntıdır ve yılda birkaç kez sürpriz yaratır:
şubatta beklediğinizden üç gün önce kesilir.

## Ödeme yaptığınızda ne olur

Son ödeme tarihinde ekstre borcunun tamamını öderseniz faiz işlemez. Bir kısmını
öderseniz kalan bakiyeye faiz başlar — ve faiz genellikle ekstre kesim tarihinden itibaren
hesaplanır, son ödeme tarihinden değil. Yani "asgariyi ödedim, gerisini gelecek ay
öderim" demek göründüğünden pahalıdır. Bunu ayrı bir yazıda ele aldık:
[asgari ödeme tuzağı](/blog/asgari-odeme-tuzagi/).

## Birden fazla kart varsa

Her kartın kendi kesim günü ve kendi ödeme aralığı vardır. Üç kartınız varsa ayda üç ayrı
kesim, üç ayrı son ödeme tarihi demektir. Bunları akılda tutmak mümkün ama bir ay
yoğunlaşıp kaçırmak da mümkün — ve kaçırılan bir son ödeme hem faiz hem de gecikme
kaydı demek.
'''

POSTS['ekstre-donemi-hangi-harcama'] = '''---
title: Bugün yaptığım harcama hangi ekstreye düşer
seoTitle: Ekstre dönemi nasıl işler, harcama hangi ekstreye yazılır
description: Ekstre dönemi bir kesim gününden diğerine kadar olan aralıktır. Kesim gününde yapılan harcamanın hangi döneme gireceği ise kartın kuralına bağlıdır.
lang: tr
slug: ekstre-donemi-hangi-harcama
published: 2026-09-25
related:
  - label: Kredi kartı takibi
    href: /ozellikler/kredi-karti-takibi/
  - label: Kesim tarihi ve son ödeme nasıl hesaplanır
    href: /blog/kredi-karti-kesim-tarihi-nedir/
---

**Ekstre dönemi**, bir kesim gününden bir sonrakine kadar geçen aralıktır. O aralıkta
yapılan her harcama aynı ekstrede toplanır ve tek bir borç olarak karşınıza çıkar.

## Aralığın sınırları

Kesim günü ayın 12'si olan bir kartta dönem şöyle işler:

> 13 Ocak → 12 Şubat arası harcamalar, **12 Şubat** ekstresinde toplanır.

Dikkat edilmesi gereken yer aralığın uçları. Dönem bir kesim gününün **ertesi günü**
başlar ve bir sonraki kesim gününde **biter**. Yani kesim gününün kendisi kapanan
dönemin son günüdür.

## Kesim gününde yapılan harcama

İşte karışan yer burası. 12 Şubat'ta, yani kesim gününün kendisinde yapılan harcama o gün
kapanan ekstreye mi girer, bir sonrakine mi?

Kural olarak **o gün kapanan ekstreye** girer. Ama pratikte iki şey bunu bozabilir:

- **İşlemin bankaya yansıma zamanı.** Kartla ödeme yaptığınız an ile işlemin hesabınıza
  düşmesi aynı an değildir. Akşam yapılan bir alışveriş ertesi güne sarkabilir.
- **Provizyon ve kesinleşme farkı.** Otel, araç kiralama ve akaryakıt gibi yerlerde önce
  bir provizyon alınır, kesin tutar sonra yansır. Kesinleşme tarihi kesimden sonraya
  düşerse harcama bir sonraki ekstreye gider.

Bu yüzden kesim gününe denk gelen harcamalarda "kesin olarak şu ekstreye girer" demek
zordur. Kritik bir tutarsa bir gün öncesine ya da bir gün sonrasına almak, belirsizliği
ortadan kaldırır.

## Taksitli harcamalar

Taksitli bir alışverişte ilk taksit, harcamanın düştüğü ekstrede görünür. Kalanlar
sonraki ekstrelere birer birer dağılır. Yani 12 taksitli bir alışveriş 12 ayrı ekstrede,
her ay aynı tutarla karşınıza çıkar.

Bunun bütçe tarafındaki etkisi şudur: bir aylık büyük harcama, on iki aylık sabit bir
yükümlülüğe dönüşür. Taksitli alışverişler üst üste binerse, aylık taksit toplamınız
farkında olmadan ciddi bir tutara ulaşabilir.

## Geri iadeler

Bir alışverişi iade ettiğinizde, iade tutarı **iadenin işlendiği** tarihteki döneme
yazılır. İade, harcamanın yapıldığı ekstreye geri gitmez. Bu yüzden kesim gününe yakın
yapılan bir iade, bir sonraki ekstrede alacak olarak görünür ve o ayki borcunuzu
düşürür — iade ettiğiniz ay değil, sonraki ay.

## Dönem toplamını takip etmek

Ekstre gelene kadar dönem içinde ne kadar harcadığınızı görmek, ekstre sürprizini
ortadan kaldırır. Bankaların uygulamaları bunu genellikle "dönem içi harcama" olarak
gösterir; harcamalarınızı ayrıca kendiniz tutuyorsanız, dönem aralığını doğru kurmanız
gerekir — ayın 1'i ile sonu arası değil, **kesim gününden kesim gününe**.
'''

POSTS['asgari-odeme-tuzagi'] = '''---
title: Asgari ödeme tuzağı — sadece asgariyi ödersen ne olur
seoTitle: Asgari ödeme nedir, sadece asgariyi ödersen borç ne kadar sürer
description: Asgari ödeme borcu kapatmaz, gecikmeyi önler. Kalan bakiyeye faiz işlemeye devam eder ve borcun ömrü beklediğinizden çok daha uzun olur.
lang: tr
slug: asgari-odeme-tuzagi
published: 2026-09-25
related:
  - label: Kredi kartı takibi
    href: /ozellikler/kredi-karti-takibi/
  - label: Kesim tarihi ve son ödeme nasıl hesaplanır
    href: /blog/kredi-karti-kesim-tarihi-nedir/
---

Ekstrede iki tutar yazar: **dönem borcu** ve **asgari ödeme tutarı**. Asgari ödeme,
kartın kapatılmaması ve gecikmeye düşülmemesi için ödemeniz gereken en küçük tutardır.

Yaygın yanlış anlama şu: asgariyi ödemek, borcu ödemek değildir. Asgariyi ödemek
**gecikmeyi önler**, borcu kapatmaz.

## Ne oluyor

Asgariyi ödediğinizde kalan bakiye devreder ve o bakiyeye faiz işler. Ertesi ay yeni
harcamalarınız bu devreden borcun üstüne biner. Yeni ekstrede borç daha büyüktür, asgari
tutar da daha büyüktür.

İki şey aynı anda olur:

1. Ödediğiniz paranın büyük kısmı **faize** gider, anapara az düşer
2. Yeni harcamalar eklendikçe bakiye toplamda **büyür**

## Bir örnek

Aşağıdaki rakamlar **örnektir** — asgari ödeme oranı ve kredi kartı faiz oranı mevzuatla
belirlenir ve değişir. Kendi ekstrenizde yazan oranları kullanın.

Diyelim 20.000 TL borcunuz var, aylık faiz %4, asgari ödeme oranı %20 ve **hiç yeni
harcama yapmıyorsunuz**:

| Ay | Dönem başı borç | Faiz | Ödenen (asgari) | Ay sonu borç |
|---|---|---|---|---|
| 1 | 20.000 | 800 | 4.160 | 16.640 |
| 2 | 16.640 | 666 | 3.461 | 13.844 |
| 3 | 13.844 | 554 | 2.880 | 11.519 |
| 6 | 7.973 | 319 | 1.658 | 6.634 |
| 12 | 2.645 | 106 | 550 | 2.200 |

Bir yıl sonra hâlâ borcunuz var — üstelik **hiç yeni harcama yapmadığınız** hâlde. Asgari
oran kalan borcun yüzdesi olduğu için ödediğiniz tutar her ay küçülür ve borç uzun bir
kuyruk bırakır.

Bir de bu tablonun her ay yeni harcama eklenen hâlini düşünün. Orada bakiye düşmez,
artar.

## Asgariyi de ödemezseniz

Asgari tutarın altında ödeme yapmak **gecikme** sayılır. Sonuçları daha ağırdır:

- Kalan borca gecikme faizi işler; bu oran normal akdi faizden yüksektir
- Kredi kayıt bürosundaki notunuz etkilenir, bu da sonraki kredi başvurularınızı etkiler
- Kart limitiniz düşürülebilir ya da kart kullanıma kapatılabilir

## Ne yapmalı

- **Tamamını ödeyin.** Mümkünse dönem borcunun tamamı. Faiz ancak böyle sıfır olur.
- **Tamamı mümkün değilse asgariden fazlasını ödeyin.** Asgarinin üstündeki her lira
  doğrudan anaparadan düşer ve borcun ömrünü kısaltır.
- **Yeni harcamayı durdurun.** Devreden bakiyesi olan bir kartla harcamaya devam etmek,
  borcu kapatmayı matematiksel olarak imkânsız hâle getirebilir.
- **Nakit avans kullanmayın.** Nakit avansta faiz genellikle çekildiği günden itibaren
  işler ve faizsiz dönem yoktur.

## Takip tarafı

Bu tablonun sizin kartınızdaki hâlini görmek, kararı kolaylaştırır. Ekstre borcu, asgari
tutar, ödenen ve kalan limit yan yana durduğunda "asgariyi ödeyeyim" kararı çok daha az
cazip görünür.
'''

POSTS['bsmv-kkdf-kredi-maliyeti'] = '''---
title: BSMV ve KKDF nedir, kredi maliyetini ne kadar değiştirir
seoTitle: BSMV ve KKDF nedir — kredinin gerçek maliyeti nasıl hesaplanır
description: Bankanın ilan ettiği faiz oranı ödediğiniz tutarın tamamı değildir. Tüketici kredilerinde faizin üzerine BSMV ve KKDF biner ve aylık maliyeti belirgin biçimde yükseltir.
lang: tr
slug: bsmv-kkdf-kredi-maliyeti
published: 2026-09-25
related:
  - label: Taksit ve kredi takibi
    href: /ozellikler/taksit-ve-kredi/
  - label: Asgari ödeme tuzağı
    href: /blog/asgari-odeme-tuzagi/
---

Banka "aylık %2,89 faizli ihtiyaç kredisi" diye ilan eder. Hesap makinesine %2,89 yazıp
taksiti hesaplarsanız, çıkan rakam bankanın söylediğinden düşük olur. Aradaki fark iki
kesintiden gelir.

## İkisi ne

**KKDF** — Kaynak Kullanımını Destekleme Fonu. **BSMV** — Banka ve Sigorta Muameleleri
Vergisi. İkisi de faizin üzerinden alınır, anaparanın değil.

Önemli nokta: bunlar bankanın ilan ettiği orana **dahil değildir** ama ödediğiniz paraya
dahildir. İlan edilen oran "faiz oranı"dır; ödediğiniz ise faiz artı bu iki kesintidir.

## Hesap nasıl işliyor

Money Agenda'nın kredi motorunda kullanılan formül şu:

> vergili aylık oran = ilan edilen aylık oran × (1 + BSMV + KKDF)

Uygulamadaki varsayılan oranlar **her ikisi için de %15**. Yani:

> vergili oran = ilan edilen oran × 1,30

Bu oranlar mevzuatla belirlenir, kredi türüne göre değişebilir ve zaman içinde değişir —
uygulamada kredi başına ayrı ayrı girilebilmesinin sebebi bu. Aşağıdaki hesap %15 + %15
varsayımıyla yapılmıştır.

## Rakamla

İlan edilen aylık oran %2,89 olsun:

| | Oran |
|---|---|
| İlan edilen aylık faiz | %2,89 |
| Vergili aylık oran (× 1,30) | **%3,757** |

Aradaki fark küçük bir yüzde gibi görünüyor ama taksit sayısı arttıkça toplam geri
ödemedeki etkisi büyür. 100.000 TL, 36 ay için:

| | Aylık taksit | Toplam geri ödeme |
|---|---|---|
| Vergisiz (%2,89) | ≈ 4.506 TL | ≈ 162.200 TL |
| **Vergili (%3,757)** | **≈ 5.112 TL** | **≈ 184.000 TL** |

Yaklaşık **21.800 TL** fark. Vergileri hesaba katmayan bir hesaplama, krediyi gerçekte
olduğundan ucuz gösterir.

## Nerede yok

Bu kesintiler her kredide yok:

- **Konut kredilerinde KKDF ve BSMV uygulanmaz.** Konut kredisinin ilan edilen oranı
  ödediğiniz orana çok daha yakındır.
- Ticari kredilerde durum farklıdır ve işletmenin vergi durumuna bağlıdır.

Yani ihtiyaç kredisi ile konut kredisinin ilan edilen oranlarını doğrudan karşılaştırmak
yanıltıcıdır — birinde üzerine %30 biniyor, diğerinde binmiyor.

## Karşılaştırma yaparken

İki bankanın ilan ettiği oranlar birbirine çok yakın olabilir ama masraflar, sigorta
zorunluluğu ve vade farkları toplamı değiştirir. Doğru karşılaştırma ölçüsü aylık oran
değil, **toplam geri ödeme** tutarıdır.

Bankadan kredi teklifi alırken sorulacak tek soru şu: *"Bu kredide toplamda ne kadar geri
ödeyeceğim?"* Tek bir rakam, bütün oranları ve kesintileri içinde barındırır.

## Erken kapatma

Krediyi erken kapatırsanız kalan anaparaya düşen faiz ve o faizin vergileri de düşer —
yani erken kapatma bu kesintilerden de tasarruf ettirir. Bankalar erken kapamada bir
komisyon uygulayabilir; kalan vadeye göre tasarrufun komisyondan büyük olup olmadığına
bakmak gerekir.
'''

POSTS['unutulan-abonelikler'] = '''---
title: Unutulan abonelikler yılda ne kadar sızdırıyor
seoTitle: Abonelik takibi — unutulan abonelikler yıllık maliyeti
description: Abonelikler bir kez kurulur, sonra kendiliğinden yenilenir. Aylık küçük tutarlar yıllık toplamda beklenenden büyük çıkar; alan adı ve hosting gibi yıllık olanlar ise tamamen gözden kaçar.
lang: tr
slug: unutulan-abonelikler
published: 2026-09-25
related:
  - label: Abonelik ve yenileme takibi
    href: /ozellikler/abonelik-ve-yenileme/
  - label: Bütçe ve rapor
    href: /ozellikler/butce-ve-rapor/
---

Aboneliklerin sinsi tarafı, kararın bir kez verilip ödemenin sürekli olmasıdır. Kaydolma
anında "ayda 149 lira" makul görünür. Bir yıl sonra o abonelik 1.788 liraya ulaşmıştır ve
arada onu kullanıp kullanmadığınızı kimse sormamıştır.

## Aylık küçük, yıllık büyük

Aylık tutarları 12 ile çarpmak basit bir işlem ama insanlar bunu nadiren yapar. Birkaç
tipik tutarın yıllık karşılığı:

| Aylık | Yıllık |
|---|---|
| 49 TL | 588 TL |
| 99 TL | 1.188 TL |
| 149 TL | 1.788 TL |
| 249 TL | 2.988 TL |

Dört beş tane aboneliğiniz varsa yıllık toplam çoğu zaman tahmininizin epey üstündedir.

## Görünmeyen kategori: dijital varlıklar

Asıl gözden kaçanlar yıllık yenilenenlerdir, çünkü yılda bir kez çıkarlar ve o an
genellikle beklenmedik bir zamandır:

- **Alan adı** — yıllık ya da çok yıllık
- **Hosting veya sunucu**
- **SSL sertifikası**
- **Yazılım lisansları** — tasarım araçları, geliştirici araçları
- **Sigortalar** — kasko, trafik, DASK, sağlık

Bunlar genellikle bir karta bağlanır ve kendiliğinden yenilenir. Kart değiştiğinde ya da
bakiye yetmediğinde yenileme başarısız olur ve durumu fark etmeniz haftalar sürebilir.
Alan adı düşerse geri almanın maliyeti, yenileme ücretinin çok üstüne çıkabilir.

## Üç adımlık temizlik

**1. Hepsini bir yere yazın.** Kart ekstrenizin son 12 ayını tarayın; düzenli tekrar eden
her tutarı not edin. Yıllık olanları yakalamak için 12 ay bakmak şart — 3 aya bakarsanız
yıllıkları göremezsiniz.

**2. Her biri için tek soru sorun.** "Bu ay bunu kullandım mı?" Cevap hayırsa ve son üç
aydır hayırsa, o abonelik artık bir alışkanlık değil, bir alışkanlığın kalıntısıdır.

**3. Yenileme tarihinden önce hatırlatma kurun.** İptal kararı, yenileme günü geldiğinde
değil, birkaç gün önce verilir. Yenileme gerçekleştikten sonra iptal etmek genellikle
parayı geri getirmez; yalnızca bir sonraki dönemi durdurur.

## Yıllığa geçmek her zaman kazanç değil

Yıllık ödeme çoğu serviste aylığa göre indirimlidir — tipik olarak iki ay bedava gibi.
Ama bu, o servisi bir yıl boyunca kullanacağınızdan eminseniz kazançtır. Emin
değilseniz, aylık kalmak size iptal etme özgürlüğü bırakır ve bu özgürlüğün de bir
değeri vardır.

Basit ölçüt: son altı aydır düzenli kullanıyorsanız yıllığa geçin. Aksi hâlde aylık
kalın.

## Takip etmenin kolay yolu

Bütün yenilemeleri tek bir takvimde tutmak, hem yıllık toplamı görünür kılar hem de
yenileme sürprizini ortadan kaldırır. Aboneliğin adını, tutarını, sıklığını ve bir
sonraki tarihini bir kez girdikten sonra iş bitmiştir — geri kalanı hatırlatmanın işi.
'''

os.makedirs(OUT, exist_ok=True)
for slug, body in POSTS.items():
    with io.open(os.path.join(OUT, slug + '.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)
print(str(len(POSTS)) + ' yazi yazildi')
