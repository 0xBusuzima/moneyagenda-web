# -*- coding: utf-8 -*-
"""Sürüm notları (tr) ve İngilizce sayfa seti.

İngilizce sayfalar Türkçelerinden kısa: birincil pazar Türkiye ve blog yalnızca Türkçe
(docs/15 §10). Kısa olmaları eksik oldukları anlamına gelmiyor — her sayfa kendi başına
tam; yalnızca Türkçe sürümlerdeki uzun örnekler tekrarlanmıyor.

Özellik alt sayfalarının İngilizcesi yok; bu yüzden İngilizce özellik başlığı alt
sayfalara bağlanmıyor. Var olmayan sayfaya bağlanmaktansa hiç bağlanmamak doğru.
"""
import io
import os

TR = 'src/content/pages/tr'
EN = 'src/content/pages/en'
FILES = {}

FILES[(TR, 'surum-notlari')] = '''---
title: Sürüm notları
seoTitle: Sürüm notları — neler değişti
description: Money Agenda'nın yayınlanan sürümleri ve her birinde neyin değiştiği.
lang: tr
path: /surum-notlari/
route: releases
lead: Üretime çıkan her sürüm ve içinde ne olduğu. Sürüm notlarında yazan her madde koddan doğrulanmıştır.
---

## 1.2.1 — 24 Eylül 2026

**Hatırlatmalar artık kendini toparlıyor.**

- Bazı cihazlarda günlük hatırlatma tazelemesi sessizce durabiliyordu; uygulama bunu
  açılışta fark edip yeniden kuruyor
- Çalan her hatırlatma bir sonrakilerin alarmını da kuruyor, böylece zincir tek bir arka
  plan işine bağlı kalmıyor
- Yeniden başlatma, cihaz uyku modu ve uçak modu senaryoları gerçek cihazda doğrulandı

## 1.2.0 — 17 Eylül 2026

**Tablet düzeni, tam İngilizce desteği ve tarih seçici.**

- Tablette navigasyon yana alındı; içerik okunabilir bir genişlikte kalıyor
- Uygulama uçtan uca İngilizce: tarihler, varsayılan kategoriler ve dışa aktarma
  başlıkları dahil
- İşlem ve abonelik yenileme tarihi artık takvimden seçilebiliyor
- "Satın alımlarımı geri yükle" artık sonucu bildiriyor
- Play'e geçici olarak ulaşılamadığında Pro hakkı düşmüyor

## 1.1.0 — 16 Eylül 2026

**Gelir modeli ve deneyim iyileştirmeleri.**

- Ücretsiz sürümde alt barın üstünde reklam şeridi; Money Agenda Pro bunu kaldırıyor
- Hiçbir özellik ödemeye kilitlenmedi — Pro yalnızca reklamı kaldırıyor
- Google ile giriş ve bulut yedeği
- Sekme geçişleri yeniden yazıldı

## 1.0.0 — 15 Eylül 2026

**İlk sürüm.**

- Kartın ne zaman kesileceği, ne zaman ödeneceği — kartın kendi kurallarıyla
- Taksit ve kredi planı; BSMV/KKDF dahil efektif oran
- Abonelik, alan adı ve yenilenen dijital varlıklar
- Bütçe, hedef ve raporlar; CSV / XLSX / PDF dışa aktarma
- Şifreli yedek, PIN ve parmak izi kilidi
'''

