---
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
