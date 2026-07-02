# AGENTS.md — Slide style library

This folder is a **slide component library**. It holds five self-contained
visual *styles*; each style ships the same set of building blocks so you can
assemble a 1280×720 (16:9) slide deck by picking a style and dropping in
ready-made slide templates.

Read this file before generating slides from `resources/slides/`.

```
resources/slides/
├── AGENTS.md            ← you are here
└── styles/
    ├── base.css         ← shared FOUNDATION (reset, 1280×720 canvas, preview, print, reduced-motion) — linked first by every slide
    ├── base.js          ← optional DECK/PREVIEW runtime (fit-to-window + keyboard nav) — include in a viewer
    ├── minimalist/      ┐
    ├── corporate/       │  one folder per style, identical file layout
    ├── editorial/       │  (see "Anatomy of a style folder")
    ├── bold-modern/     │
    └── playful/         ┘
```

---

## 1. Pick a style

Choose **one** style folder for the whole deck (don't mix styles in one deck).
Use this table to map intent → style:

| Style          | Personality                                   | Reach for it when…                                            |
|----------------|-----------------------------------------------|---------------------------------------------------------------|
| `minimalist`   | Near-monochrome, hairlines, lots of whitespace | Calm, focused, content-first decks; one idea per slide        |
| `corporate`    | Navy + blue, structured grid, KPI panels       | Business reviews, investor/board decks, financial reporting   |
| `editorial`    | Cream paper, serif (Playfair), drop caps       | Long-form narrative, thought-leadership, magazine feel        |
| `bold-modern`  | Near-black, vivid gradient, huge bold type     | Product launches, keynotes, "wow" moments                     |
| `playful`      | Bright crayon palette, rounded, blobs          | Workshops, education, demos, anything that should feel fun    |

The **folder name is the style selector** — once you've chosen, everything you
need lives inside that one folder plus the two shared `base.*` files.

---

## 2. Anatomy of a style folder

Every style contains exactly these 13 files. The **filename tells you what each
one is — you should not need to open a file to choose the right one.**

```
<style>/
├── css/
│   ├── theme-tokens.css     CSS variables: palette, spacing, radius (the "skin")
│   ├── typography.css       font families, weights, and slide-scale type sizes
│   ├── slide-layouts.css    the 1280×720 .slide canvas + layout helpers
│   └── components.css       reusable pieces: cards, bullets, badges, dividers…
├── html/
│   ├── cover-title-slide.html       opening / title slide
│   ├── section-divider-slide.html   chapter / agenda break
│   ├── bulleted-list-slide.html     heading + bullet list
│   ├── two-column-slide.html        side-by-side comparison
│   ├── big-number-stat-slide.html   one hero metric (animated count-up)
│   └── quote-slide.html             pull quote + attribution
└── js/
    ├── entrance-animations.js   animates [data-animate] elements on load
    ├── count-up-numbers.js      animates [data-countup] figures from 0
    └── decor-background.js      injects the style's signature background chrome
```

The taxonomy is identical across all five styles. To switch a deck's look,
point at a different style folder — the filenames and markup stay the same.

---

## 3. How to use a style — the fast path

Each `html/*.html` file is a **complete, standalone slide document**. To build a
slide:

1. Copy the template whose name matches the slide type you need (e.g.
   `quote-slide.html` for a quote).
2. Replace the placeholder copy with the real content. Keep the existing
   classes and `data-*` attributes (see §4 and §5) — they drive layout and
   motion.
3. Repeat for each slide, using templates from **the same style folder**.

A slide's `<head>` already links its dependencies in the correct order:

```html
<link rel="stylesheet" href="../../base.css">          <!-- shared foundation -->
<link rel="stylesheet" href="../css/theme-tokens.css"> <!-- skin first -->
<link rel="stylesheet" href="../css/typography.css">
<link rel="stylesheet" href="../css/slide-layouts.css">
<link rel="stylesheet" href="../css/components.css">
```

and pulls the behavior at the end of `<body>`:

```html
<script src="../js/decor-background.js"></script>
<script src="../js/entrance-animations.js"></script>
<!-- only on slides with animated numbers: -->
<script src="../js/count-up-numbers.js"></script>
```

> **Load order matters:** `theme-tokens.css` must come before the others (it
> defines the variables they consume). Keep the order above.

---

## 4. Shared vocabulary (works in every style)

Use these classes/attributes and the chosen style decides how they look. This
is what makes markup portable between styles.

**Layout** (`slide-layouts.css`)
- `.slide` — the 1280×720 canvas. One per file.
- `.slide--center` — vertically center the content.
- `.stack` / `.stack--tight` — vertical flex stack (normal / tighter gap).
- `.grid-2` — two-column grid.
- `.row` — horizontal flex row. `.fill` — height:100%. `.spacer` — flex filler.

**Text** (`typography.css`)
- `.kicker` — small eyebrow label above a title.
- `.title` — the slide headline. `.subtitle` — supporting line.
- `.body` — paragraph/body copy. `.caption` — small print / attribution.
- `.stat-number` — the big hero figure on a stat slide.
- `.quote-text` — large quotation text.

**Lists** (`components.css`)
- `.bullets` — a `<ul>` with the style's bullet markers.

---

## 5. Behavior contracts (`data-*` attributes)

The JS is **declarative** — it scans the DOM for attributes. Add the attribute,
get the behavior; no per-slide wiring.

- `data-animate` — put it on any element to give it the style's entrance
  motion (staggered in DOM order). `entrance-animations.js` handles it.
- `data-countup="<number>"` — on a `.stat-number`, animates from 0 to the
  number. Optional `data-prefix` and `data-suffix` wrap the value.
  `count-up-numbers.js` handles it. Examples actually used in the templates:
  ```html
  <span class="stat-number" data-countup="98"   data-suffix="%">0%</span>
  <span class="stat-number" data-countup="142"  data-prefix="$" data-suffix="M">$0M</span>
  <span class="stat-number" data-countup="9000" data-suffix="+">0+</span>
  ```
  Put the **final/fallback text** as the element's initial content (e.g.
  `0%`) so the slide still reads correctly if scripts don't run.

