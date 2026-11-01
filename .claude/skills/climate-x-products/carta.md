
# Climate X Carta

Source tags: **[site]** climate-x.com (read 2026-11-01; Climate X's own claims), **[web]** press or third parties, **[prep]** my preparation notes, **[analysis]** my inference. Present [analysis] items as hypotheses, never as facts.

## What it is [site]
- Corporate asset mapping: "location data for **18.7 million** public and private companies worldwide". Enter a company; Carta finds its physical assets (offices, factories, data centres, warehouses…) and subsidiaries, including joint ventures with a >50% stake, across every sector and region
- **Pipeline:** multi-source discovery (company websites, job boards, registries, mapping services) → assets geo-located, classified and **scored for materiality** → validation combining AI, ML, LLMs, third-party data and **human review of every output** → **satellite image checks** on high-impact sites → outputs feed Spectra or the customer's own systems
- **Quality control:** automated anomaly detection, pipeline monitoring, spot checks, **annual remapping**; tracks new builds, closures and divestitures
- **Delivery:** a **fully managed service** run by Climate X ("service-first"), in standardised formats; one counterparty or hundreds; results "in days, not months"
- Claims it "significantly outperforms standalone LLMs and typical manual searches"; "trusted by leading global banks, including a top three investment bank"; CBRE expanded its climate risk capabilities with Climate X
- Product UI: company search, a map of located assets, an "asset directory" table (parent, subsidiary, industry, premise type, criticality, address, coordinates), counts by confidence (e.g. 90% high, 10% medium), breakdowns by asset type and geography, capital figures, CSV export and a "Spectra →" hand-off

## Customers and users
- **Banks:** climate risk of corporate borrowers; mapping the full asset hierarchy behind a counterparty for provisions and SS5/25 data expectations [site]
- **Investment banks, asset managers and PE:** screening, due diligence on targets, portfolio exposure beyond home markets [site]
- **Advisers and insurers** [site]
- Likely users: credit analysts, portfolio managers, deal teams, ESG and risk teams [analysis]

## Value proposition [site]
- Physical risk for companies you **don't own** (most of a bank's or investor's exposure), without asking each one for data; "save yourself from months of manual research, fragmented data sources or expensive consultants"
- Climate X's argument: "you can't provision for what you haven't mapped". Indirect losses (business interruption, supply chain) run several times direct damage, so asset hierarchies matter

## Strengths [analysis]
- A hard data problem solved at scale is a moat; it also feeds Spectra, Adapt and Adaptation Finance (lead generation)
- Already designed for trust: materiality scores, human review, satellite checks, confidence levels shown in the UI
- Clear AI-native use case with humans in the loop

## Weaknesses and risks [analysis]
- **No complete golden dataset:** accuracy is hard to prove when the true asset list is unknown
- Missed sites (recall) understate risk; wrong sites (precision) erode trust; each error a customer finds damages credibility
- Thin public footprints for small and private companies may make coverage uneven
- A managed service scales with people: unit cost and turnaround as volume grows
- Annual remapping may lag deals and restructurings

## Opportunities (hypotheses to test) [analysis]
1. **Per-site provenance:** show the sources, validation steps and confidence behind each site (already partly in the UI as confidence levels), so a credit analyst can defend it
2. **Evaluation without a full golden set:** validate against companies whose full site lists are known (customers' own, published lists), representative of small and private firms; track precision and recall; use customer corrections as feedback
3. **Self-serve for the common case:** instant results for well-known companies, managed service for complex ones; reduces cost and turnaround
4. **Customer correction loop:** customers add or remove sites; corrections feed evals and models
5. **Deal and credit workflow:** a pack for a target or borrower (structure → assets → materiality → Spectra risk → Adapt options) in time for the decision
6. **Change alerts:** notify when a counterparty opens, closes or sells material sites, instead of waiting for annual remapping

## Discovery questions (non-leading)
- How do you assess a borrower's or target's physical climate risk today? How long does it take?
- When you last relied on a company's asset list, how did you know it was complete?
- What would make you trust (or distrust) a site you hadn't seen before?
- Which counterparties matter most, and why those?

## Related
- `spectra.md` (risk engine), `adapt.md` (what to do about it), the `climate-x-company` skill
