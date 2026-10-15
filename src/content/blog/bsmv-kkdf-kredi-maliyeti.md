---
title: BSMV ve KKDF nedir, kredi maliyetini ne kadar değiştirir
seoTitle: BSMV ve KKDF nedir, kredinin gerçek maliyeti nasıl hesaplanır
description: Bankanın ilan ettiği faiz ödediğinizin tamamı değil. Tüketici kredisinde faize BSMV ve KKDF biner, aylık oran 1,30 ile çarpılır — %2,89 gerçekte %3,757.
lang: tr
slug: bsmv-kkdf-kredi-maliyeti
published: 2026-09-25
updated: 2026-10-16
related:
  - label: Kredi maliyeti hesaplama
    href: /araclar/kredi-maliyeti-hesaplama/
  - label: Aylık faiz ile yıllık maliyet farkı
    href: /blog/aylik-faiz-yillik-maliyet-farki/
  - label: Taksit ve kredi takibi
    href: /ozellikler/taksit-ve-kredi/
---

Banka "aylık %2,89 faizli ihtiyaç kredisi" diye ilan eder. Hesap makinesine %2,89 yazıp
taksiti hesaplarsanız, çıkan rakam bankanın söylediğinden düşük olur. Aradaki fark iki
kesintiden gelir.

## Kısa cevap

**KKDF** ve **BSMV**, faizin üzerinden alınan iki kesintidir. Tüketici kredisinde ikisi
de %15 olduğunda ilan edilen aylık oran **1,30 ile çarpılır**: %2,89 ilan edilen oran,
gerçekte %3,757 olarak işler.

100.000 TL'lik bir kredide bu iki kesintinin size maliyeti vadeye göre **6.302 TL ile
41.391 TL** arasında değişiyor. Aşağıda vade vade tablosu var.

Kendi kredinizin hesabını
[kredi maliyeti hesaplayıcısında](/araclar/kredi-maliyeti-hesaplama/) vergileri açıp
kapatarak görebilirsiniz.

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

Aradaki fark küçük bir yüzde gibi görünüyor. 100.000 TL, 36 ay için ne demek olduğuna
bakalım:

| | Aylık taksit | Toplam geri ödeme |
|---|---|---|
| Vergisiz (%2,89) | 4.505,51 TL | 162.198,39 TL |
| **Vergili (%3,757)** | **5.112,11 TL** | **184.035,61 TL** |

**21.837,22 TL** fark. Vergileri hesaba katmayan bir hesaplama, krediyi gerçekte
olduğundan ucuz gösterir — bu örnekte anaparanın beşte biri kadar.

## Vade uzadıkça bedeli büyüyor

Kesintiler faizden alındığı için, faiz arttıkça kesinti de artıyor. Vade uzadıkça ödenen
toplam faiz büyüdüğünden vergilerin bedeli orantısız biçimde yükseliyor.

Aynı 100.000 TL kredi, ilan edilen %2,89 ile:

| Vade | Vergisiz toplam | Vergili toplam | Vergilerin bedeli | Anaparaya oranı |
|---|---|---|---|---|
| 12 ay | 119.764,26 TL | 126.066,31 TL | 6.302,05 TL | %6,3 |
| 24 ay | 140.039,86 TL | 153.516,74 TL | 13.476,88 TL | %13,5 |
| 36 ay | 162.198,39 TL | 184.035,61 TL | 21.837,22 TL | %21,8 |
| 48 ay | 186.135,20 TL | 217.345,36 TL | 31.210,16 TL | %31,2 |
| **60 ay** | 211.714,32 TL | **253.105,80 TL** | **41.391,48 TL** | **%41,4** |

12 ayda anaparanın %6,3'ü, 60 ayda **%41,4'ü**. Yani uzun vade seçmek sadece daha çok
faiz değil, daha çok vergi de demek. Vadeyi kısaltmanın tasarrufu iki koldan geliyor.

## Yıllık karşılığı

Vergili aylık %3,757 oranın bileşik yıllık karşılığı **%55,67** — bankanın vitrinindeki
%2,89 ile arasındaki mesafe budur. Aylık oranın yıllığa nasıl çevrildiği ve neden 12 ile
çarpmanın yanlış olduğu
[ayrı bir yazıda](/blog/aylik-faiz-yillik-maliyet-farki/) anlatılıyor.

## Nerede yok

Bu kesintiler her kredide yok:

- **Konut kredilerinde KKDF ve BSMV uygulanmaz.** Konut kredisinin ilan edilen oranı
  ödediğiniz orana çok daha yakındır.
- Ticari kredilerde durum farklıdır ve işletmenin vergi durumuna bağlıdır.

Yani ihtiyaç kredisi ile konut kredisinin ilan edilen oranlarını doğrudan karşılaştırmak
yanıltıcıdır — birinde üzerine %30 biniyor, diğerinde binmiyor. Aynı ilan edilen oranla
iki kredi, biri konut biri ihtiyaç ise, gerçekte tamamen farklı maliyette.

## Karşılaştırma yaparken

İki bankanın ilan ettiği oranlar birbirine çok yakın olabilir ama masraflar, sigorta
zorunluluğu ve vade farkları toplamı değiştirir. Doğru karşılaştırma ölçüsü aylık oran
değil, **toplam geri ödeme** tutarıdır.

Bankadan kredi teklifi alırken sorulacak tek soru şu: *"Bu kredide toplamda ne kadar geri
ödeyeceğim?"* Tek bir rakam, bütün oranları ve kesintileri içinde barındırır.

## Erken kapatma

Krediyi erken kapatırsanız kalan anaparaya düşen faiz ve o faizin vergileri de düşer —
yani erken kapatma bu kesintilerden de tasarruf ettirir. Yukarıdaki tablo bunun neden
böyle olduğunu gösteriyor: 60 aylık bir krediyi 36. ayda kapatmak, kalan 24 ayın hem
faizini hem o faizin %30'unu ortadan kaldırıyor.

Bankalar erken kapamada bir komisyon uygulayabilir; kalan vadeye göre tasarrufun
komisyondan büyük olup olmadığına bakmak gerekir.

## Takip tarafı

Kredinin kalan vadesini ve aylık yükünü görmek, erken kapatma kararını da kolaylaştırıyor.
[Taksit ve kredi takibi](/ozellikler/taksit-ve-kredi/) sayfasında, amortisman tablosunun
ve kalan anaparanın nasıl izlendiği anlatılıyor.