The animation *timing and easing differ per style* (minimalist is calm,
bold-modern springs, playful bounces) but the attributes are identical — so you
write the same markup regardless of style.

`decor-background.js` needs no attributes: it injects the style's signature
background (e.g. corporate's top bar, editorial's rules, bold-modern's gradient
orbs, playful's blobs) into every `.slide` automatically.

---

## 6. Style-specific components

Beyond the shared vocabulary, each style adds a few pieces of its own (defined
in that style's `components.css`). Use them only within their style:

- **minimalist:** `.divider`, `.divider--ink`, `.num-list`, `.card`, `.folio`, `.brandmark`
- **corporate:** `.panel`, `.kpi` + `.kpi-grid`, `.badge`, `.slide-no`, `.brandmark`
- **editorial:** `.dropcap`, `.pullquote`, `.byline`, `.running-head`, `.folio`, `.columns`, `.divider--crimson`
- **bold-modern:** `.chip`, `.card` + `.card--gradient`, `.underline-gradient`, `.gradient-text`, `.divider--gradient`
- **playful:** `.badge-pill` (`--teal`/`--yellow`/`--purple`), `.card` (`--coral`/`--teal`/`--yellow`/`--purple`), `.tilt-left`/`.tilt-right`, `.highlight`

If you need a piece that isn't there, prefer composing from the shared classes
over inventing new CSS.

---

## 7. Two ways to render

**A. Served / opened as files (default).** The relative `../css/` and `../js/`
links resolve when the HTML is opened from disk or served from this folder.
Nothing else to do.

**B. Rendered from an HTML string** (e.g. a tool that takes raw HTML and does
*not* resolve relative paths). Inline the dependencies before rendering: paste
`base.css` followed by the four `css/*.css` files (in the order in §3) into a
single `<style>` in the `<head>`, and the needed `js/*.js` into `<script>` tags
before `</body>`.
Everything is plain CSS/JS with no build step, so inlining is a copy-paste.

---

## 8. Customizing / reskinning

- **Recolor or respace a whole style:** edit only its `theme-tokens.css`. All
  templates and components read from those variables.
- **Change type:** edit `typography.css` (families live in the `:root` block at
  the top).
- **`base.css` — shared foundation (auto-linked first by every slide):** the
  CSS reset, the universal 1280×720 `.slide` canvas geometry, browser-preview
  ergonomics (centers slides on a neutral backdrop, only when the window is
  bigger than a slide), PDF `@page` sizing, and a `prefers-reduced-motion`
  guard. Strictly style-agnostic (no palette, no fonts) and a style's CSS loads
  after, so it can override anything here. Put genuinely cross-style rules here.
- **`base.js` — optional deck/preview runtime:** include it in a viewer
  document (or add `data-deck` to `<body>`) to scale the fixed canvas to fit the
  window and get keyboard navigation across multiple slides. Render-safe (a
  no-op at a native 1280×720 viewport); not required for single-slide files.
- Keep edits inside the chosen style folder so other styles are unaffected.

---

## 9. Rules of thumb

- One style per deck; one `.slide` per HTML file.
- Reuse the shared classes and `data-*` attributes; don't hand-roll motion or
  layout that a class already provides.
- Author type at slide scale (titles ~48–92px, body ~22–26px) — these are
  full-screen slides, not web pages.
- Always leave readable fallback text inside `data-countup` elements.
- Don't rename the files: the names are the catalogue agents select from.

---

## 10. The `data-slot` contract (for the Deck Assembler)

Each bundled HTML template carries `data-slot="<name>"` attributes on the
elements that the Deck_Assembler fills with content. These anchors tell the
assembler *where* to place each piece of slide content; they are invisible to
the browser (they don't affect rendering or behavior) and are stripped from the
final assembled output.

### Slot vocabulary by slide type

| Template | Slots |
|----------|-------|
| `cover-title-slide.html` | `kicker`, `title`, `subtitle` |
| `section-divider-slide.html` | `kicker`, `figure`, `title` |
| `bulleted-list-slide.html` | `kicker`, `title`, `bullets` |
| `two-column-slide.html` | `kicker`, `title`, `left-heading`, `left-body`, `right-heading`, `right-body` |
| `big-number-stat-slide.html` | `kicker`, `value`, `label` |
| `quote-slide.html` | `quote`, `attribution` |

### Page numbers: the `data-folio` marker

A page-number element (a folio / slide number) can opt into automatic
numbering by carrying a `data-folio` attribute: the assembler overwrites its
text with the slide's 1-based position in the deck (zero-padded to two digits,
e.g. `01`, `02`, … `12`) and then strips the attribute. Don't rely on a
hard-coded literal — annotate the element with `data-folio` and let the
assembler number it, so single-slide and reordered decks stay correct.

### Rules for custom styles

When creating or editing a custom style's templates, **keep the `data-slot`
attributes on the appropriate elements** — they are how the assembler knows
where to place content. Removing or renaming them will prevent the style from
being assembled.

Custom-style creation seeds `minimalist` verbatim, so the attributes are already
in place. If you restructure a template's markup, move the `data-slot` to
whichever element should receive that content.
