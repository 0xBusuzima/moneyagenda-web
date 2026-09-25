# -*- coding: utf-8 -*-
"""Türkçe metin sayfalarını yazar.

Tek dosyada toplandı çünkü hepsi aynı frontmatter şemasını kullanıyor ve aralarındaki
iç bağlantıların tutarlı olması gerekiyor. Sayfa sayfa yazılsaydı, bir adresi
değiştirdiğinde ona bağlanan öbür sayfaları bulmak elle arama işi olurdu.

Çalıştırma: python scripts/seed-pages.py
"""
import io
import os

OUT = 'src/content/pages/tr'

PAGES = {}

PAGES['gizlilik'] = ('''---
title: Gizlilik Politikası
seoTitle: Gizlilik Politikası — hangi veriler işleniyor
description: Money Agenda hangi verileri işler, nerede saklar, kiminle paylaşır. Kayıtlarınız varsayılan olarak yalnızca telefonunuzda tutulur.
lang: tr
path: /gizlilik/
route: privacy
lead: Money Agenda (com.moneyagenda.app) kişisel finans ve yükümlülük takibi için tasarlanmış bir Android uygulamasıdır. Bu politika, uygulamanın hangi verileri işlediğini açıklar.
updated: "Son güncelleme: 15 Eylül 2026"
---

> **Özet:** Kayıtlarınız varsayılan olarak yalnızca telefonunuzda tutulur. Google ile
> giriş yapmazsanız cihazınızdan hiçbir finansal veri çıkmaz. Ücretsiz sürümde reklam
> gösterilir; reklam ağı finansal kayıtlarınızı görmez.

## Toplanan veriler

**Giriş yapılmazsa:** Hiçbir veri toplanmaz. Tüm kayıtlar telefonunuzdaki yerel
veritabanında kalır.

**Google ile giriş yapılırsa** (isteğe bağlı), bulut yedeği için şunlar işlenir:

- **Hesap tanımlayıcısı:** Google hesabınızın e-posta adresi ve kullanıcı kimliği (uid)
- **Uygulama içi kayıtlarınız:** işlemler, hesaplar, kartlar, taksitler, krediler,
  abonelikler, bütçeler ve kategoriler

## Verinin nerede tutulduğu

Bulut yedeği Google Firebase (Firestore) üzerinde saklanır. Veriler Google Cloud'un
Avrupa bölgesinde barındırılır. Erişim, yalnızca kendi hesabınıza ait kayıtlarla
sınırlıdır; güvenlik kuralları başka bir kullanıcının verisine erişimi engeller.

## Paylaşım ve kullanım amacı

- **Finansal verileriniz satılmaz ve reklam amacıyla kullanılmaz.** Tutarlar, kart
  adları, kişi adları, kategoriler ve bütçeler reklam ağına ya da başka bir üçüncü tarafa
  hiçbir koşulda gönderilmez.
- **Analitik veya çökme raporlama servisi kullanılmaz.**
- Bulut yedeği verileri yalnızca size ait yedeğin saklanması ve cihazlarınız arasında
  eşitlenmesi için işlenir.

## Reklamlar

Uygulamanın ücretsiz sürümünde ekranın alt kısmında bir reklam şeridi gösterilir.
Reklamlar Google AdMob tarafından sunulur ve AdMob bu iş için şu verileri işleyebilir:

- Reklam kimliği (Android Advertising ID) ve yaklaşık konum (IP adresinden ülke/şehir
  düzeyinde)
- Cihaz ve uygulama bilgisi: cihaz modeli, işletim sistemi sürümü, uygulama sürümü
- Reklam etkileşimi: reklamın gösterilip gösterilmediği, tıklanıp tıklanmadığı

Bu verileri Google kendi sorumluluğunda işler. **Uygulama içindeki hiçbir finansal
kaydınız AdMob'a gönderilmez** — reklam şeridi uygulamanın içeriğini görmez.

Avrupa Ekonomik Alanı ve Birleşik Krallık kullanıcılarına, reklam gösterilmeden önce bir
rıza ekranı sunulur; rıza verilmezse kişiselleştirilmiş reklam gösterilmez. Rıza
tercihinizi daha sonra uygulama üzerinden değiştirebilirsiniz.

Reklamları tamamen kaldırmak isterseniz uygulama içinden **Money Agenda Pro** satın
alabilirsiniz (aylık, 6 aylık, yıllık abonelik veya tek seferlik ömür boyu paket). Pro'da
reklam isteği hiç yapılmaz. Satın alma işlemi Google Play üzerinden yürütülür; ödeme
bilgileriniz uygulamaya iletilmez, uygulama yalnızca hakkın olup olmadığını öğrenir.

## İzinler

- **Bildirimler:** ödeme günü hatırlatmaları için
- **Tam zamanlı alarm:** hatırlatmanın doğru saatte çıkması için
- **İnternet:** yalnızca bulut yedeği ve döviz kuru bilgisi için

Uygulama SMS okuma izni istemez ve bankacılık uygulamalarınıza bağlanmaz.

## Saklama ve silme

Bulut yedeğiniz, siz silene kadar saklanır. Silme iki yolla yapılabilir:

- Uygulama içinde: **Ayarlar → Hesap ve bulut yedeği → Hesabımı sil**
- [Hesap silme sayfası](/hesap-silme/) üzerinden talep

Hesap silindiğinde buluttaki kayıtlarınız kaldırılır; telefonunuzdaki yerel kayıtlarınız
durmaya devam eder.

## Çocukların gizliliği

Uygulama 13 yaş altındaki kullanıcılara yönelik değildir ve bilerek bu yaş grubundan veri
toplamaz.

## İletişim

Sorularınız için: [yzcdev@gmail.com](mailto:yzcdev@gmail.com)
''')

