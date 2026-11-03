---
name: pm-5-visual-design
description: "Turn the agreed solution detail into a visual design: polished static images of the key screens, product only, one screen shown first. Use when producing or changing the visual design, before anything clickable."
---

# Visual design

Input: `solution-detail.md` (agreed) and the design principles in `pm-4-solution-detail`. Output: `runs/run-N/visual-design.md` with images, agreed with the user before `pm-6-clickable-prototype`.

## Look
- Clean B2B SaaS: generous spacing, clear hierarchy, consistent components, restrained colour
- Looks like part of their product: copy conventions from real product screenshots, and real brand values from the source, never guessed
- Accessible: never colour alone, visible focus, works in light and dark and on a phone
- A page shared outside the company doesn't present itself as the company's product

## Visual design (`visual-design.md`)
Key screens as polished, realistic static images, not clickable:
- Real content: their actual question, real numbers from code, their terms
- The happy path, plus the one screen that matters most for trust (e.g. the review screen, or a failure being caught)
- Made in Figma when connected, otherwise a static HTML mock rendered to PNG
- **One screen first.** Make the most important screen (usually the answer), show it, and make the others while the user reviews it. Their feedback on it shapes the rest
- **The images show only the product, exactly as the user would see it.** No annotations, numbered markers, side notes, "screen 1 of 3" labels, pain call-outs, design-check results or review comments. Reasoning goes in `visual-design.md`, never in the image
- `visual-design.md`: the images, the reasoning for each screen, brand values and their source
- Agree all of them with the user before building anything clickable. Cheap to change now, expensive later
