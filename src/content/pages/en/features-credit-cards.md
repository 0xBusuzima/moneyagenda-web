---
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