PAGES['kosullar'] = ('''---
title: Kullanım Koşulları
seoTitle: Kullanım Koşulları
description: "Money Agenda kullanım koşulları: hizmetin kapsamı, verilerin doğruluğu, hatırlatmaların sınırı, Pro ücretlendirmesi ve iade."
lang: tr
path: /kosullar/
route: terms
lead: Money Agenda uygulamasını kullanarak aşağıdaki koşulları kabul etmiş olursunuz.
updated: "Son güncelleme: 15 Eylül 2026"
---

> **Money Agenda yatırım tavsiyesi vermez.** Uygulamadaki tüm hesaplar, tahminler ve
> raporlar yalnızca bilgilendirme amaçlıdır ve girdiğiniz verilere dayanır. Finansal
> kararlarınızın sorumluluğu size aittir.

## Hizmetin kapsamı

Uygulama; girdiğiniz gelir, gider, kart, taksit, kredi ve abonelik bilgilerini takvimler
ve kurallar yardımıyla düzenler, ödeme günlerinizi hatırlatır. Uygulama bankanıza
bağlanmaz, işlemlerinizi otomatik olarak okumaz ve sizin adınıza ödeme yapmaz.

## Verilerin doğruluğu

Hesaplamalar girdiğiniz verilere dayanır. Yanlış ya da eksik girilen tutar, tarih veya
oran, sonuçların da yanlış olmasına yol açar. Girdiğiniz bilgilerin doğruluğundan siz
sorumlusunuz. Özellikle kredi taksiti, vade farkı ve ekstre hesaplarında **bankanızın
bildirdiği tutarı esas alın**.

## Hatırlatmalar

Hatırlatmalar cihazınızın alarm ve bildirim sistemine dayanır. İşletim sisteminin pil
tasarrufu ayarları, bildirimlerin kapatılması veya cihazın kapalı olması hatırlatmaların
gecikmesine ya da hiç görünmemesine yol açabilir. Uygulama, bir ödemenin zamanında
yapılacağını garanti etmez.

## Ücretlendirme

**Uygulamanın tüm takip özellikleri ücretsizdir**; hiçbir işlev ödemeye kilitli değildir.
Ücretsiz sürümde ekranın altında bir reklam şeridi gösterilir.

**Money Agenda Pro**, bu reklam şeridini kaldırır. Aylık, 6 aylık ve yıllık abonelik ile
tek seferlik ömür boyu paket seçenekleri vardır. Güncel fiyatlar uygulama içindeki satın
alma ekranında, Google Play'in size gösterdiği para birimi ve vergiyle görünür.

**Abonelikler siz iptal etmedikçe her dönem sonunda kendiliğinden yenilenir.** İptal,
Google Play hesabınızın abonelikler bölümünden yapılır; uygulama içindeki "Aboneliği
yönet" bağlantısı sizi doğrudan oraya götürür. İptal, içinde bulunduğunuz dönemin sonunda
geçerli olur — kalan süreyi kullanmaya devam edersiniz.

Ödeme ve iade işlemleri Google Play üzerinden yürütülür; ödeme bilgileriniz uygulamaya
iletilmez. İade talepleri Google Play'in iade politikasına tabidir ve Google Play
üzerinden yapılır.

Ömür boyu paket tek seferlik bir satın almadır ve uygulamanın yayında kaldığı süre
boyunca geçerlidir; abonelik değildir, yenilenmez.

## Sorumluluğun sınırı

Hizmet "olduğu gibi" sunulur. Uygulamanın kesintisiz veya hatasız çalışacağı garanti
edilmez. Kullanımdan doğabilecek doğrudan veya dolaylı zararlardan geliştirici sorumlu
tutulamaz. Yedeklerinizi düzenli almanız önerilir.

## Yedekler

Uygulama içinden aldığınız parolalı yedek dosyasının parolası yalnızca sizde durur.
**Parolanızı kaybederseniz yedek dosyası açılamaz ve içeriği kurtarılamaz.**

## Değişiklikler

Bu koşullar güncellenebilir. Güncel sürüm her zaman bu sayfada yayımlanır.

## İletişim

[yzcdev@gmail.com](mailto:yzcdev@gmail.com)
''')