FILES[(EN, 'features')] = '''---
title: Features
seoTitle: Features — what Money Agenda tracks
description: Credit card statement and due dates, instalments, loans, subscriptions and domain renewals, budgets, reports and reliable reminders.
lang: en
path: /en/features/
route: features
lead: Money Agenda gathers five things into one calendar - cards, loans, renewals, budgets and reminders. Each could be a separate app; here they share one list.
---

The home screen shows what is **coming**, not what is past.

## Credit cards

Statement and due dates, billing cycles, minimum payment, current balance and remaining
limit. Every card has its own statement day and its own gap to the due date, so the app
keeps those per card rather than assuming one rule for all.

Days that do not exist in every month shift correctly: a card that closes on the 31st
closes on the 28th in February, not the 1st of March.

## Instalments and loans

The remaining plan for instalment purchases, a loan amortisation table, and the effective
cost **including the Turkish BSMV and KKDF levies**. The monthly rate a bank advertises
and what you actually pay are not the same number; the app shows both.

## Subscriptions and renewals

Subscriptions, domains, hosting, SSL, insurance - anything that renews, with its date.
This category is missing from most finance apps, yet a domain that lapses quietly is
still a payment you missed.

Amounts can be fixed or variable. For variable ones (a utility bill) the app does not
invent an estimate; it shows past payments and you enter the figure.

## Budgets and reports

Category budgets, goals, monthly reports and a month-end estimate. The estimate formula
is written on screen - no AI, and a number that cannot say where it came from is not
trustworthy.

Reports and transactions export to **CSV, XLSX and PDF**. Your data is not locked in.

## Reminders

Alerts before and after the due date, quiet hours and a daily digest. Reminders use exact
alarms, so they fire on time even when the device is idle, and the schedule is rebuilt
automatically after a reboot.

Because some manufacturers' battery managers restrict background apps, the app ships a
step-by-step guide for your device brand and a test notification button.

## Security and privacy

- Encrypted local backup; the password stays with you alone
- PIN and fingerprint lock
- Amount masking
- Works fully without signing in - cloud backup is entirely optional

See the [privacy policy](/en/privacy/) for details.
'''

FILES[(EN, 'why')] = '''---
title: Why Money Agenda
seoTitle: Why Money Agenda - how it differs from budgeting apps
description: It shows what is coming rather than what is past, knows the Turkish banking calendar, keeps data on your phone and locks no feature behind payment.
lang: en
path: /en/why-money-agenda/
route: why
lead: Most budgeting apps tell you what you spent. That is usually not the problem.
---

The problem is missing a statement date and rolling into the next cycle. Not knowing
which month an instalment plan ends. A domain lapsing quietly. None of that is solved by
knowing how much you spent on coffee last month.

## Four differences

### 1. The home screen looks forward

The obligation calendar is the centre of the product. Whatever is due today and in the
coming days sits at the top. Charts of last month exist, but in
[reports](/en/features/) - not on the home screen.

### 2. It knows the Turkish banking calendar

Statement day, due date, billing cycle, minimum payment, BSMV and KKDF. An international
budgeting app either lacks these or approximates them. Here they are computed by
unit-tested rules, and amounts are held to the kurus with no rounding drift.

### 3. Renewing digital assets

Domains, hosting, SSL, licences. If you run a site these are real payments, and missing
one is expensive to undo. This category is hard to find elsewhere.

### 4. Your data stays, features do not lock

The app works fully **without signing in**. Cloud backup is optional. No bank connection,
no SMS permission, no AI.

The free version shows an ad strip and Pro removes it - but **no feature sits behind
payment**. A user who never pays still gets the whole product. The distinction is not
"ad-free", it is that not paying costs you nothing in function.

## What it deliberately does not do

- **No bank connection.** There is no open banking integration. You enter the records;
  in return you share no banking credentials.
- **No SMS reading.** The permission is not even requested.
- **No AI.** Every calculation is deterministic and its formula is on screen.
- **No investment advice.**

---

[Get it free on Google Play](https://play.google.com/store/apps/details?id=com.moneyagenda.app)
'''

