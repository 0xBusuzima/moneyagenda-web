---
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
- **Uygulamada davranış analitiği yok.** Hangi ekranı ne kadar kullandığınız, neye
  dokunduğunuz, uygulamayı ne sıklıkla açtığınız ölçülmüyor. Yalnızca çökme raporlama
  var; aşağıda ayrıca açıklanıyor. (Bu web sitesi için durum en altta anlatılıyor.)
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

## Çökme raporlama

Uygulama beklenmedik şekilde kapanırsa, hatayı bulup düzeltebilmek için **Firebase
Crashlytics** (Google) bir çökme raporu gönderir. Rapor şunları içerir:

- Hatanın kod içinde nerede oluştuğu (yığın izi) ve uygulama sürümü
- Cihaz modeli, Android sürümü, kullanılabilir bellek ve depolama
- Çökmenin zamanı ve uygulamanın o an ne kadar süredir açık olduğu
- Cihazınıza özel, kurulumla birlikte üretilen rastgele bir kurulum kimliği

**Finansal kayıtlarınız çökme raporuna girmez.** Tutarlar, kart adları, kişi adları,
kategoriler ve bütçeler rapora yazılmaz. Bunu kazara bozmamak için kodda otomatik bir
denetim çalışıyor: doğrulama ve hata mesajlarında tutar geçiyorsa derleme başarısız olur.

Uygulama Crashlytics'e **kendi kayıtlarını, hesap bilgilerinizi ya da hangi ekranları
gezdiğinizi göndermez** — yalnızca çökmenin kendisi gider. Çökme raporları yalnızca
mağazadan kurulan sürümden gönderilir.

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

## Bu web sitesi

Yukarıdakiler **uygulama** içindir. `moneyagenda.com.tr` sitesinde kaç kişinin hangi
sayfayı gördüğünü ölçmek için **Cloudflare Web Analytics** kullanılıyor.

- **Çerez koymaz** ve tarayıcınızda hiçbir şey saklamaz; bu yüzden sitede çerez onayı
  penceresi yoktur
- **Parmak izi çıkarmaz**, sizi siteler arasında takip etmez
- Toplanan şey sayfa adresi, yönlendiren adres, ülke, tarayıcı ve cihaz türü gibi
  toplulaştırılmış bilgidir — kişiyi tanımlamaz

**Sitedeki hesaplayıcılar tarayıcınızda çalışır.** Girdiğiniz tutarlar, oranlar ve
tarihler hiçbir sunucuya gönderilmez; ölçüm de bunları görmez.

Uygulama ile site arasında veri alışverişi yoktur: uygulamadaki kayıtlarınız siteye,
sitedeki ölçüm de uygulamaya geçmez.

## İletişim

Sorularınız için: [yzcdev@gmail.com](mailto:yzcdev@gmail.com)
