# -*- coding: utf-8 -*-
"""Blog yazıları 6-10.

Rakam kuralı ilk turdakiyle aynı: her sayı ya hesaplanarak doğrulandı ya da açıkça
"örnek" diye işaretli. Bileşik oranlar `(1+i)^12 - 1` ile hesaplandı; örtülü faiz
(taksitli fiyattan geri çıkarılan oran) ikili arama ile bulundu.

Çalıştırma: python scripts/seed-blog-2.py
"""
import io
import os

OUT = 'src/content/blog'
POSTS = {}

POSTS['faizsiz-taksit-gercekten-faizsiz-mi'] = '''---
title: "\\"Faizsiz taksit\\" gerçekten faizsiz mi"
seoTitle: Faizsiz taksit gerçekten faizsiz mi — gizli vade farkı
description: Taksitte faiz görünmüyorsa maliyet peşin fiyatta saklıdır. Peşin fiyatı bilmeden taksitin ucuz olup olmadığını söylemek mümkün değil.
lang: tr
slug: faizsiz-taksit-gercekten-faizsiz-mi
published: 2026-09-26
related:
  - label: Taksit planı hesaplama
    href: /araclar/taksit-plani-hesaplama/
  - label: BSMV ve KKDF nedir
    href: /blog/bsmv-kkdf-kredi-maliyeti/
---

Ekranda "12 taksit, faizsiz" yazıyor. Toplam ödeyeceğiniz tutar, etiket fiyatının aynısı.
Görünürde faiz yok. Peki bu gerçekten bedava bir vade mi?

## Maliyet nereye saklanıyor

Satıcı taksitli satışta bankaya komisyon öder. Bu komisyon ortadan kaybolmaz — fiyata
girer. Yani "faizsiz taksit" çoğu zaman şu anlama gelir: **etiket fiyatı, taksit
komisyonunu zaten içeriyor.**

Bunu görmenin tek yolu peşin fiyatı sormaktır. Peşin alana indirim yapılıyorsa, indirim
tutarı taksitin gerçek maliyetidir.

## Rakamla

Bir ürün 12 taksitle **12.000 TL**, peşin **10.800 TL** olsun:

| | |
|---|---|
| Taksitli toplam | 12.000 TL |
| Peşin fiyat | 10.800 TL |
| Fark | **1.200 TL** |
| Peşine göre artış | **%11,1** |

"Faizsiz" denilen bu işlemde 10.800 TL'lik bir malı 12 ay boyunca 1.000 TL taksitle
ödüyorsunuz. Bu nakit akışını bir krediymiş gibi çözersek örtülü aylık faiz
**%1,66** çıkıyor — bileşik yıllık karşılığı **%21,8**.

Faiz yok değil. Faiz var, sadece adı konmamış.

## Ne zaman gerçekten kazançlı

Bu, taksitin her zaman kötü olduğu anlamına gelmiyor. Örtülü oranın enflasyondan ya da
paranızın alternatif getirisinden düşük olduğu durumlarda taksit **kazançlıdır** — parayı
elinizde tutup değerlendirirsiniz, ödemeyi geleceğin daha ucuz lirasıyla yaparsınız.

Karar için sorulacak soru şu: *bu örtülü oran, paramı başka yerde değerlendirsem elde
edeceğim getiriden yüksek mi?*

- **Peşin fiyat taksitliyle aynıysa** taksit gerçekten bedava bir vadedir; almamak için
  sebep yok.
- **Peşin fiyat belirgin düşükse** aradaki farkı örtülü faiz olarak hesaplayın ve
  karşılaştırın.

## Kaçınılması gereken karıştırma

Taksit sayısı arttıkça aylık tutar düştüğü için ürün ucuzlamış gibi hissettirir. Oysa
değişen tek şey ödemenin yayılmasıdır. **Karşılaştırma aylık taksit üzerinden değil,
toplam ödenen üzerinden yapılmalı.**

Bir de şu var: taksitli alışverişler üst üste binince aylık taksit toplamınız farkında
olmadan büyür ve her ay ekstrede karşınıza çıkar. Bir aylık karar, aylarca süren sabit
bir yükümlülüğe dönüşür.

## Pratik yöntem

1. Kasada **"peşin ne kadar?"** diye sorun. Cevap taksitliyle aynıysa taksit yapın.
2. Fark varsa, farkı peşin fiyata bölüp yüzdeye çevirin.
3. O yüzde size yüksek geliyorsa peşin ödeyin; düşük geliyorsa taksit yapın.

[Taksit planı hesaplayıcısına](/araclar/taksit-plani-hesaplama/) peşin fiyatı da
girerseniz bu farkı sizin için çıkarır.
'''