FILES[(EN, 'support')] = '''---
title: Support
seoTitle: Support and frequently asked questions
description: Frequently asked questions about Money Agenda, fixing missing notifications, moving your data and contact details.
lang: en
path: /en/support/
route: support
lead: If you cannot find what you need here, write in - emails are usually answered within a few working days.
---

## Notifications are not arriving

This is the most common issue and the cause is usually the phone's battery management
rather than the app.

1. In the app, go to **Settings - Reminder settings - Send test notification**. If it
   arrives, permissions and channels are fine.
2. On the same screen, **"Notifications are not arriving"** opens a step-by-step guide
   for your device brand.
3. In the phone's settings, turn **off battery optimisation** for Money Agenda.
4. On Android 12 and above, make sure the **exact alarm** permission is granted.

## Moving data to another phone

- **Backup file:** Settings - Backup, create a password-protected backup, move the file
  to the new phone and restore it there. The password stays with you alone; if it is
  lost, the file cannot be opened.
- **Cloud backup:** if you sign in with Google, your records are stored against your
  account and appear on the new device when you sign in with the same account.

## I bought Pro but ads are still showing

Use **Restore my purchases** on the Pro screen. A temporary problem reaching Play does
not remove the entitlement; it returns on its own once the connection is back.

To cancel a subscription, use the subscriptions section of your Google Play account; the
"Manage subscription" link in the app takes you there.

## Which Android versions are supported

Android 8.0 (API 26) and above. Tablet layout is supported.

## Is there an iPhone version

Not at the moment.

## Where does my data go

It stays on your phone. See the [privacy policy](/en/privacy/).

## Contact

[yzcdev@gmail.com](mailto:yzcdev@gmail.com)

When reporting a problem, include your device model, Android version and the app version
(Settings - Version).
'''

FILES[(EN, 'privacy')] = '''---
title: Privacy Policy
seoTitle: Privacy Policy - what data is processed
description: What Money Agenda processes, where it is stored and who it is shared with. Your records stay on your phone by default.
lang: en
path: /en/privacy/
route: privacy
lead: Money Agenda (com.moneyagenda.app) is an Android app for personal finance and obligation tracking. This policy explains what data the app processes.
updated: "Last updated: 15 September 2026"
---

> **In short:** Your records are kept only on your phone by default. If you do not sign
> in with Google, no financial data leaves your device. The free version shows ads; the
> ad network does not see your financial records.

## Data collected

**Without signing in:** Nothing is collected. All records stay in the local database on
your phone.

**If you sign in with Google** (optional), the following are processed for cloud backup:

- **Account identifier:** your Google account email address and user id (uid)
- **Your in-app records:** transactions, accounts, cards, instalments, loans,
  subscriptions, budgets and categories

## Where data is stored

Cloud backup is stored on Google Firebase (Firestore), hosted in Google Cloud's European
region. Access is limited to records belonging to your own account; security rules
prevent access to another user's data.

## Sharing and purpose

- **Your financial data is never sold or used for advertising.** Amounts, card names,
  people's names, categories and budgets are never sent to an ad network or any other
  third party.
- **No analytics or crash reporting service is used.**
- Cloud backup data is processed solely to store your backup and sync it across your
  devices.

## Advertising

The free version of the app shows an ad strip at the bottom of the screen. Ads are served
by Google AdMob, which may process:

- Advertising identifier (Android Advertising ID) and approximate location
  (country/city level from the IP address)
- Device and app information: device model, OS version, app version
- Ad interaction: whether the ad was shown and whether it was tapped

Google processes this data under its own responsibility. **None of your financial records
are sent to AdMob** - the ad strip does not see the app's content.

Users in the European Economic Area and the United Kingdom are shown a consent screen
before ads appear; without consent, no personalised ads are shown. You can change your
consent choice later from within the app.

To remove ads entirely you can buy **Money Agenda Pro** in the app (monthly, 6-month or
yearly subscription, or a one-time lifetime package). With Pro no ad request is made at
all. Purchases go through Google Play; your payment details are never passed to the app,
which only learns whether the entitlement exists.

## Permissions

- **Notifications:** for payment day reminders
- **Exact alarm:** so the reminder fires at the right time
- **Internet:** only for cloud backup and exchange rate data

The app does not request SMS read permission and does not connect to your banking apps.

## Retention and deletion

Your cloud backup is kept until you delete it. Deletion can be done in two ways:

- In the app: **Settings - Account and cloud backup - Delete my account**
- Through the [account deletion page](/en/delete-account/)

When the account is deleted, your cloud records are removed; local records on your phone
remain.

## Children's privacy

The app is not directed at users under 13 and does not knowingly collect data from that
age group.

## Contact

[yzcdev@gmail.com](mailto:yzcdev@gmail.com)
'''