PAGES['hesap-silme'] = ('''---
title: Hesap ve veri silme
seoTitle: Hesap ve veri silme talebi
description: Money Agenda hesabınızı ve buluttaki verilerinizi uygulama içinden anında ya da e-posta ile silebilirsiniz.
lang: tr
path: /hesap-silme/
route: deleteAccount
lead: Money Agenda hesabınızı ve buluttaki verilerinizi istediğiniz zaman silebilirsiniz.
---

## Uygulama içinden (en hızlı yol)

1. Money Agenda uygulamasını açın
2. **Ayarlar → Hesap ve bulut yedeği** bölümüne girin
3. **Hesabımı sil** seçeneğine dokunun ve onaylayın

İşlem anında gerçekleşir; ayrıca bir talep göndermenize gerek yoktur.

## E-posta ile talep

Uygulamaya erişemiyorsanız, **hesabınıza ait Google e-posta adresinden**
[yzcdev@gmail.com](mailto:yzcdev@gmail.com) adresine "Hesap silme talebi" konulu bir
e-posta gönderin. Talepler en geç 30 gün içinde, genellikle birkaç iş günü içinde
karşılanır. Doğrulama için talebin hesabın kendi e-posta adresinden gelmesi gerekir.

## Neyin silindiği

| Silinir | Silinmez |
|---|---|
| Google hesabı bağlantınız | Telefonunuzdaki yerel kayıtlar |
| Bulutta saklanan tüm kayıtlarınız: işlemler, hesaplar, kartlar, taksitler, krediler, abonelikler, bütçeler | Bunlar cihazınızda kalmaya devam eder |

Yerel kayıtları da tamamen kaldırmak için uygulamayı telefonunuzdan silin.

## Saklama süresi

Silme işleminden sonra buluttaki verileriniz **kalıcı olarak kaldırılır ve geri
getirilemez**. Silmeden önce uygulama içinden yedek almanız önerilir
(**Ayarlar → Yedekleme**).
''')

PAGES['ozellikler'] = ('''---
title: Özellikler
seoTitle: Özellikler — neleri takip eder
description: Kredi kartı kesim ve son ödeme, taksit, kredi, abonelik ve alan adı yenilemeleri, bütçe, rapor ve hatırlatmalar. Money Agenda neyi nasıl takip eder.
lang: tr
path: /ozellikler/
route: features
lead: Money Agenda beş şeyi aynı takvimde toplar: kart, kredi, yenileme, bütçe ve hatırlatma. Her biri ayrı bir uygulamanın işi olabilirdi; burada hepsi tek listede birleşiyor.
---

Uygulamanın ana ekranı geçmişi değil **sırada olanı** gösterir. Bu sayfada her alanın ne
yaptığını bulabilirsiniz.

## [Kredi kartı takibi](/ozellikler/kredi-karti-takibi/)

Kesim ve son ödeme tarihleri, ekstre dönemleri, asgari ödeme, güncel borç ve kalan limit.
Her kartın kendi kesim günü ve kendi ödeme aralığı vardır; uygulama bunu kart bazında
tutar.

## [Taksit ve kredi](/ozellikler/taksit-ve-kredi/)

Taksitli alışverişlerin kalan planı, kredi amortisman tablosu ve **BSMV ile KKDF dahil
efektif maliyet**. Bankanın söylediği aylık oran ile gerçekte ödediğiniz yıllık maliyet
aynı şey değildir; uygulama ikisini de gösterir.

## [Abonelik ve yenileme](/ozellikler/abonelik-ve-yenileme/)

Abonelik, alan adı, hosting, SSL, sigorta — yenilenen ne varsa tarihiyle birlikte. Bu
kategori çoğu finans uygulamasında yoktur; oysa sessizce yenilenen bir alan adı da bir
ödemedir.

## [Bütçe ve rapor](/ozellikler/butce-ve-rapor/)

Kategori bütçeleri, hedefler, aylık raporlar ve ay sonu tahmini. Dışa aktarma CSV, XLSX
ve PDF olarak yapılır — veriniz uygulamada hapis değildir.

## [Bildirimler](/ozellikler/bildirimler/)

Vade öncesi ve sonrası uyarılar, sessiz saatler, günlük özet. Hatırlatma **kesin alarmla**
kurulur; cihaz uyku moduna girse de yeniden başlatılsa da plan korunur.

## Güvenlik ve gizlilik

- Parolalı, şifreli yerel yedek; parola yalnızca sizde durur
- PIN ve parmak izi kilidi
- Tutarları gizleme (omuz üstünden bakışa karşı)
- Giriş yapmadan tam çalışma — bulut tamamen isteğe bağlı

Ayrıntı için [gizlilik politikası](/gizlilik/).

## Tablet ve dil

Arayüz tablette yan gezinme rayına geçer ve içerik okunabilir bir genişlikte kalır.
Uygulama uçtan uca Türkçe ve İngilizce çalışır; tarih biçimleri, varsayılan kategoriler
ve dışa aktarma başlıkları dahil.
''')

