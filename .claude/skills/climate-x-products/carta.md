
# Climate X Carta

Confidence tags: **[prep]** from my preparation notes, **[analysis]** my inference. ⚠️ No public source for Carta was found in web search. Everything here comes from prep material and should be confirmed with Climate X.

## What it is
- Maps a company's structure, subsidiaries and assets, and the physical risk flowing through them [prep]
- Lets customers assess the climate risk of *other* companies (borrowers, investments, potential acquisitions) without those companies' internal asset lists [prep]
- Reported approach: public sources (company websites, job ads, registries such as Companies House, map data), processed by LLMs with humans in the loop [prep, unverified]

## Customers and users
- **Banks:** climate risk of corporate borrowers in the lending book [prep]
- **Asset managers and PE:** screening investments and due diligence on acquisitions [prep]
- Likely users: credit analysts, portfolio managers, deal teams, ESG and risk teams [analysis]

## Value proposition
- Physical risk for counterparties you **don't own**, which is the bulk of a bank's or investor's exposure, without asking each company for data
- ROI: replaces manual research and consultant work, and supports better lending and investment decisions [prep framing]

## Strengths [analysis]
- Solves a hard data problem (where is a company's exposure?) that is a moat once solved at scale
- Reuses Spectra's risk engine on discovered assets, giving one consistent methodology
- Clear AI-native use case: LLMs extracting structured asset data from messy public sources

## Weaknesses and risks [analysis]
- **No complete golden dataset:** accuracy is hard to prove when the true asset list is unknown
- Missed sites (recall) understate risk; wrong sites (precision) erode trust. Each error a customer finds damages credibility
- Smaller and private companies have thin public footprints, so coverage may be uneven
- Hard to tell whether a site is material (a head office vs a key factory) without revenue or operational weighting

## Opportunities (hypotheses to test) [analysis]
1. **Confidence per site and per company:** sources and confidence visible, with sites confirmed by several sources marked as such and conflicts flagged for review. Builds trust with conservative buyers
2. **Evaluation without a full golden set:** validate against companies whose full site lists are known (customers' own lists, published lists), with a representative mix including small and private firms. Track precision and recall, and use customer corrections as a feedback signal
3. **Materiality weighting:** weight assets by revenue or operational importance so risk reflects business impact, not just site count
4. **Customer correction loop:** let customers add or remove sites, and feed those corrections into evals and models
5. **Deal workflow:** a due-diligence pack for a target company (structure → assets → risk), in time for a deal decision

## Discovery questions (non-leading)
- How do you assess a borrower's or target's physical climate risk today? How long does it take?
- When you last relied on a company's asset list, how did you know it was complete?
- What would make you trust (or distrust) a site you hadn't seen before?
- Which counterparties matter most, and why those?

## Related
- `spectra.md` (risk engine), the `climate-x-company` skill
