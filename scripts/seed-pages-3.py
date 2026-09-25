# -*- coding: utf-8 -*-
"""İngilizce özellik alt sayfaları (F14.7).

Türkçe karşılıklarının aynı yapısı, daha kısa gövde: birincil pazar Türkiye ve blog
yalnızca Türkçe. Yine de her sayfa kendi başına tam — İngilizce okuyan biri eksik bir
şey okumuyor, yalnızca uzun örnekler tekrarlanmıyor.

Bu beş sayfa eklendiğinde İngilizce ana sayfadaki özellik kartları alt sayfalara
bağlanabilir hâle geliyor; o yüzden `src/copy/home.ts` de birlikte güncelleniyor.

Çalıştırma: python scripts/seed-pages-3.py
"""
import io
import os

EN = 'src/content/pages/en'
FILES = {}

FILES['features-credit-cards'] = '''---
title: Credit card tracking
seoTitle: Credit card statement and due date tracking
description: Statement day, due date, billing cycle, minimum payment and remaining limit - computed by each card's own rules.
lang: en
path: /en/features/credit-cards/
route: featuresCards
lead: With a credit card the real question is not "how much did I spend" but "when does it close and when do I have to pay". The app computes both from the card's own rules.
---

## Statement day and due date

Each card gets its own **statement day** and its own gap to the due date. Banks set that
gap differently, so a single default does not fit every card.

From those two the app derives the billing cycle and shows "days left until the due date"
on the home screen.

## Month-end shifting

What happens in February to a card that closes on the 31st? The app **shifts days that do
not exist in a month to the last day of that month**. A card that closes on 31 January
closes on 28 February, not 3 March.

The anchor is preserved: the following month it closes on the 31st again. This is the
detail people tracking by hand most often miss, and it produces a surprise a few times a
year.

## Which statement a purchase lands in

Does a purchase made on the statement day belong to the cycle closing that day or to the
next one? The app keeps the cycle as a half-open interval - `(previous close, this
close]` - so a purchase made **on** the closing day belongs to that statement, and one
made the next day belongs to the following cycle.

## Minimum payment and balance

The card detail shows the current balance, the minimum payment, the amount already paid
and how full the limit is, side by side. Paying the minimum does not clear the debt -
interest accrues on the remaining balance. The app presents the minimum as a floor, not a
target.

## Several cards

Cards are kept separately, each with its own statement day, payment gap and limit. The
"card debt" figure on the home screen combines them; the card detail shows each one.

---

Related: [Instalments and loans](/en/features/instalments-and-loans/) ·
[Reminders](/en/features/reminders/)
'''

FILES['features-instalments'] = '''---
title: Instalments and loans
seoTitle: Instalment plans and loan cost tracking
description: Remaining instalment plans, loan amortisation and the effective cost including the Turkish BSMV and KKDF levies.
lang: en
path: /en/features/instalments-and-loans/
route: featuresLoans
lead: A loan advertised at "2.89% monthly" does not cost 34.68% a year - it costs more. The app computes both figures and shows the gap.
---

## Instalment purchases

When you enter an instalment purchase, the app keeps the remaining instalments, which
month each one falls in, and the total surcharge. The "instalments due this month" figure
on the home screen sums instalments across every card.

"Interest-free instalments" usually are interest-free - but if the **cash price is
lower**, the difference is a hidden cost. The app lets you enter the cash price too and
reports the surcharge separately.

## Loan amortisation

Enter the principal, interest rate and term, and the app produces the monthly payment and
the payment plan. The table separates how much of each instalment is principal and how
much is interest. Early in a loan most of the payment is interest, which matters when you
are deciding whether to pay it off early.

## BSMV and KKDF

In Turkey two levies sit on top of the interest on consumer loans:

- **BSMV** - the banking and insurance transactions tax
- **KKDF** - the resource utilisation support fund

Neither is included in the rate a bank advertises, but both are included in the money you
pay. The app accounts for them when computing the effective cost. This is precisely where
a general budgeting app gives an approximate answer.

Both default to 15% and can be set per loan, because the rates are set by regulation and
change. **Housing loans are exempt**, so comparing an advertised consumer loan rate
directly against a housing loan rate is misleading.

## Why the gap matters

Two banks can advertise almost identical rates while the total repayment differs by a
large amount. The right basis for comparison is not the monthly rate but the **total
repayment**, which the app keeps visible at all times.

---

Related: [Credit card tracking](/en/features/credit-cards/) ·
[Budgets and reports](/en/features/budget-and-reports/)
'''

FILES['features-subscriptions'] = '''---
title: Subscriptions and renewals
seoTitle: Subscription, domain and hosting renewal tracking
description: Subscriptions, domains, hosting, SSL, insurance - anything that renews, with its date, and a reminder before it does.
lang: en
path: /en/features/subscriptions/
route: featuresRenewals
lead: "Subscriptions are set up once and then renew on their own. That is the problem: the payment recurs every month, the decision was made only once."
---

## What you can track

- **Subscriptions** - digital services, gym, magazines, cloud storage
- **Domains** - annual or multi-year renewals
- **Hosting and servers** - monthly or annual
- **SSL certificates and licences**
- **Insurance** - motor, home, health
- **Regular bill-like payments** - choose "variable" when the amount changes

The domain and hosting category is missing from most personal finance apps. Yet a domain
that lapses quietly can cost more than a missed credit card payment.

## Fixed and variable amounts

Services with a known price are entered as **fixed**; things like an electricity bill are
**variable**. For variable ones the app does not estimate the amount - it shows past
payments and you enter the figure. An invented estimate only misaligns the budget.

## Renewal date and frequency

Monthly, quarterly, half-yearly, yearly and two-yearly frequencies are supported. The next
renewal date can be picked from the presets ("in 1 month", "in 1 year") or **from a
calendar** - you may well have started the subscription before adding it to the app.

## Reminders

For each renewal you set how many days ahead you want to be told (default: 3 days and
1 day before). For a subscription you are thinking of cancelling, that leaves time to
decide.

A subscription that falls due turns into a transaction automatically and the next date
moves forward; you do not have to re-enter it.

---

Related: [Reminders](/en/features/reminders/) ·
[Budgets and reports](/en/features/budget-and-reports/)
'''

