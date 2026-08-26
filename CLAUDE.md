# CLAUDE.md

Context for Claude Code working on this repo.

## What this is

Marketing site for **Arevalo's Auto Repair**, a transmission rebuild shop at
505 E Irving Blvd, Irving, TX 75060. Family-run, 20+ years, one location.

It replaces an abandoned Astro site built by an agency that the owner had no access to.
That old site had hallucinated template copy claiming the shop was in Arevalo, **Spain**,
never once used the word "transmission," and rendered every image as a gray placeholder.
Don't reintroduce any of that.

The business is demand-constrained, not capacity-constrained. Every decision on this site
should serve one goal: **get someone to call 214-718-8587.**

## Stack

Plain static HTML, CSS and vanilla JS. No build step, no framework, no package.json, no
node_modules. This is deliberate — the owner is not a developer and needs to be able to
edit a file and drag a folder onto Netlify.

**Do not add a build system, a framework, or a dependency without being asked.**

```
index.html                 Home
transmission-repair.html   Main money page — Google Ads point here, not at home
fleet.html                 Wholesale / dealer / fleet accounts (B2B growth channel)
services.html              Other services + about
contact.html               Quote form, hours, map
styles.css                 Everything. Tokens at the top under :root
site.js                    Mobile nav + gallery fallback
assets/                    Logo (background stripped) + shop photos
es/                        Full Spanish mirror — see below
build-es.py                Generated the /es pages originally. See warning below.
robots.txt, sitemap.xml
_redirects, vercel.json    Old Astro URLs -> new pages, plus vanity URLs
```

## Business facts — keep these consistent everywhere

Wrong numbers here cost real money and generate bad reviews. One review already
complains about being told a 1-year warranty and getting 6 months.

- Phone: **214-718-8587** (primary, on all listings) and **469-350-6499**
- Email: **arevalostransmission@gmail.com**
- Address: **505 E Irving Blvd, Irving, TX 75060** — Irving, NOT Dallas
- Hours: **Mon–Fri 8:00–6:00, Sat 9:00–4:00, Sun closed**
- Rebuilds start at **$1,400**
- Warranty: **6 months**, parts and labor
- Diagnostic: **free**
- Towing: **free within 15 miles**, when the shop does the major work
- Focus: **Ford, Chevy, Ram** — rebuilt in-house, never junkyard swaps

Phone numbers and address also appear in JSON-LD schema in `index.html` and in
`_redirects`/`sitemap.xml`. Change one, grep for the rest.

## Design system

- Display type: Archivo 800/900, tight tracking. Body: IBM Plex Sans. Data/labels: IBM Plex Mono.
- Palette in `:root` — near-black `--ink`, brand red `--red`, amber accent `--amber`.
- Two signature components:
  - **`.ticket`** — the job-ticket panel. Price, warranty, diagnostic, towing as an
    estimate slip. The terms *are* the pitch, so they sit above the fold.
  - **`.units`** — grid of actual transmission model codes (6R80, 4L60E, 6L80, 68RFE,
    Allison 1000...) with the trucks they're in. This is the highest-value block on the
    site: it signals real expertise to a truck owner and those codes are exactly what
    people type into Google. Don't dilute it into generic service copy.
- Photo components: `figure.shot`, `.steps-media` (sticky photo beside steps),
  `.photoband` (full-bleed with overlaid text), `.pagehead--photo`.
- Every call-to-action must be a real `tel:` link. There's a sticky call bar on mobile.

## Voice

Plain, direct, no marketing gloss. Short sentences. Say the number, name the trade-off.
"It costs more up front than a junkyard swap and it lasts a lot longer. That's the whole
trade." No "Rev up your ride," no "Look no further," no exclamation points.

## Spanish site (`/es/`)

Full mirror, not machine translation. Written for how DFW customers actually talk —
*transmisión, grúa, presupuesto, yonke, patina, no camina*. This matters commercially:
the shop's Facebook posts in Spanish and Spanish keywords are far cheaper to bid on in
this market.

- Each page pairs with its English counterpart via `hreflang` tags. Add a page in one
  language, add it in both, and wire the tags.
- Spanish pages are one folder deep, so asset paths are `../assets/`. There are
  `html[lang="es"]` overrides in `styles.css` for CSS background images.
- Nav labels are longer in Spanish; the header collapses to the menu button earlier.

**`build-es.py` warning:** it generated the Spanish pages initially, but the HTML in
`es/` has been hand-edited since. Re-running it will overwrite that work. Edit the HTML
directly. Delete the script if it's causing confusion.

## Known TODOs

1. **Formspree ID.** `contact.html`, `fleet.html`, `es/contacto.html`,
   `es/flotas-y-mayoreo.html` all contain `YOUR_FORM_ID`. Forms don't deliver until it's
   replaced.
2. **Google review link.** `index.html` and `es/index.html` have a
   `REPLACE_WITH_GOOGLE_REVIEW_LINK` placeholder on the review button.
3. **Reviews need verifying.** The three quotes on the homepage came from third-party
   aggregators, not the shop's own Google profile. They need to be confirmed and replaced
   with exact wording plus real names and dates.
4. **Missing photo:** exterior of the building with signage and street visible. It's the
   shot people use to recognize the place. Would go behind the "One shop. Irving Blvd."
   section and the Contact page header.
5. **Naming.** The sign, the email, the Facebook page and the waiting-room wall all say
   "Arevalo's **Transmission**." Only the website says "Auto Repair." If the owner
   decides to change it, it has to change everywhere at once — site, schema, Google,
   Yelp, Manta, MerchantCircle, Facebook.

## Off-site work that matters more than this repo

The site is where people land; the Google Business Profile is what gets them there.
Listings currently disagree with each other — Yelp and Manta say closed Saturday when the
shop is open 9–4, opening times vary between 8:00, 8:30 and 9:00, and MerchantCircle
carries a different phone number entirely (972-721-7259). Google reads those
inconsistencies as unreliable business data. Google rating is ~4.2 across ~39 reviews;
4.6+ is where the map pack calls start.

If asked about growth, that list and a review campaign beat any code change here.

## Testing

No test suite. Verify visually:

```bash
python3 -m http.server 8000
```

Then check `http://localhost:8000`. Open over HTTP, not `file://` — the Google Maps
embeds are blocked on `file://`.

Before shipping a change, check both languages, both breakpoints (the header collapses at
1080px, phone layout at 760px), and that every `tel:` link and internal link still
resolves.
