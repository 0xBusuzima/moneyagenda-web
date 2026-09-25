---
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