PAGES['ozellikler-kredi-karti'] = ('''---
title: Kredi kartı takibi
seoTitle: Kredi kartı kesim ve son ödeme takibi
description: Kesim günü, son ödeme tarihi, ekstre dönemi, asgari ödeme ve kalan limit. Her kartın kendi kurallarıyla hesaplanır.
lang: tr
path: /ozellikler/kredi-karti-takibi/
route: featuresCards
lead: Kredi kartında asıl soru "ne kadar harcadım" değil, "ne zaman kesiliyor ve ne zaman ödemem gerekiyor". Uygulama bu iki tarihi kartın kendi kurallarıyla hesaplar.
---

## Kesim günü ve son ödeme

Her karta kendi **kesim günü** ve kesimden son ödemeye kaç gün olduğu girilir. Bankalar bu
aralığı farklı tutar; tek bir varsayılan bütün kartlara uymaz.

Uygulama bu ikisinden ekstre dönemini üretir ve ana ekranda "son ödemeye kaç gün kaldı"
bilgisini gösterir.

## Ay sonu kaydırması

Kesim günü ayın 31'i olan bir kartta şubat ne olacak? Uygulama **o ayda bulunmayan günleri
ayın son gününe kaydırır**. Bu, elle takip edenlerin en sık kaçırdığı ayrıntıdır: 31
Ocak'ta kesilen kart 28 Şubat'ta kesilir, 3 Mart'ta değil.

## Hangi harcama hangi ekstreye düşer

Kesim gününde yapılan bir harcama, o gün kapanan ekstreye mi yoksa bir sonrakine mi
girer? Uygulama ekstre dönemini açık aralık olarak tutar ve harcamayı doğru döneme
yerleştirir. Ana ekranda "bu dönem harcamaları" bu mantıkla toplanır.

## Asgari ödeme ve güncel borç

Kart detayında güncel borç, asgari ödeme, ödenen tutar ve limit doluluk oranı birlikte
görünür. Asgari ödemeyi ödemek borcu kapatmaz — kalan bakiyeye faiz işler. Uygulama
asgariyi bir hedef değil, bir alt sınır olarak gösterir.

## Birden fazla kart

Kartlar ayrı ayrı tutulur; her birinin kendi kesim günü, ödeme aralığı ve limiti vardır.
Ana ekrandaki "kart borcu" toplamı hepsini birleştirir, kart detayı tek tek gösterir.

---

İlgili: [taksit ve kredi](/ozellikler/taksit-ve-kredi/) · [bildirimler](/ozellikler/bildirimler/)
''')

PAGES['ozellikler-taksit-kredi'] = ('''---
title: Taksit ve kredi
seoTitle: Taksit planı ve kredi maliyeti takibi
description: Taksitli alışverişlerin kalan planı, kredi amortismanı ve BSMV/KKDF dahil efektif maliyet. Aylık oran ile gerçek yıllık maliyet aynı şey değildir.
lang: tr
path: /ozellikler/taksit-ve-kredi/
route: featuresLoans
lead: Bir kredinin "aylık %2,9 faizli" olması, yılda %34,8 ödeyeceğiniz anlamına gelmez — daha fazlasını ödersiniz. Uygulama ikisini de hesaplar ve farkı gösterir.
---

## Taksitli alışveriş

Taksitli bir alışveriş girdiğinizde uygulama kalan taksitleri, her birinin hangi ay
düşeceğini ve toplam vade farkını tutar. Ana ekranda "bu ay ödenecek taksit" bütün
kartlardaki taksitlerin toplamıdır.

"Faizsiz taksit" çoğu zaman gerçekten faizsizdir ama **peşin fiyatı daha düşükse** aradaki
fark gizli bir maliyettir. Uygulama peşin fiyatı da girmenize izin verir ve vade farkını
ayrıca gösterir.

## Kredi amortismanı

Kredi için anapara, faiz oranı ve vade girilir; uygulama aylık taksiti ve ödeme planını
üretir. Her taksitin ne kadarı anapara, ne kadarı faiz — tablo bunu ayrı ayrı gösterir.
Kredinin başında taksitin büyük kısmı faizdir; bu, erken kapatma kararını etkiler.

## BSMV ve KKDF

Türkiye'de tüketici kredilerinde faizin üzerine iki kesinti biner:

- **BSMV** — Banka ve Sigorta Muameleleri Vergisi
- **KKDF** — Kaynak Kullanımını Destekleme Fonu

Bunlar bankanın ilan ettiği faiz oranına dahil değildir ama **ödediğiniz paraya dahildir**.
Uygulama efektif maliyeti bu iki kesintiyi hesaba katarak gösterir. Genel bir bütçe
uygulamasının yaklaşık cevap verdiği yer tam olarak burasıdır.

## Neden bu fark önemli

Aynı anapara ve vade için iki bankanın ilan ettiği oran birbirine çok yakın olabilir ama
toplam geri ödeme farkı binlerce lira çıkabilir. Karşılaştırmayı aylık orana bakarak değil
**toplam geri ödemeye** bakarak yapmak gerekir; uygulama toplamı her zaman görünür tutar.

---

İlgili: [kredi kartı takibi](/ozellikler/kredi-karti-takibi/) · [bütçe ve rapor](/ozellikler/butce-ve-rapor/)
''')

