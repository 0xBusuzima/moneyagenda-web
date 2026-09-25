---
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
