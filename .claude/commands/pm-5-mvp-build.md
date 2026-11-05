---
name: pm-5-mvp-build
description: "Turn the agreed screens into a working first version, fast: one HTML file, numbers calculated by code. Use when building or changing the prototype."
---

# Build: the working first version

Input: the agreed screens from pm-4-solution-design and the solution concept (workflow, success criteria, test cases), from the Notion page linked in `RUN.md`, fetched fresh every time. Before starting, read climate-x-products, climate-x-company and climate-x-role. Follow the communication guide in climate-x-role for everything you write.

## How to build
- One plain HTML file with inline JS and CSS. No framework, no build step.
- Build all the agreed screens in one go, so the whole flow can be tried end to end. After that, change one thing at a time: edit, never regenerate the whole file.
- Follow the split between AI, code and people from the solution concept. Every number is calculated by code.
- Use the data provided directly. If there's no real data, use a small synthetic file, clearly labelled.
- Each change after the first build should take about two minutes. If it will take longer, tell me first and suggest a smaller step.

## Look
Match the agreed screens from pm-4-solution-design exactly. Don't add new elements. Add a small animation when the step changes. Exports also leave out buttons.

## Check before showing me
- After each change: run the tests from the solution concept, if there are any, and a quick headless check (about 10 seconds): the page loads, the main flow clicks through, no errors. No screenshots unless I ask.
- Ask: can a first-time user tell in five seconds what each screen is for and what to do next? Are the numbers right?

## Later, only if I ask
- Branch and PR with screenshots, how to run it and test results
- Dark mode and mobile layout
- A clickable demo that replays precomputed answers
- Hand-off: one PR per screen behind a feature flag, engineer review, staging, then release and measure against agreed targets
