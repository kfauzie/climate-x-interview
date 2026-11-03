# Live build session

## Why this repo exists
Preparation for a live prototyping interview for a Principal PM role (senior IC) at Climate X. Confidential: keep this repo private.

## The session
- Live build session, remote with screen share, with **Kevin Luo** (leads product). Kevin hands over a real dataset of Climate X outputs during the session, which will differ from any practice run, and asks for a new feature built on it
- **Kevin role-plays an enterprise customer.** Run live discovery on him first, get past the stated ask to the real workflow problem, and keep asking while building so every trade-off traces back to something he said
- Kamil Kluza (co-founder): the prep page lists him for the session, but that is wrong. Per the candidate, the session is with Kevin, and the conversation with Kamil only happens **if it goes well**. Kamil brings a founder's lens: commercial impact, product strategy, the Series B vision
- Considered for **Seat 1 (Customer & UX / Discovery)**: discovery-centric, with LLM familiarity as support. Frame value commercially (investment and lending decisions; ROI = time saved, consultant cost avoided, better decisions), not as safety
- Assessed on thinking and outcome, not polish. AI tools are encouraged
- What lands:
  - think out loud and narrate choices
  - take the work as far as something an engineer can review (a PR, not a spec)
  - make AI output trustworthy for regulated, decision-grade use (evals, golden datasets, human in the loop, thresholds, failure modes, the line between deterministic and AI)
  - keep the commercial thread: customer value, adoption, conservative enterprise buyers

## Second-stage prep from the recruiter (numi, received 2026-11-03)
- **Format:** 60-minute live build with Kevin (VP Product and Tech, ex-Revolut). He sends a data pack 15–20 minutes before; get it into Claude or Cursor, then share the screen and build live. Nothing to prepare or start in advance. Two-way: he'll chat and nudge ("have you thought about X?"), so narrate. If it goes well, a separate 30-minute conversation with Kamil
- **Where I stand:** strong first-round feedback on AI evaluation and reliability (ExaCare), customer discovery (Multiverse, users and sponsors), and hands-on delivery with safeguards
- **The one thing to nail:** *show the product and UX side, not just the agent optimisation.* His one reservation: experience looked narrowly focused on optimising agents, with less evidence of UI, broader UX and end-to-end product judgement. Take the build all the way to a **clear, usable product a non-technical customer would trust and use**, and show judgement on **what is worth building**
- **What wins:** build hands-on from a standing start ("it's your playground"); practical AI judgement (numbers in code, the model for interpretation; cost, reliability, where not to use a model); interrogate the data honestly (surface the real signal, e.g. a loss concentration; flag uncertainty); drive to a clear, traceable action (decision-ready beats a better risk report); iterate fast, think big (narrow early, ship a first version, then improve; show ambition)
- **What trips people up:** over-analysing and running short on the build; being a "director" rather than a builder; all backend, no customer; not finishing to something credible (leave time for checked, usable output with explicit limitations)
- **Kamil (30 min):** cut to the chase (conclusion, one or two reasons, stop); bias to speed and action ("here's what I'd do now, and why"); flex when challenged, don't dig in; at ease with ambiguity (make the call, name the assumption, say what you'd validate); own failures cleanly and briefly; show you want this IC seat for the long run (not an interim stop after founding Savvy)
- **How the repo answers the reservation:** lead with `pm-design` (design philosophy, what's worth building, trust for non-technical users, review checklist) and the prototype's screens; keep evals and the deterministic/AI split as supporting proof