FILES['features-budget'] = '''---
title: Budgets and reports
seoTitle: Budgets, goals and reports
description: Category budgets, goals, monthly reports, a month-end estimate, and export to CSV, XLSX and PDF.
lang: en
path: /en/features/budget-and-reports/
route: featuresBudget
lead: A budget is not there to forbid spending. It is there to show where you stand before the month ends.
---

## Category budgets

Set a monthly budget per category. The app compares spending against it and warns you as
you approach the threshold. When it is exceeded the alert arrives **on the day** - not at
the end of the month, when nothing can be done about it.

## Month-end estimate

The estimate on the home screen looks at what you have spent so far and how many days
remain:

> remaining days x average daily variable spending over the last three months

The formula is written on screen. There is no AI: a number that cannot say where it came
from is not trustworthy.

## Goals

Set a goal to reach a certain amount by a certain date. The app shows how much you need
to set aside each month and tracks progress.

## Reports

- Income, expense and net flow
- Category breakdown
- The last 12 months
- A breakdown by account and card

## Export

Reports and transaction lists export to **CSV**, **XLSX** and **PDF**. Your data is not
locked in the app. Export headers follow the app's language.

## Currency

Foreign currency amounts use the Turkish central bank rate, refreshed once a day. With no
internet the last known rate is used and its date is shown.

## Security

You can take a password-protected, encrypted local backup. **The password stays with you
alone** - if it is lost, the backup cannot be opened. The app can be locked with a PIN or
fingerprint, and amounts can be masked with one tap.

---

Related: [Privacy policy](/en/privacy/) · [Features](/en/features/)
'''

FILES['features-reminders'] = '''---
title: Reminders
seoTitle: How payment reminders work
description: Alerts before and after the due date, quiet hours and a daily digest. Exact alarms, and the schedule survives a reboot.
lang: en
path: /en/features/reminders/
route: featuresAlerts
lead: A reminder that fails silently is worse than no reminder, because you rely on it. That is why this is the most worked-on part of the app.
---

## When it tells you

For every obligation type you set how many days ahead to be warned. Defaults vary by type:
3 and 1 day ahead for subscriptions, and for credit cards based on the statement and due
dates.

**It also warns you after the due date.** If you missed a payment, an overdue notice
arrives the next day - only for types where money can actually be late (cards,
instalments, loans, bills, debts). That is exactly what the product exists to prevent.

## Quiet hours and the daily digest

If you do not want notifications at night, set a quiet window; a reminder falling inside
it moves to the end of the window. You can also receive a "what is due today" digest once
a day at a time you choose.

## Why they arrive on time

Reminders are set with **exact alarms** (`setExactAndAllowWhileIdle`), so they fire on
time even when the device is idle. Only reminders falling within the next 48 hours get a
real alarm; a daily job adds the rest as they enter that window, which keeps the number of
scheduled alarms far below system limits.

When the phone reboots, the app is updated, or the clock or time zone changes, the
schedule is **rebuilt automatically**. You do not need to open the app.

## Manufacturer battery managers

Some manufacturers' battery management restricts background apps, delaying or blocking
notifications entirely. This is the weakest point of every reminder app and no single
setting fixes it.

The app does two things:

1. **A step-by-step guide for your device brand** - showing where each setting lives
2. **A test notification button** - so you can see it work on your own device

The app also notices when no reminder has fired in the last seven days and suggests the
guide. Saying so is better than failing silently.

---

Related: [Subscriptions and renewals](/en/features/subscriptions/) ·
[Support](/en/support/)
'''

os.makedirs(EN, exist_ok=True)
for name, body in FILES.items():
    with io.open(os.path.join(EN, name + '.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)
print(str(len(FILES)) + ' ingilizce sayfa yazildi')

# Ingilizce ana sayfadaki ozellik kartlari artik alt sayfalara baglanabilir.
p = 'src/copy/home.ts'
s = io.open(p, encoding='utf-8').read()
hedefler = [
    ('Credit cards', '/en/features/credit-cards/'),
    ('Instalments and loans', '/en/features/instalments-and-loans/'),
    ('Subscriptions and renewals', '/en/features/subscriptions/'),
    ('Budgets and reports', '/en/features/budget-and-reports/'),
    ('Reminders', '/en/features/reminders/'),
    ('Security', '/en/features/budget-and-reports/'),
]
parcalar = s.split("href: '/en/features/'")
if len(parcalar) == 7:
    yeni = parcalar[0]
    for i, (_, hedef) in enumerate(hedefler):
        yeni += "href: '" + hedef + "'" + parcalar[i + 1]
    io.open(p, 'w', encoding='utf-8', newline='\n').write(yeni)
    print('ingilizce ozellik kartlari alt sayfalara baglandi')
else:
    print('UYARI: home.ts beklenen bicimde degil, elle bakin (' + str(len(parcalar) - 1) + ' eslesme)')