FILES[(EN, 'terms')] = '''---
title: Terms of Use
seoTitle: Terms of Use
description: "Money Agenda terms of use: scope of the service, accuracy of data, limits of reminders, Pro pricing and refunds."
lang: en
path: /en/terms/
route: terms
lead: By using Money Agenda you accept the terms below.
updated: "Last updated: 15 September 2026"
---

> **Money Agenda does not give investment advice.** All calculations, estimates and
> reports in the app are for information only and are based on the data you enter. You
> are responsible for your financial decisions.

## Scope of the service

The app organises the income, expense, card, instalment, loan and subscription
information you enter, using calendars and rules, and reminds you of payment days. The
app does not connect to your bank, does not read your transactions automatically and does
not make payments on your behalf.

## Accuracy of data

Calculations are based on what you enter. An incorrect amount, date or rate leads to an
incorrect result. You are responsible for the accuracy of the information you enter. For
loan instalments, instalment surcharges and statement calculations in particular, **treat
the figure your bank states as authoritative**.

## Reminders

Reminders rely on your device's alarm and notification system. Battery saving settings,
notifications being turned off, or the device being powered down can delay reminders or
prevent them entirely. The app does not guarantee that a payment will be made on time.

## Pricing

**All tracking features are free**; no function is locked behind payment. The free
version shows an ad strip at the bottom of the screen.

**Money Agenda Pro** removes that strip. Monthly, 6-month and yearly subscriptions are
offered alongside a one-time lifetime package. Current prices appear on the purchase
screen in the app, in the currency and with the tax Google Play shows you.

**Subscriptions renew automatically at the end of each period unless you cancel.**
Cancellation is done from the subscriptions section of your Google Play account.
Cancellation takes effect at the end of the current period - you keep access for the
remaining time.

Payments and refunds are handled by Google Play; your payment details are never passed to
the app. Refund requests are subject to Google Play's refund policy.

The lifetime package is a one-time purchase valid for as long as the app remains
published; it is not a subscription and does not renew.

## Limitation of liability

The service is provided "as is". It is not guaranteed to be uninterrupted or error-free.
The developer cannot be held liable for direct or indirect damages arising from use.
Taking regular backups is recommended.

## Backups

The password for a backup file you create in the app stays with you alone. **If you lose
the password, the backup file cannot be opened and its contents cannot be recovered.**

## Changes

These terms may be updated. The current version is always published on this page.

## Contact

[yzcdev@gmail.com](mailto:yzcdev@gmail.com)
'''

FILES[(EN, 'delete-account')] = '''---
title: Account and data deletion
seoTitle: Account and data deletion request
description: You can delete your Money Agenda account and your cloud data at any time, instantly from within the app or by email.
lang: en
path: /en/delete-account/
route: deleteAccount
lead: You can delete your Money Agenda account and your cloud data whenever you want.
---

## From within the app (fastest)

1. Open the Money Agenda app
2. Go to **Settings - Account and cloud backup**
3. Tap **Delete my account** and confirm

This happens immediately; you do not need to send a separate request.

## By email

If you cannot reach the app, send an email titled "Account deletion request" **from the
Google email address belonging to the account** to
[yzcdev@gmail.com](mailto:yzcdev@gmail.com). Requests are handled within 30 days at the
latest, usually within a few working days. For verification, the request must come from
the account's own email address.

## What is deleted

| Deleted | Not deleted |
|---|---|
| Your Google account link | Local records on your phone |
| All records stored in the cloud: transactions, accounts, cards, instalments, loans, subscriptions, budgets | These stay on your device |

To remove local records as well, uninstall the app from your phone.

## Retention

After deletion your cloud data is **permanently removed and cannot be recovered**. Taking
a backup from within the app first is recommended (**Settings - Backup**).
'''