POSTS['aylik-faiz-yillik-maliyet-farki'] = '''---
title: Aylık faiz ile yıllık maliyet arasındaki fark
seoTitle: Aylık faiz yıllık kaç eder — basit ve bileşik oran farkı
description: Aylık %2,89 faiz yılda %34,68 değil, %40,76 eder. Aradaki fark bileşik etkidir ve vergiler eklenince daha da büyür.
lang: tr
slug: aylik-faiz-yillik-maliyet-farki
published: 2026-09-26
related:
  - label: Kredi maliyeti hesaplama
    href: /araclar/kredi-maliyeti-hesaplama/
  - label: BSMV ve KKDF nedir
    href: /blog/bsmv-kkdf-kredi-maliyeti/
---

Aylık faiz oranını 12 ile çarpmak, yıllık maliyeti bulmanın doğru yolu değil. Çarpım
size **basit** yıllık oranı verir; ödediğiniz ise **bileşik** orandır ve her zaman daha
yüksektir.

## İki hesap

Aylık %2,89 faizli bir kredi düşünün.

| | Hesap | Sonuç |
|---|---|---|
| Basit yıllık | 2,89 × 12 | %34,68 |
| Bileşik yıllık | (1 + 0,0289)¹² − 1 | **%40,76** |

Aradaki 6 puanlık fark, faizin faize binmesinden gelir. Kredi taksitli ödendiği için
anapara her ay azalır ama oran aynı kaldığından bileşik etki yine de işler.

## Vergiler eklenince

Türkiye'de tüketici kredilerinde ilan edilen orana BSMV ve KKDF biner — ikisi de %15
iken oran 1,30 ile çarpılır. Aynı kredi için:

| | Aylık oran | Basit yıllık | Bileşik yıllık |
|---|---|---|---|
| İlan edilen | %2,890 | %34,68 | %40,76 |
| **Vergili** | **%3,757** | %45,08 | **%55,67** |

Bankanın vitrinindeki %2,89 ile gerçekte katlandığınız yıllık %55,67 arasındaki mesafe
budur. İkisi de doğru sayılardır — farklı şeyleri ölçerler.

## Hangi sayıya bakmalı

Kredi karşılaştırırken bileşik oranı hesaplamaya çalışmayın; daha basit ve daha güvenilir
bir ölçüt var:

> **Toplam geri ödeme.**

Tek bir rakam, bütün oranları, vergileri ve vadeyi içinde barındırır. İki teklifi
karşılaştırmak için "hangisinde toplamda daha az para veriyorum" sorusu yeterlidir.

Bankadan teklif alırken sorulacak cümle: *"Bu kredide toplamda ne kadar geri
ödeyeceğim?"*

## Vade uzadıkça

Aylık taksit düştüğü için uzun vade ucuz hissettirir. Oysa vade uzadıkça toplam faiz
**artar** — daha uzun süre borçlu kalırsınız. Aynı kredide 12 ay yerine 36 ay seçmek
aylık yükü hafifletir ama toplam maliyeti belirgin biçimde yükseltir.

[Kredi maliyeti hesaplayıcısında](/araclar/kredi-maliyeti-hesaplama/) vadeyi değiştirip
toplam geri ödemenin nasıl hareket ettiğini görebilirsiniz.

## Mevduat tarafında da aynı

Bu matematik tersine de çalışır: aylık %3 getiri vaat eden bir yatırım, yılda %36 değil
%42,6 eder — eğer getiri her ay anaparaya ekleniyorsa. Eklenmiyorsa %36'dır. "Bileşik mi
basit mi" sorusu her iki yönde de sonucu değiştirir.
'''