PAGES['ozellikler-abonelik'] = ('''---
title: Abonelik ve yenileme
seoTitle: Abonelik, alan adı ve hosting yenileme takibi
description: Abonelik, alan adı, hosting, SSL, sigorta — yenilenen ne varsa tarihiyle birlikte tek listede. Yenilemeden önce hatırlatır.
lang: tr
path: /ozellikler/abonelik-ve-yenileme/
route: featuresRenewals
lead: Abonelikler bir kez kurulur, sonra kendiliğinden yenilenir. Sorun da budur: ödeme her ay çıkar, karar ise yalnızca bir kez verilmiştir.
---

## Neler girilebilir

- **Abonelikler** — dijital servisler, spor salonu, dergi, bulut depolama
- **Alan adı** — yıllık ya da çok yıllık yenilemeler
- **Hosting ve sunucu** — aylık veya yıllık
- **SSL ve lisanslar**
- **Sigorta** — kasko, trafik, DASK, sağlık
- **Fatura benzeri düzenli ödemeler** — tutarı değişkense "değişken (fatura)" seçilir

Alan adı ve hosting kategorisi çoğu kişisel finans uygulamasında hiç yoktur. Oysa
sessizce düşen bir alan adı, kaçırılan bir kredi kartı ödemesinden daha pahalıya mal
olabilir.

## Sabit ve değişken tutar

Netflix gibi tutarı belli olanlar **sabit**; elektrik faturası gibi her ay değişenler
**değişken** olarak girilir. Değişkenlerde uygulama tutarı tahmin etmez — geçmiş
ödemeleri gösterir, rakamı siz girersiniz. Uydurulmuş bir tahmin, bütçeyi yanlış
hizalamaktan başka işe yaramaz.

## Yenileme tarihi ve sıklık

Aylık, 3 aylık, 6 aylık, yıllık ve 2 yıllık sıklıklar desteklenir. Sıradaki yenileme
tarihi hazır seçeneklerden ("1 ay sonra", "1 yıl sonra") ya da **takvimden** seçilir —
aboneliği uygulamaya eklerken değil, daha önce başlatmış olabilirsiniz.

## Hatırlatma

Her yenileme için kaç gün önceden haber verileceği ayarlanır (varsayılan: 3 gün ve 1 gün
kala). İptal etmeyi düşündüğünüz bir abonelikte bu, kararı verecek zamanı bırakır.

Vadesi gelen abonelik otomatik olarak işleme dönüşür ve bir sonraki tarih ilerler; elle
tekrar girmeniz gerekmez.

---

İlgili: [bildirimler](/ozellikler/bildirimler/) · [bütçe ve rapor](/ozellikler/butce-ve-rapor/)
''')

PAGES['ozellikler-butce-rapor'] = ('''---
title: Bütçe ve rapor
seoTitle: Bütçe, hedef ve rapor
description: Kategori bütçeleri, hedefler, aylık raporlar, ay sonu tahmini ve CSV / XLSX / PDF dışa aktarma.
lang: tr
path: /ozellikler/butce-ve-rapor/
route: featuresBudget
lead: Bütçe, harcamayı yasaklamak için değil; ay bitmeden nerede durduğunuzu görmek için vardır.
---

## Kategori bütçeleri

Kategori başına aylık bütçe konur. Uygulama harcamayı bütçeye oranlar ve eşiğe
yaklaştığınızda haber verir. Eşik aşıldığında uyarı gelir — ay sonunda değil, aşıldığı
gün.

## Ay sonu tahmini

Ana ekrandaki tahmin, bugüne kadarki harcamaya ve kalan gün sayısına bakar:

> kalan günler × son üç ayın günlük ortalama değişken harcaması

Formül ekranda açıkça yazar. Yapay zekâ yoktur; sayı nereden geldiğini söyleyemiyorsa
güvenilmez.

## Hedefler

Belirli bir tutara belirli bir tarihe kadar ulaşmak için hedef konur. Uygulama aylık ne
kadar ayırmanız gerektiğini gösterir ve ilerlemeyi takip eder.

## Raporlar

- Gelir, gider ve net akış
- Kategori dağılımı
- Son 12 ayın seyri
- Hesap ve kart bazında kırılım

## Dışa aktarma

Rapor ve işlem listeleri **CSV**, **XLSX** ve **PDF** olarak dışa aktarılır. Veriniz
uygulamada hapis değildir; istediğiniz an tablonuza alabilirsiniz. Dışa aktarma
başlıkları uygulamanın diline göre üretilir.

## Döviz

Döviz cinsinden tutarlar TCMB kuruyla gösterilir. Kur günde bir kez tazelenir; internet
yoksa elde bulunan son kur kullanılır ve bunun tarihi görünür.

## Güvenlik

Parolalı ve şifreli yerel yedek alınabilir. **Parola yalnızca sizde durur** — kaybolursa
yedek açılamaz. Uygulamaya PIN veya parmak izi kilidi konabilir; tutarlar tek dokunuşla
gizlenebilir.

---

İlgili: [gizlilik politikası](/gizlilik/) · [özellikler](/ozellikler/)
''')

