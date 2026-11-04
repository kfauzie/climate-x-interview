---
name: pm-2-discovery-interview
description: "Prepare and run a 10-minute customer discovery interview: a few open questions that get from what the customer asks for to the real problem behind it. Use when preparing, running or reviewing a discovery call."
---

# Discovery interview

The job is to find the real problem behind what the customer asks for.

Before starting, read climate-x-products, climate-x-company and climate-x-role.

## Principles
- **Problem, not solution.** Questions name the problem, never the requested solution. Don't assume who the user is or what gets built. If they ask for a feature, ask what it would let them do.
- **Be specific.** Ask about a real, recent example, not general habits.
- **Plain, specific words.** In the customer's language (e.g. risk appetite, stress test, provisions). Use the customer's own name for their organisation, not a category ("[Company]", not "the company"). Say "mortgage application" or "loan application", never just "application". Say "the output", not "the number": there isn't always a number.
- **Open questions.** No hint of the answer you expect and no belief built in.
- **One question per line,** so they get asked one at a time.
- **Stay generic.** Look for patterns, not a known story.

## The questions (10 minutes)
X is what they asked for. Fill it in from the case context. No padding: every line must earn its place, and the questions to ask in the call fit on one screen.

1. **Source of the need.**
   - Could you tell me where the need for X is coming from?
   - Is it just [whoever is asking] asking for this, or do others like you get the same request?
2. **User journey.**
   - **Walkthrough**
     - Walk me through the last time you used [the data, named exactly: which file, export or report] for a decision or a report: who did what, in which tool, how long it took.
     - Who would actually use X?
     - *\<Unexpected step → "How did you decide that last time?"\>*
   - **Pain points**
     - Where does most of the time go?
     - What makes it painful?
     - *\<Vague, hedged or suspiciously slow → "Why does that happen? It seems simple."\>*
     - *\<Admits a gap → "What happens when that goes wrong?"\>*
3. **Success criteria.**
   - If this worked, how would you know?
   - What would the impact be: time saved, money, better decisions?
   - What would you need to see to trust the output?
4. **Close.**
   - **\<Recap\>** Three points, biggest problem first, in the customer's words and with their numbers.
   - Anything I missed?
   - Can I email you short questions?

## Data findings
No separate data section and no separate list of things to confirm. Take the findings from pm-1-data-discovery (in `RUN.md`) and include one only if its answer could change what gets built. If none do, include none. Weave each into the walkthrough where it fits naturally, as the way into the customer's story:
- Your data shows [finding in plain words, with a number]. Walk me through the last time that came up.

Anything that needs clarifying is either worth asking in the call (put it in the walkthrough) or it isn't (drop it).

## Save
Publish it as a Notion page under 2nd round prep (https://app.notion.com/p/4088f31ef05f80108cfdcc4ced27f94f), titled "Run N: discovery questions (customer)", with an empty Notes section at the end. The page holds only what I'd say in the interview: the ask and one list of questions. No notes to self (timing, instructions, reminders), except short in-line prompts in italics between `<>`, placed where they're needed. Highlight the recap so it isn't missed. Always give me the link to the new page, and add it to `RUN.md`.
