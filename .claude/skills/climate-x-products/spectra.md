# Spectra

## What it is
- Physical risk → asset-level financial loss. Search an address, or upload a portfolio (up to 100k rows), pick scenario settings, download a report
- Web app, CSV export (Tableau, Power BI, Qlik), Enterprise API, PDF reports
- 11 hazards, RCPs and SSPs, 2020–2100 in 5-year steps (see `climate-x-company` → Method)
- Outputs: ratings A–G with accuracy, probability, severity; Expected Annual Loss in £ and %; cVaR; portfolio score; flat-level detail for residential
- Pitch: "Replace outdated Power BI and Excel files"; glass-box methodology

## Who buys it
- Banks (climate and credit risk): stress tests, ICAAP, capital, ECL, collateral, lending decisions; SS5/25 evidence
- Tier 1 bank: ~0.5m properties, cVaR → provision figure; next step: API in mortgage underwriting
- Real estate (CBRE, Aroundtown), insurers, PE, consultancies; partners (Mitie, IBD, Scaler, Nfq)
- Typical user: risk analyst; financially literate, not a climate expert

## Gaps (my take)
- Property damage ≠ bank loss: banks need LTV, LGD, insurance. Their own article says indirect losses run 6–14× direct
- Choices move the headline: scenario, year, hazards, defended or not, per-loan vs per-property, missing data. Two analysts, two numbers
- Scenario set in transition: "severe" moving from SSP5-8.5 to SSP3-7.0
- Wide exports (hazard × scenario × year × metric columns) push people back into Excel
- Moody's and S&P bundle with credit data; Climate X has to win on depth, usability, trust

## Opportunities (my take)
1. Answers with their method: assumptions, data dates, lineage, reproducible. SS5/25 evidence by default
2. Analyst agent: plain-English question → choices the user confirms → numbers from code, rows cited
3. Scenario transition: old and new "severe" side by side, change logged for the methodology owner
4. Lender view: property loss → loan impact with the bank's LTV, LGD, insurance; feeds ECL and ICAAP
5. Underwriting via API: new applications checked against risk appetite in real time
6. Event impact: storm hits → which assets and loans, how much
7. Thresholds per customer: at what rating does a decision change? Also tells the science team what to prioritise

## Questions
- Last time a Spectra number went into a decision or report: who used it, what did they do?
- At what point does a risk change your decision? Why there? Same across portfolios?
- When someone challenged a number, what did you show them?
- How do you get from property damage to impact on your book?
- Which scenario and year do you report, how did you justify it, and what changes as SSP5-8.5 retires?
- What do you do with the export after downloading it?
