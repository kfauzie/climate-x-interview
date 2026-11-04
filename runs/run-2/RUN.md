# Run 2

**Status:** interview done; next: test her claims against the data (pm-1 Answer), then the solution concept (pm-3)
**Dataset:** `data/harbourside_mortgage_book_spectra_2026-10.csv` (Spectra export of the mortgage book, October 2026)
**Analysis:** `notebooks/initial_review.py` (every number below comes from it)

**On Notion (2nd round prep)**
- Discovery questions v2 (with the data questions): https://app.notion.com/p/40e8f31ef05f819e9d1ee2d8a4e0c209
- Discovery questions v1 and call notes: https://app.notion.com/p/40e8f31ef05f8129964ec33de404a680

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

## Initial review (pm-1)
Code: `notebooks/initial_review.py`. Rated E–G means in 2050; central = SSP2-4.5, severe = SSP5-8.5.

| Finding | Why it might matter (guess) | The question it becomes |
|---|---|---|
| **Newer lending is riskier.** 16% of the balance lent since 2024 is rated E–G for subsidence, against 6% before. It jumped from 4% in 2023 to 15% in 2024. Under the severe scenario: 29% against 13% | Something changed in 2024 in where or what they lend; may push against any limit they set | The data shows 16% of your lending since 2024 is rated E–G for subsidence, against 6% before. Does that match what you see? If underwriters had seen the rating on those applications, what would they have done differently? |
| **It's concentrated.** 71% of the subsidence-risk balance (£40m, 173 loans) sits in 5 postcode districts (RG30, ME14, LU1, CM1, PE1), which hold 14% of all lending | A few areas, perhaps new estates, drive the risk; acting on a few areas may be enough | The data shows most of your subsidence risk sits in five postcode districts. Does that match what you see? How would a rating on each application change lending in those areas? |
| **The newest lending can't be seen.** The 118 loans completed since 3 Jul 2026 (£23m) have no scores; everything up to 30 Jun has them. And 6 loan IDs appear on two rows with different dates and balances, so adding up rows counts £1.4m twice | Scores arrive in batches months after lending; the duplicates suggest a manual step that can double count | The data shows your last 4 months of lending have no ratings. Does that match what you see? If the rating came at application instead, what would that change for you? |

**Checked, nothing found:** £ loss matches damage % × property value; ratings match their bands; no LTV over 100%; river and coastal flood aren't rising in newer lending; broker and direct lending look similar (9% and 12%)

**Follow-ups to ask me**
- What changed in 2024: split the jump by postcode district, new build and product
- Rerun every finding under the severe scenario and for 2030
- Compare by number of loans instead of balance

**The data:** 2,406 rows, one per loan (2,400 loans, £442m, completed Jan 2015 to Oct 2026). Columns: loan ID, completion date, postcode district, region, property type, new build, channel, product, value, balance, LTV; then rating A–G, damage % and £ loss a year for river, coastal and surface water flood and subsidence, under central and severe, for 2030 and 2050
**Usable:** yes, up to 30 Jun 2026; take the latest row for the 6 repeated loan IDs. Guess: a Spectra export of the book, used for risk reporting

## From the interview (claims to test)
- **Her risk appetite:** no more than 10% of new lending rated E–G (her board limit). She told the board in September she was within it, using June data
- **The blind spot:** Spectra ratings arrive quarterly; Tom (analyst) joins the export to the loan book by loan ID in Excel, about a week each quarter, and flags new lending since March rated E–G for flood or subsidence under the central scenario. New loans go unseen for up to 3 months
- **Her worry:** she may already be over 10%, before the PRA review of climate risk management next spring. "I need to know where we stand now"
- **Trust:** total balance must match finance's figure to the pound; the method written down for the board and the PRA
- **Sign-off:** IT for anything touching the broker portal (about a 6-month queue); credit committee for any change to lending

## Missed in the call (from feedback, to follow up)
- **Who acts on it:** underwriters follow the lending policy, and no single loan breaches a portfolio limit. The real lever is likely credit committee tightening criteria, or capping a broker or an area
- **The data finding (calculated):** since 2024, 16.0% of the lending balance is rated E–G for subsidence (central, 2050), against her 10% limit; 28.6% under the severe scenario. Since March 2026: 9.7% (only loans scored so far)
- **Scenario:** which one and who decided; a non-executive director has already asked about the severe scenario
- **What she can't see:** broker firm isn't in the file, only the channel
- **When it went wrong:** last quarter further advances were double counted; matches the 6 duplicate loan IDs
