---
name: pm-5-build
description: "Turn the agreed screens into a working first version, fast: one HTML file, numbers calculated by code, AI only for interpreting input. Use when building or changing the prototype."
---

# Build: the working first version

Input: the agreed screens from pm-4-solution-design and the solution concept (workflow, success criteria, test cases). Before starting, read climate-x-products, climate-x-company and climate-x-role.

## How to build
- One plain HTML file with inline JS and CSS. No framework, no build step.
- Build all the agreed screens in one go, so the whole flow can be tried end to end. After that, change one thing at a time: edit, never regenerate the whole file.
- Numbers, checks and labels are calculated by code, as plain functions kept separate from the AI part. AI only turns messy input into choices the user confirms; it never produces a number.
- Use the data provided directly. If there's no real data, use a small synthetic file, clearly labelled.
- Each change after the first build should take about two minutes. If it will take longer, tell me first and suggest a smaller step.

## Look
Match the agreed screens from pm-4-solution-design exactly. Don't add new elements.

## Check before showing me
- Run the test cases from the solution concept once, at the end.
- Ask: can a first-time user tell in five seconds what each screen is for and what to do next? Are the numbers right?
- After each change, run the tests and a quick headless check (about 10 seconds): the page loads, nothing covers it, the main flow clicks through end to end, no errors on the page. No screenshots or visual walkthroughs unless I ask.

## Later, only if I ask
- Branch and PR with screenshots, how to run it and test results
- Dark mode and mobile layout
- A clickable demo that replays precomputed answers
- Hand-off: one PR per screen behind a feature flag, engineer review, staging, then release and measure against agreed targets