PAGES['ozellikler-bildirimler'] = ('''---
title: Bildirimler
seoTitle: Ödeme hatırlatmaları nasıl çalışır
description: Vade öncesi ve sonrası uyarılar, sessiz saatler, günlük özet. Kesin alarmla kurulur; yeniden başlatmada plan korunur.
lang: tr
path: /ozellikler/bildirimler/
route: featuresAlerts
lead: Bir hatırlatıcı sessizce çalışmıyorsa, hiç olmamasından kötüdür — çünkü ona güvenirsiniz. Bu yüzden bildirim tarafı uygulamanın en çok uğraşılan parçası.
---

## Ne zaman haber verir

Her yükümlülük türü için kaç gün önceden uyarılacağı ayrı ayarlanır. Varsayılanlar
türüne göre değişir; abonelikte 3 ve 1 gün kala, kredi kartında kesim ve son ödeme
günlerine göre.

**Vadeden sonra da uyarır.** Ödemeyi kaçırdıysanız ertesi gün bir gecikme bildirimi
gelir — yalnızca parası gecikebilen türlerde (kart, taksit, kredi, fatura, borç). Ürünün
önlemek için var olduğu şey tam olarak budur.

## Sessiz saatler ve günlük özet

Gece bildirim istemiyorsanız sessiz saat aralığı konur; o aralığa düşen hatırlatma
aralığın sonuna kayar. Ayrıca günde bir kez, seçtiğiniz saatte "bugün ne var" özeti
gönderilebilir.

## Teknik tarafı: neden zamanında geliyor

Hatırlatmalar **kesin alarm** (`setExactAndAllowWhileIdle`) ile kurulur; cihaz uyku
moduna girse bile alarm zamanında çalışır. Yalnızca önümüzdeki 48 saate düşen
hatırlatmalar için gerçek alarm kurulur, gerisini günlük bir iş pencereye girdikçe ekler
— böylece aynı anda kurulu alarm sayısı sistem sınırlarının çok altında kalır.

Telefon yeniden başlatıldığında, uygulama güncellendiğinde veya saat/saat dilimi
değiştiğinde plan **otomatik olarak yeniden kurulur**. Uygulamayı açmanız gerekmez.

## Üreticinin pil yöneticisi

Bazı üreticilerin pil yönetimi, uygulamaları arka planda kısıtlayarak bildirimleri
geciktirebilir ya da tamamen engelleyebilir. Bu, hatırlatıcı uygulamaların en zayıf
noktasıdır ve tek bir ayarla çözülmez.

Uygulama iki şey yapar:

1. **Cihaz markanıza göre adım adım rehber** — hangi ayarın nerede olduğunu gösterir
2. **Test bildirimi düğmesi** — kendi cihazınızda çalıştığını görürsünüz

Ayrıca son yedi günde tetiklenmemiş hatırlatma varsa uygulama bunu fark eder ve rehberi
önerir; sessizce başarısız olmaktansa durumu söylemek doğrudur.

---

İlgili: [abonelik ve yenileme](/ozellikler/abonelik-ve-yenileme/) · [destek](/destek/)
''')

