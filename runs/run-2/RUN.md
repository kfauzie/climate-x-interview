# Run 2

**Status:** initial data review done; next: discovery questions (pm-2)
**Dataset:** `data/harbourside_mortgage_book_spectra_2026-10.csv` (Spectra export of the mortgage book, October 2026)
**Analysis:** `notebooks/initial_review.py` (every number below comes from it)

**On Notion (2nd round prep)**
- (none yet)

Everything below applies to **run 2 only**. Do not carry it into any other run.

## Customer (given for this run)
- **Name:** Helen Price
- **Role:** Chief Risk Officer
- **Organisation:** Harbourside Building Society, a mid-size UK building society. Residential mortgages only. Regulated by the PRA
- **Relationship with Climate X:** Spectra customer for about a year

## Customer ask (given, word for word)
> "We need Spectra ratings showing up in the broker portal, so underwriters see the climate risk on every application before we make an offer."

*This is a solution (put ratings in the broker portal), not a problem. Discovery should find what an underwriter would do differently once they see the rating, and what goes wrong today because they don't.*

## What the ask implies (inferred, test in discovery)
- **The user is the underwriter,** deciding on one mortgage application at a time, before an offer. Helen (CRO) is the buyer and owns the risk policy
- **The decision is per property, at application time,** not on the whole book. Spectra can score one address or many, and has an API (climate-x-products)
- **A rating alone may not change a decision.** Unknown: what an underwriter should do with a poor rating (decline, lower the loan size, ask for a survey, refer it on), and whether a policy says so
- **"The broker portal" may not be theirs.** Unknown: who runs it, whether brokers would also see the rating, and what that means for customers
- **Why now:** PRA SS5/25 expects property-level climate data in risk management (climate-x-company). Unknown: whether this is driven by the regulator, by losses, or by the board

## Data notes
- **What it is (guess, to confirm):** a Spectra export of the whole mortgage book, scored after the loans completed. Likely used for risk reporting and the PRA's climate expectations, not for decisions on applications
- **One row = one loan.** 2,406 rows, 2,400 loans, £442m balance, completed Jan 2015 to Oct 2026. 81% came through brokers. About 27 loans a month completed in the last 12 months
- **Columns:** loan ID, completion date, postcode district (e.g. RG30, not the full postcode), region, property type, new build, channel, product, property value, balance, LTV; then rating (A–G), damage % and £ loss a year for each hazard, scenario and year
- **Hazards:** river flood, coastal flood, surface water flood, subsidence. **Scenarios:** SSP2-4.5 (central, roughly today's policies), SSP5-8.5 (very high emissions). **Years:** 2030, 2050. So 16 ratings per loan
- **Not scored:** the 118 loans completed since 3 Jul 2026 have no Spectra scores; every loan up to 30 Jun 2026 has them
- **Duplicates:** 6 loan IDs appear twice, with different completion dates and balances (guess: a further advance or a product switch)
- **No property value or LTV:** 11 loans
- **Usable:** yes, for the book up to 30 Jun 2026

## Findings (initial review)
- **Rated E–G on at least one hazard by 2050 (central):** 329 loans (13.7%), £69m balance. Under very high emissions: 668 (27.8%)
- **Newer lending is riskier:** 17.3% of loans completed since 2024 are rated E–G, against 11.7% before
- **Subsidence drives it:** 173 of the E–G ratings, and £2.4m of the £4.9m expected loss a year (central, 2050)
- **The rating depends on the scenario and year:** for 405 loans, the worst rating moves by 2 bands or more
- **Concentrated:** 42% of the E–G loans sit in 5 postcode districts (RG30, ME14, PE1, LU1, CM1)
- **High LTV and poor rating together:** only 18 loans (£6.6m) are over 85% LTV and rated E–G
- **What this data can't tell us:** applications (including ones declined or not completed), what underwriters decided, buildings insurance, loss to the society rather than damage to the property

## Questions for Helen (from the data)
| Question | Why ask | How the answer would change the product |
|---|---|---|
| If an application came in rated E or worse, what should the underwriter do differently? | 13.7% of the book (329 loans, £69m) is rated E–G on at least one hazard by 2050; 17.3% of lending since 2024 | If there's a set action (refer it, lend less, ask for a survey), the screen shows the rating with that action. If there's none, a rating alone changes nothing, and the policy comes first |
| Which rating should the underwriter see: the risk now or by 2050, and under which scenario? Who decides? | Each loan has 16 ratings; for 405 loans the worst one moves by 2 bands or more depending on the scenario and year | Decides what appears on each application: one rating or several, and which is the default |
| How do new loans get their Spectra scores today, and how long after completion? | The 118 loans completed since 3 Jul 2026 have no scores; every loan before 30 Jun 2026 has them | If scores arrive in batches months later, getting a score at application is the core build. If they're already near-instant, the work is only showing them |

## Defaults
(none yet)