POSTS['alan-adi-hosting-yenileme'] = '''---
title: Alan adı ve hosting yenilemesini kaçırmamak
seoTitle: Alan adı yenileme takibi — süresi dolarsa ne olur
description: Alan adı süresi dolduğunda site kapanır, e-postalar düşer ve geri alma maliyeti yenileme ücretinin çok üstüne çıkabilir. Kaçırmamak için ne yapmalı.
lang: tr
slug: alan-adi-hosting-yenileme
published: 2026-09-26
related:
  - label: Abonelik ve yenileme takibi
    href: /ozellikler/abonelik-ve-yenileme/
  - label: Abonelik maliyeti hesaplama
    href: /araclar/abonelik-maliyeti-hesaplama/
---

Alan adı yenilemesi, kaçırıldığında en pahalıya mal olan ödemelerden biridir — ve en
kolay kaçırılanı. Yılda bir kez çıkar, hatırlatması genellikle tek bir e-postadır ve o
e-posta çoğu zaman kullanılmayan bir adrese gider.

## Süre dolduğunda ne oluyor

Alan adı süresi dolar dolmaz kimse kapmaz; önce bir dizi aşamadan geçer. Genel işleyiş
şöyledir (kayıt kuruluşuna ve uzantıya göre değişir):

1. **Süre dolar.** Site ve e-posta çalışmayı durdurabilir.
2. **Ek ödeme süresi.** Normal ücretle yenilenebildiğiniz bir pencere açılır.
3. **Kurtarma dönemi.** Hâlâ sizindir ama yenileme ücreti **çok daha yüksektir** —
   normal yenilemenin birkaç katı olabilir.
4. **Serbest bırakma.** Alan adı yeniden herkese açılır.

En kritik nokta ikinci ve üçüncü aşama arasındaki geçiş. Bir hafta gecikme normal ücretle
kapanabilirken, bir ay gecikme kurtarma ücretine düşebilir.

## Kurumsal alan adlarında risk daha yüksek

Site kapanmasının maliyeti yalnızca yenileme ücreti değildir:

- **E-postalar düşer.** Alan adına bağlı kurumsal e-posta adresleri çalışmaz. Gelen
  e-postalar geri döner, gönderen tarafta "adres yok" hatası görünür.
- **Arama sonuçlarındaki yeriniz etkilenir.** Uzun süre erişilemeyen bir site
  dizinlenmeden düşebilir.
- **SSL sertifikası yenilenemez**, tarayıcılar güvenlik uyarısı gösterir.
- **Bağlı servisler kopar** — ödeme sağlayıcıları, webhook'lar, doğrulama kayıtları.

## Otomatik yenileme neden yetmiyor

"Otomatik yenileme açık" demek güvende olduğunuz anlamına gelmez. Başarısız olmasının
yaygın sebepleri:

- **Kart değişmiş ya da süresi dolmuş.** En sık sebep bu.
- **Kart limiti o gün yetmemiş.**
- **Kayıt kuruluşundaki e-posta adresi artık okunmuyor**, uyarı görünmüyor.
- **Hesap başka birine ait** — ajans, eski çalışan, devreden ortak.

Bunların hepsinde sistem size haber verdiğini sanır, siz haber almazsınız.

## Ne yapmalı

**1. Bir envanter çıkarın.** Elinizdeki her alan adı, hosting, SSL ve lisansın yenileme
tarihini tek yere yazın. Kayıt kuruluşu panelinde durması yetmez — oraya girmeyi
hatırlamanız gerekir.

**2. Takvime değil, hatırlatıcıya bağlayın.** Yenilemeden **en az bir ay önce** uyarı
kurun. Bir ay, kartı güncellemeye ve gerekirse kayıt kuruluşunu değiştirmeye yeter.

**3. Kayıttaki iletişim adresini kontrol edin.** Alan adının kendi uzantısındaki bir
e-postayı iletişim adresi yapmayın — alan adı düşerse uyarı e-postası da düşer.

**4. Uzun süreli yenileyin.** Kritik alan adlarını 2-5 yıllık yenilemek, hem riski
azaltır hem çoğu kayıt kuruluşunda daha ucuzdur.

**5. Transfer kilidini açık tutun.** Yetkisiz transferlere karşı koruma sağlar.

## Hosting ve SSL

Aynı disiplin hosting ve sertifika için de geçerli. Hosting kesintisinde veriniz
genellikle bir süre korunur ama site kapanır; bazı sağlayıcılarda belirli bir süre sonra
**yedekler de silinir**. Sertifika yenilemesi otomatikse bile, otomasyonun sessizce
bozulduğunu ancak tarayıcı uyarı verince fark edersiniz.

En sağlıklısı bu üçünü — alan adı, hosting, sertifika — aynı listede tutup tarihleri yan
yana görmek. [Abonelik maliyeti hesaplayıcısı](/araclar/abonelik-maliyeti-hesaplama/)
yıllık toplamı çıkarır; tarihleri takip etmek içinse bir hatırlatıcı gerekir.
'''

