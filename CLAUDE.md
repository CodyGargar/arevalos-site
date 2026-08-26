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
site.js                    Mobile nav, gallery fallback, call/lead tracking
assets/                    Logo (background stripped) + shop photos
es/                        Full Spanish mirror — see below
404.html                   Not-found page. Has the phone number on it, on purpose.
thanks.html, es/gracias.html   Post-submit pages the forms redirect to
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
  Confirmed correct by the owner on 2026-08-26. The site and the JSON-LD schema are
  right. The placard on the building is the thing that is out of date — see TODO 5.
- Rebuilds start at **$1,400**
- Warranty: **6 months**, parts and labor
- Diagnostic: **free**
- Towing: **free within 15 miles**, when the shop does the major work
- Focus: **Ford, Chevy, Ram** — rebuilt in-house, never junkyard swaps
- Google Business Profile CID: **8593300856004174944**
  (`https://www.google.com/maps?cid=8593300856004174944`)
- The owner appears in reviews as **Eric / Erick**; techs named are Ricky, Alvarez, Francisco

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

## Measurement

The conversion is a phone call, not a pageview. `site.js` records every `tel:` tap,
`mailto:` click, directions click and form submit, tagged with the page region it
happened in (`sticky_call_bar`, `header`, `ticket_panel`, `footer`...) and the page
language — so "are the Spanish pages producing calls?" is answerable.

It is switched off until someone sets `ANALYTICS_ID` (a GA4 `G-XXXXXXXXXX`) at the top
of `site.js`. Empty means genuinely inert: no script, no request, no cookie. One edit
point, not a snippet pasted into ten files.

**Ads cannot be measured without the second step:** import `call_click` and
`generate_lead` as conversions in Google Ads (Tools → Conversions → Import from GA4).
Don't spend on ads before that's done.

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

The Spanish pages were originally generated by a `build-es.py` script. It was deleted
once the HTML diverged from it by hand — it could only overwrite good work. Edit the
HTML in `es/` directly. (The script is still in git history at commit 99d9dfd if it's
ever needed.)

## Known TODOs

1. **GA4 Measurement ID.** `site.js` has `var ANALYTICS_ID = ''`. Until it's filled in
   nothing is measured, and the Google Ads plan in the README can't work. See
   **Measurement** above.
2. **Formspree ID.** `contact.html`, `fleet.html`, `es/contacto.html`,
   `es/flotas-y-mayoreo.html` all contain `YOUR_FORM_ID`. Forms don't deliver until it's
   replaced. Each of those four pages currently shows a `.formnote` callout telling
   visitors to call instead — **delete those four blocks and the `.formnote` rule in
   `styles.css` the moment the real ID goes in.**
3. **No website link on the Google Business Profile.** The profile literally offers
   "Add website" — there is no URL on it at all. Nothing else on this list moves as many
   calls as fixing that. Point it at `/transmission-repair.html`.
4. **Google review link — short version still wanted.** The review button now points at
   the verified canonical profile URL, `https://www.google.com/maps?cid=8593300856004174944`.
   That works. The short `https://g.page/r/.../review` link from the Business Profile
   dashboard opens the star picker directly and converts better — swap it into
   `index.html` and `es/index.html` when you have it.
5. **Homepage reviews are now verbatim from Google** (read 2026-08-26) with real
   reviewer names: Texas Topline Motors, Carlos Choto, Steve Cox on `index.html`;
   Khris Nino (original Spanish) plus two marked `traducido` on `es/index.html`.
   Google only exposes relative dates, so no dates are cited — add real ones if you pull
   them from the dashboard. **Never paraphrase a review and attribute it to Google.**
6. **The sign on the building has the wrong hours.** Nothing to change in this repo —
   the site and the schema are correct and owner-confirmed. The physical placard,
   visible in `assets/shopexterior.jpg`, reads **Monday–Friday 9:30 AM – 6:00 PM** and
   lists **no Saturday at all**. The shop actually opens at 8:00 and is open Saturday
   9:00–4:00.

   That is 90 minutes of every weekday morning plus the whole of Saturday during which
   a passer-by believes the shop is shut. For a demand-constrained shop on a main road,
   a new placard costs less than one rebuild. Google also cross-checks what the
   storefront says against the profile, so it feeds the listing problem below.
7. **Naming — there are three variants, not two.** The building sign reads
   **"Arevalo's Auto & Transmission"** (confirmed from `assets/shopexterior.jpg`), the
   waiting-room wall reads **"Arevalo's Transmission"**, and the website, all 13 page
   titles, the schema, the email and the domain say **"Arevalo's Auto Repair."**
   If the owner picks one, it has to change everywhere at once — site, schema, the two
   physical signs, Google, Yelp, Manta, MerchantCircle, Facebook.

**Done, kept here so it is not re-opened:** the shop exterior photo that used to be
listed as missing is in as `assets/shopexterior.jpg`, behind the "One shop. Irving Blvd."
section on both homepages and as the Contact page header and social card.

## Off-site work that matters more than this repo

The site is where people land; the Google Business Profile is what gets them there.
Listings currently disagree with each other — Yelp and Manta say closed Saturday when the
shop is open 9–4, opening times vary between 8:00, 8:30 and 9:00, and MerchantCircle
carries a different phone number entirely (972-721-7259). Google reads those
inconsistencies as unreliable business data. Google rating is **4.4 across 36 reviews**
(verified on the profile 2026-08-26); 4.6+ is where the map pack calls start. Google
categorises the shop as **"Mechanic"** — it should be **Transmission Shop**.

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