FILES[(EN, 'press')] = '''---
title: Press kit
seoTitle: Press kit - logo, screenshots and fact sheet
description: Logo, screenshots, short descriptions and fact sheet for anyone writing about Money Agenda.
lang: en
path: /en/press-kit/
route: press
lead: If you are writing about Money Agenda, you may use the text and images here without asking.
---

## One-sentence description

> Money Agenda is an Android app built for Turkey that gathers every payment obligation -
> from credit card statement and due dates to subscription and domain renewals - into a
> single calendar.

## Short description (50 words)

Money Agenda shows what is coming, not what is past. Card statement and due dates,
instalments, loans, subscriptions and domain renewals gather in one calendar and remind
you before the date arrives. Every feature is free, the app works without signing in, and
data stays on the phone.

## Fact sheet

| | |
|---|---|
| Name | Money Agenda |
| Package | `com.moneyagenda.app` |
| Platform | Android 8.0 and above |
| Category | Finance |
| Languages | Turkish, English |
| Price | Free; Pro removes ads |
| Released | 15 September 2026 |
| Contact | [yzcdev@gmail.com](mailto:yzcdev@gmail.com) |

## Images

- [App icon (512x512)](/brand/icon-512.png)
- [Share image (1200x630)](/og/default.png)

Screenshots: [Today](/screens/01-bugun-840.webp) ·
[Card detail](/screens/05-kart-detay-840.webp) ·
[Instalments](/screens/08-taksitler-840.webp) ·
[Reports](/screens/02-raporlar-840.webp)

## Please get these right

- The app **uses no AI**; every calculation is a deterministic rule.
- It **does not connect to banks** and does not read SMS. The user enters the records.
- The free version shows ads; **no feature is locked behind payment**.
- It does not give investment advice.
'''

FILES[(EN, 'tools')] = '''---
title: Tools
seoTitle: Free calculators
description: Credit card due date, minimum payment, loan cost and instalment plan calculators - the same engine the app uses.
lang: en
path: /en/tools/
route: tools
lead: The same calculations that run inside the app, in the browser without installing anything. No sign-up, and nothing is sent to a server.
---

These tools are derived from Money Agenda's domain layer and validated against the same
test vectors, so a result here cannot diverge from a result in the app.

> **In preparation.** The tools are going live one at a time. Until they all ship, every
> calculation is already inside the app.

## Coming

- **Due date calculator** - finds the due date from the statement day and shifts
  month-end dates correctly
- **Minimum payment simulator** - how long the debt lasts, and the total interest, if you
  keep paying only the minimum
- **Loan cost calculator** - total repayment and effective rate including BSMV and KKDF
- **Instalment plan calculator** - instalment amount, surcharge and monthly split
- **Subscription cost calculator** - annual total across different billing frequencies

## Meanwhile

All of it is already
[in the app](https://play.google.com/store/apps/details?id=com.moneyagenda.app), with
your own cards and your own loan.

[Features](/en/features/) · [Why Money Agenda](/en/why-money-agenda/)
'''

FILES[(EN, 'release-notes')] = '''---
title: Release notes
seoTitle: Release notes - what changed
description: Money Agenda releases and what changed in each one.
lang: en
path: /en/release-notes/
route: releases
lead: Every released version and what it contained. Each line in a release note is verified against the code.
---

## 1.2.1 - 24 September 2026

**Reminders now heal themselves.**

- On some devices the daily reminder refresh could stop silently; the app now notices at
  launch and sets it up again
- Every reminder that fires also schedules the next ones, so the chain no longer depends
  on a single background job
- Reboot, device idle and airplane mode paths verified on a real device

## 1.2.0 - 17 September 2026

**Tablet layout, full English support and a date picker.**

- On tablets the navigation moved to the side; content stays at a readable width
- The app is now fully English: dates, default categories and export headers included
- Transaction and subscription renewal dates can be picked from a calendar
- "Restore my purchases" now tells you the result
- A temporary problem reaching Play no longer removes Pro

## 1.1.0 - 16 September 2026

**Revenue model and experience improvements.**

- An ad strip above the bottom bar in the free version; Money Agenda Pro removes it
- No feature was locked behind payment - Pro only removes the ad
- Sign in with Google and cloud backup
- Tab transitions rewritten

## 1.0.0 - 15 September 2026

**First release.**

- When a card closes and when it is due - by each card's own rules
- Instalment and loan plans; effective rate including BSMV/KKDF
- Subscriptions, domains and renewing digital assets
- Budgets, goals and reports; CSV / XLSX / PDF export
- Encrypted backup, PIN and fingerprint lock
'''

for (folder, name), body in FILES.items():
    os.makedirs(folder, exist_ok=True)
    with io.open(os.path.join(folder, name + '.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)
print(str(len(FILES)) + ' sayfa yazildi')