POSTS['zamli-yilda-butce'] = '''---
title: Zamlı bir yılda aylık bütçe nasıl kurulur
seoTitle: Enflasyonda bütçe nasıl yapılır — zamlı dönemde aylık plan
description: Fiyatlar sürekli değişirken geçen ayın rakamlarıyla bütçe kurmak işe yaramaz. Sabit ve değişken giderleri ayırıp bütçeyi yürüyen ortalamaya bağlamak gerekir.
lang: tr
slug: zamli-yilda-butce
published: 2026-09-26
related:
  - label: Bütçe ve rapor
    href: /ozellikler/butce-ve-rapor/
  - label: Gelir gider takibi nasıl sürdürülür
    href: /blog/gelir-gider-takibi-yontem/
---

Klasik bütçe tavsiyesi şudur: geçen ay ne harcadığına bak, bu aya ona göre limit koy.
Fiyatların sık değiştiği bir yılda bu yöntem her ay sizi yanıltır — limiti aşarsınız,
suçlu hissedersiniz, sonra bütçe tutmayı bırakırsınız.

Sorun disiplinde değil, yöntemde.

## Sabit ve değişkeni ayırın

İlk adım, giderleri değişme davranışına göre ikiye ayırmak:

**Sabitler** — kira, aidat, kredi taksiti, sigorta, abonelikler. Tutarları belli ve
genellikle yılda bir değişir. Bunlar bütçe kalemi değil, **takvim kalemidir**: ne zaman
çıkacağını bilirsiniz.

**Değişkenler** — market, ulaşım, yeme-içme, giyim. Bunlar hem miktar hem fiyat olarak
oynar. Bütçe asıl burada kurulur.

Zam etkisi bu ikisinde farklı işler: sabitlerde **basamaklıdır** (bir gün birden %30
artar ve öyle kalır), değişkenlerde **sürekli sızar**.

## Değişkenlerde son üç ayın ortalaması

Geçen ayın tek başına bir anlamı yok — bayram, tatil, tek seferlik bir alışveriş onu
bozar. Daha sağlam ölçüt **son üç ayın günlük ortalaması**:

> ay sonu tahmini = kalan gün sayısı × son üç ayın günlük ortalama değişken harcaması

Üç ay, hem mevsimsel dalgalanmayı yumuşatacak kadar uzun hem de fiyat artışını takip
edecek kadar kısa. Money Agenda'nın ay sonu tahmini de tam olarak bu formülü kullanır ve
formülü ekranda açıkça yazar — çünkü nereden geldiğini söyleyemeyen bir tahmin
güvenilmez.

## Bütçeyi yüzdeyle değil, gerçekle güncelleyin

"Enflasyon %40, bütçeyi %40 artırayım" demek çekici ama yanlış. Genel enflasyon sizin
sepetinizle aynı oranda artmaz: market sepetiniz farklı, ulaşım alışkanlığınız farklı.

Doğrusu, bütçeyi **kendi verinizin yürüyen ortalamasına** bağlamak. Her ay başında geçmiş
üç ayın ortalamasına bakıp limiti ona göre düzeltmek, kendi enflasyonunuzu ölçmek
demektir.

## Sabitleri yılda bir gözden geçirin

Sabitler sessizce birikir. Yılda bir kez, tercihen zam döneminde, listeyi baştan aşağı
okuyun:

- Hâlâ kullanıyor muyum?
- Daha ucuz bir alternatifi var mı?
- Yıllık ödemeye geçersem indirim var mı? (Bir yıl kullanacağımdan emin miyim?)

Bu, değişken harcamalarda kuruş kısmaktan çok daha büyük tasarruf üretir — çünkü sabitler
her ay otomatik çıkar ve kimse fark etmez.

## Zam beklentisini bütçeye yazmayın

Gelecek zammı tahmin edip bütçeye şimdiden eklemek, bugünkü kararları bozar. Bunun yerine
küçük bir **tampon** bırakın: aylık bütçenin %5-10'u kadar, kalem belirtilmemiş bir pay.
Zam geldiğinde onu emer; gelmediğinde birikime döner.

## Aşıldığında ne yapmalı

Bütçe aşımı bir başarısızlık değil, bir sinyaldir. Sinyali ay sonunda değil, **aşıldığı
gün** almak gerekir — kalan günlerde davranışı değiştirme şansı ancak o zaman olur. Ay
bittikten sonra öğrenilen bir aşımın hiçbir işlevi yoktur.

## En önemlisi

Bütçe harcamayı yasaklamak için değil, **ay bitmeden nerede durduğunuzu görmek** için
vardır. Tuttuğu sürece basit kalsın; karmaşık bir bütçe iki ay sonra terk edilir.
'''