PAGES['neden'] = ('''---
title: Neden Money Agenda
seoTitle: Neden Money Agenda — gelir gider uygulamalarından farkı
description: Geçmişi değil sırada olanı gösterir, Türk bankacılık takvimini bilir, veriler telefonda kalır ve hiçbir özellik ödemeye kilitli değildir.
lang: tr
path: /neden-money-agenda/
route: why
lead: Gelir gider uygulamalarının çoğu size ne harcadığınızı anlatır. Sorun genelde bu değildir.
---

Sorun, kartın kesim gününü kaçırıp bir sonraki ekstreye sarkmak. Taksitin hangi ay
biteceğini bilmemek. Alan adının sessizce düşmesi. Bunların hiçbiri "geçen ay ne kadar
kahve içtim" sorusuyla çözülmez.

## Dört ayrım noktası

### 1. Ana ekran ileriye bakar

Yükümlülük takvimi ürünün merkezinde. Bugün ve önümüzdeki günlerde ödenecek ne varsa
üstte durur. Geçmiş aya ait grafikler var ama ana ekranda değil — orası için
[raporlar](/ozellikler/butce-ve-rapor/) sayfası var.

### 2. Türk bankacılık takvimini bilir

Kesim günü, son ödeme, ekstre dönemi, asgari ödeme, BSMV ve KKDF. Bunlar uluslararası bir
bütçe uygulamasında ya hiç yoktur ya da yaklaşık hesaplanır. Burada hepsi birim testli
kurallarla hesaplanıyor.

Ayın 29-31'i gibi her ayda bulunmayan günler doğru kaydırılıyor; tutarlar kuruş
hassasiyetinde tutuluyor, ondalık yuvarlama hatası olmuyor.

### 3. Yenilenen dijital varlıklar

Alan adı, hosting, SSL, lisans. Bir siteniz varsa bunlar gerçek ödemelerdir ve
kaçırıldığında geri dönüşü pahalıdır. Bu kategoriyi başka bir yerde bulmak zor.

### 4. Veriniz telefonda, özellik kilitlenmiyor

Uygulama **giriş yapmadan tam olarak çalışır**. Bulut yedeği isteğe bağlı. Banka
bağlantısı yok, SMS izni istenmiyor, yapay zekâ kullanılmıyor.

Ücretsiz sürümde alt tarafta bir reklam şeridi var ve Pro bunu kaldırıyor — ama **hiçbir
özellik ödemenin arkasında değil**. Ödeme yapmayan kullanıcı da bütün işlevi kullanır.
Ayrım "reklamsızlık" değil, ödeme yapmayanın hiçbir şey kaybetmemesi.

## Neyi yapmıyoruz

Bunları bilerek yapmıyoruz; eksik değil, karar:

- **Bankaya bağlanmıyoruz.** Açık bankacılık entegrasyonu yok. Kayıtları siz
  giriyorsunuz; karşılığında hiçbir banka kimlik bilgisi paylaşmıyorsunuz.
- **SMS okumuyoruz.** İzin bile istenmiyor.
- **Yapay zekâ kullanmıyoruz.** Her hesap deterministik ve formülü ekranda yazıyor.
- **Yatırım tavsiyesi vermiyoruz.**

## Bir uygulama seçerken nelere bakmalı

Hangi uygulamayı seçerseniz seçin, şunları sorun:

1. Ana ekran geçmişi mi gösteriyor, sırada olanı mı?
2. Kredi kartı kesim günü ile son ödeme arasındaki farkı kart bazında ayarlayabiliyor musunuz?
3. Verileriniz nereye gidiyor ve giriş yapmadan çalışıyor mu?
4. Verinizi dışa aktarabiliyor musunuz?
5. Hatırlatma cihazınızda gerçekten çalışıyor mu — test edebiliyor musunuz?

---

[Google Play'den ücretsiz indirin](https://play.google.com/store/apps/details?id=com.moneyagenda.app)
''')

PAGES['destek'] = ('''---
title: Destek
seoTitle: Destek ve sık sorulanlar
description: Money Agenda ile ilgili sık sorulan sorular, bildirim sorunlarının çözümü ve iletişim.
lang: tr
path: /destek/
route: support
lead: Aradığınızı bulamazsanız yazın; e-postalara genellikle birkaç iş günü içinde dönülür.
---

## Bildirimler gelmiyor

En sık karşılaşılan sorun bu ve nedeni genellikle uygulamada değil, telefonun pil
yönetiminde.

1. Uygulama içinde **Ayarlar → Hatırlatma ayarları → Test bildirimi gönder**'e dokunun.
   Bildirim geliyorsa kanal ve izin tarafı sorunsuz demektir.
2. Aynı ekranda **"Bildirimler gelmiyor"** bağlantısı, cihaz markanıza göre adım adım ne
   yapmanız gerektiğini gösterir.
3. Telefonun ayarlarından Money Agenda için **pil optimizasyonunu kapatın**.
4. Android 12 ve üstünde **tam zamanlı alarm** izninin açık olduğundan emin olun.

## Verilerimi başka telefona nasıl taşırım

İki yol var:

- **Yedek dosyası:** Ayarlar → Yedekleme → parolalı yedek oluşturun, dosyayı yeni
  telefona taşıyın, oradan geri yükleyin. Parola yalnızca sizde durur; kaybolursa dosya
  açılamaz.
- **Bulut yedeği:** Google ile giriş yaparsanız kayıtlarınız hesabınıza bağlı olarak
  saklanır ve yeni cihazda aynı hesapla girdiğinizde gelir.

## Pro satın aldım ama reklamlar duruyor

Ayarlar → Pro ekranında **"Satın alımlarımı geri yükle"** seçeneğini kullanın. Play'e
geçici olarak ulaşılamadığında hak düşmez; bağlantı gelince kendiliğinden geri gelir.

Aboneliği iptal etmek isterseniz Google Play hesabınızın abonelikler bölümünden
yapabilirsiniz; uygulama içindeki "Aboneliği yönet" bağlantısı sizi oraya götürür.

## Uygulama hangi Android sürümlerinde çalışır

Android 8.0 (API 26) ve üstü. Tablet düzeni desteklenir.

## iPhone sürümü var mı

Şu an yok.

## Verilerim nereye gidiyor

Telefonunuzda kalıyor. Ayrıntı için [gizlilik politikası](/gizlilik/).

## İletişim

[yzcdev@gmail.com](mailto:yzcdev@gmail.com)

Hata bildirirken cihaz modelinizi, Android sürümünüzü ve uygulama sürümünü (Ayarlar →
Sürüm) yazarsanız çözüm hızlanır.
''')