POSTS['gelir-gider-takibi-yontem'] = '''---
title: "Gelir gider takibi: defter tutmadan sürdürülebilir yöntem"
seoTitle: Gelir gider takibi nasıl yapılır — sürdürülebilir yöntem
description: Her kuruşu kaydetmek iki hafta sürer ve biter. Takibi sürdürülebilir kılan şey eksiksizlik değil, doğru şeyi kaydetmek.
lang: tr
slug: gelir-gider-takibi-yontem
published: 2026-09-26
related:
  - label: Zamlı bir yılda aylık bütçe
    href: /blog/zamli-yilda-butce/
  - label: Bütçe ve rapor
    href: /ozellikler/butce-ve-rapor/
---

Gelir gider takibi denemelerinin çoğu aynı şekilde biter: ilk iki hafta her kuruş
kaydedilir, üçüncü hafta birkaç gün atlanır, dördüncü hafta uygulama silinir.

Sebep tembellik değil. Yöntem sürdürülemez.

## Eksiksizlik hedefi yanlış hedef

"Her harcamayı kaydedeceğim" demek, günde 8-10 kayıt demek. Bunun karşılığında ne
öğrenirsiniz? Zaten bildiğiniz bir şeyi: paranın nereye gittiğini kabaca biliyorsunuzdur.

Takibin asıl değeri başka yerde: **ne zaman ne ödeyeceğinizi bilmekte.** Kartın kesim
günü, taksitin düşeceği ay, aboneliğin yenileneceği tarih. Bunlar unutulduğunda gerçek
para kaybedilir — gecikme faizi, düşen alan adı, kaçırılan ödeme.

## Önce yükümlülükler, sonra harcamalar

Sıralamayı tersine çevirin:

**1. Yükümlülükleri bir kez girin.** Kartların kesim ve son ödeme günleri, kredi ve
taksitler, abonelikler, sigortalar. Bunlar bir kez girilir ve kendi kendine ilerler.
Günlük emek istemez ama en çok parayı burası kurtarır.

**2. Sabit gelirleri girin.** Maaş, kira geliri. Bunlar da bir kez.

**3. Harcamaları kaba kategorilerle takip edin.** Market, ulaşım, yeme-içme, diğer.
Dört-beş kategori yeter. "Market" ile "manav"ı ayırmak size ay sonunda hiçbir karar
kazandırmaz.

## Günde bir dakika kuralı

Her harcamayı anında kaydetmek yerine günde bir kez, sabit bir anda otur ve o günü gir.
Akşam, telefonu bırakmadan önce. Bir dakika sürer.

Kaçırdığınız günü telafi etmeye çalışmayın. Geriye dönük üç günü hatırlamaya çalışmak,
takibi bırakmanın en yaygın sebebidir. Kaçırdıysanız o günü atlayın ve devam edin —
eksik bir takip, hiç takipten sonsuz kat iyidir.

## Nakit için ayrı bir yöntem

Nakit harcamaları tek tek kovalamak yorucudur. Daha pratik yol: ayda bir kez cüzdandaki
nakdi sayıp farkı tek kalem "nakit harcama" olarak girmek. Kalemi bilmezsiniz ama toplamı
bilirsiniz ve bütçe için toplam yeterlidir.

## Hangi sayıya bakmalı

Ay sonunda üç sayı yeter:

1. **Bu ay ne kadar geldi**
2. **Bu ay ne kadar gitti**
3. **Önümüzdeki 30 günde ne ödenecek**

Üçüncüsü en değerlisi ve çoğu uygulamada en zor bulunanıdır — çünkü çoğu uygulama
geçmişe bakar.

## Ne zaman detaya inmeli

Detaylı kategori takibi bir soruya cevap ararken anlamlıdır: "Yeme-içme gerçekten bu
kadar mı?" gibi. O zaman bir ay boyunca yalnızca o kategoriyi detaylı tutun, cevabı alın,
sonra kaba takibe geri dönün.

Sürekli detay, sürekli emek demektir ve emek biter.

## Özet

- Yükümlülükleri bir kez gir, kendi kendine ilerlesin
- Harcamaları kaba kategorilerle, günde bir dakika
- Kaçırılan günü telafi etmeye çalışma
- Ay sonunda üç sayıya bak, en önemlisi "sırada ne var"

Bu yöntemin işe yaraması için özel bir uygulama gerekmiyor; bir kâğıt da olur. Ama
yükümlülük tarafını hatırlatan bir şey kullanmak, kaçırılan ödemelerin önüne geçer —
[Money Agenda](/) tam olarak bunun için var.
'''

os.makedirs(OUT, exist_ok=True)
for slug, body in POSTS.items():
    with io.open(os.path.join(OUT, slug + '.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)
print(str(len(POSTS)) + ' yazi yazildi')