PAGES['basin-kiti'] = ('''---
title: Basın kiti
seoTitle: Basın kiti — logo, ekran görüntüleri ve künye
description: Money Agenda hakkında yazacaklar için logo, ekran görüntüleri, kısa tanıtım metinleri ve künye bilgileri.
lang: tr
path: /basin-kiti/
route: press
lead: Money Agenda hakkında yazıyorsanız buradaki metin ve görselleri izin istemeden kullanabilirsiniz.
---

## Tek cümlelik tanım

> Money Agenda, kredi kartı kesim ve son ödeme tarihlerinden abonelik ve alan adı
> yenilemelerine kadar bütün ödeme yükümlülüklerini tek takvimde toplayan, Türkiye'ye
> özgü bir Android uygulamasıdır.

## Kısa tanıtım (50 kelime)

Money Agenda geçmişi değil, sırada olanı gösterir. Kredi kartı kesim ve son ödeme,
taksit, kredi, abonelik ve alan adı yenilemeleri tek takvimde toplanır; vakti gelmeden
hatırlatılır. Tüm özellikler ücretsizdir, uygulama giriş yapmadan çalışır ve veriler
telefonda kalır.

## Künye

| | |
|---|---|
| Ad | Money Agenda |
| Paket | `com.moneyagenda.app` |
| Platform | Android 8.0 ve üstü |
| Kategori | Finans |
| Diller | Türkçe, İngilizce |
| Fiyat | Ücretsiz; Pro reklamları kaldırır |
| Yayın | 15 Eylül 2026 |
| İletişim | [yzcdev@gmail.com](mailto:yzcdev@gmail.com) |

## Görseller

- [Uygulama ikonu (512×512)](/brand/icon-512.png)
- [Paylaşım görseli (1200×630)](/og/default.png)

Ekran görüntüleri: [Bugün](/screens/01-bugun-840.webp) ·
[Kart detayı](/screens/05-kart-detay-840.webp) ·
[Taksitler](/screens/08-taksitler-840.webp) ·
[Raporlar](/screens/02-raporlar-840.webp)

## Doğru bilgiler

Yazarken şunlara dikkat edilmesi rica olunur:

- Uygulama **yapay zekâ kullanmaz**; tüm hesaplar deterministik kurallardır.
- **Bankaya bağlanmaz**, SMS okumaz. Kayıtları kullanıcı girer.
- Ücretsiz sürümde reklam vardır; **hiçbir özellik ödemeye kilitli değildir**.
- Yatırım tavsiyesi vermez.
''')

PAGES['araclar'] = ('''---
title: Araçlar
seoTitle: Ücretsiz hesaplama araçları
description: Kredi kartı son ödeme tarihi, asgari ödeme, kredi maliyeti ve taksit planı hesaplayıcıları. Uygulamanın kendi motoruyla aynı sonucu verir.
lang: tr
path: /araclar/
route: tools
lead: Uygulamanın içindeki hesaplamaların aynısı, kurulum gerektirmeden tarayıcıda. Kayıt yok, veri sunucuya gitmiyor.
---

Bu araçlar Money Agenda'nın domain katmanındaki hesaplamalardan türetildi ve aynı test
vektörleriyle doğrulanıyor. Yani buradaki sonuç ile uygulamadaki sonuç birbirinden
ayrışamaz.

> **Hazırlanıyor.** Araçlar sırayla yayına alınıyor. Aşağıdaki listede ne geleceğini
> görebilirsiniz; hepsi çıkana kadar hesaplamaların tamamı zaten uygulamanın içinde.

## Sırada

- **Son ödeme tarihi hesaplayıcı** — kesim gününden son ödeme tarihini bulur, ay sonu
  kaydırmasını doğru yapar
- **Asgari ödeme simülatörü** — yalnızca asgariyi ödemeye devam ederseniz borcun ne kadar
  sürede biteceğini ve toplam faizi gösterir
- **Kredi maliyeti hesaplayıcı** — BSMV ve KKDF dahil, toplam geri ödeme ve efektif oran
- **Taksit planı hesaplayıcı** — taksit tutarı, vade farkı ve aylık dağılım
- **Abonelik maliyeti hesaplayıcı** — farklı sıklıklardaki aboneliklerin yıllık toplamı

## Bu arada

Hepsi [uygulamanın içinde](https://play.google.com/store/apps/details?id=com.moneyagenda.app)
zaten var; üstelik kendi kartlarınız ve kendi kredinizle.

[Kredi kartı takibi](/ozellikler/kredi-karti-takibi/) ·
[Taksit ve kredi](/ozellikler/taksit-ve-kredi/)
''')

os.makedirs(OUT, exist_ok=True)
for name, body in PAGES.items():
    with io.open(os.path.join(OUT, name + '.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)
print(str(len(PAGES)) + ' sayfa yazildi')
