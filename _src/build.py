#!/usr/bin/env python3
"""GP & GP (PANTELAS) — builds index.html from _src. Run: python3 _src/build.py"""
import json, os, html as H
S = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(S)
rd = lambda p: open(os.path.join(S, p), encoding='utf-8').read()

TEL1, TEL1F = '+306942222752', '694 222 2752'
TEL2, TEL2F = '+306972812233', '697 281 2233'
MAIL1, MAIL2 = 'pantelasginis@gmail.com', 'pilarinosgeorgios@gmail.com'
VAL = {'TEL1': TEL1, 'TEL1F': TEL1F, 'TEL2': TEL2, 'TEL2F': TEL2F, 'MAIL1': MAIL1, 'MAIL2': MAIL2,
       'VIBER': 'viber://chat?number=%2B306942222752', 'VIBER2': 'viber://chat?number=%2B306972812233',
       'WA': 'https://wa.me/306942222752', 'WA2': 'https://wa.me/306972812233'}

I = {
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 'viber': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M11.4 1.5C9.1 1.5 4.5 1.9 3 4.3 1.8 6 1.6 8.4 1.6 11.2c0 2.9.2 5.6 2.6 7.3v3.1c0 .5.6.8 1 .4l2.7-2.6c1.2.2 2.3.3 3.6.3 2.3 0 6.9-.4 8.4-2.8 1.2-1.7 1.4-4.2 1.4-6.9 0-2.8-.2-5.3-1.4-6.9-1.5-2.4-6.2-2.6-8.5-2.6zm.1 1.8c2 0 5.9.2 7 2 .9 1.3 1 3.3 1 5.7 0 2.3-.1 4.4-1 5.7-1.1 1.8-5 2-7 2-1.2 0-2.3-.1-3.4-.3l-2.3 2.2v-2.8l-.5-.4c-1.8-1.3-2-3.5-2-6.4 0-2.4.1-4.4 1-5.7 1.2-1.8 5.1-2 7.2-2zM9.3 6c-.3 0-.6.1-.9.4-.5.5-.9 1-.8 1.7.3 1.9 1.3 3.6 2.6 5 1.4 1.4 3.1 2.5 5 3 .7.1 1.2-.3 1.6-.8.3-.4.3-.9-.1-1.2l-1.5-1.1c-.4-.3-.9-.2-1.2.1l-.5.5c-1.2-.4-2.3-1.5-2.8-2.8l.5-.5c.3-.3.4-.8.1-1.2L10.2 6.4c-.2-.3-.5-.4-.9-.4zm3.1.4a.4.4 0 0 0 0 .8c2.1.1 3.8 1.8 3.9 3.9a.4.4 0 0 0 .8 0c-.1-2.5-2.2-4.6-4.7-4.7zm.1 1.6a.4.4 0 0 0 0 .8c1.1.1 1.9.9 2 2a.4.4 0 0 0 .8 0c-.1-1.5-1.3-2.7-2.8-2.8z"/></svg>',
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a9.9 9.9 0 0 0-8.5 15l-1.4 5 5.2-1.4A9.9 9.9 0 1 0 12 2zm0 18.1a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.1zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.9 2.9 4.6 4 1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.5-.3z"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3 6 9 7 9-7"/></svg>',
 'sms': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/></svg>',
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'x': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 'taxi': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5h8l1 3H11z"/><path d="M5 18l2.5-7.5A2 2 0 0 1 9.4 9h13.2a2 2 0 0 1 1.9 1.5L27 18"/><rect x="3.5" y="17.5" width="25" height="6.5" rx="2"/><path d="M7 24v2.5M25 24v2.5"/><circle cx="8.5" cy="21" r="1"/><circle cx="23.5" cy="21" r="1"/></svg>',
 'van': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 22V13l4-5h15l6 7v7"/><path d="M3.5 22h25"/><path d="M8 8v6h20M14 8v6M20 8v6"/><circle cx="9" cy="23" r="2.5"/><circle cx="23" cy="23" r="2.5"/></svg>',
 'star': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" aria-hidden="true"><path d="m16 4 3.5 7.6 8.3.9-6.2 5.6 1.8 8.2L16 22.1l-7.4 4.2 1.8-8.2-6.2-5.6 8.3-.9z"/></svg>',
 'wheel': '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><circle cx="16" cy="16" r="12"/><circle cx="16" cy="16" r="3"/><path d="M4.5 13.5c4 1.2 7.5 1.4 11.5 1.4s7.5-.2 11.5-1.4M13.5 18.6 9 26.5M18.5 18.6 23 26.5"/></svg>',
 'car': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 14l2-5.5A2 2 0 0 1 6.9 7h10.2a2 2 0 0 1 1.9 1.5L21 14"/><rect x="2" y="13.5" width="20" height="5" rx="1.6"/><path d="M5 18.5v2M19 18.5v2"/></svg>',
 'user': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>',
 'flip': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8M21 3v5h-5M21 12a9 9 0 0 1-15.5 6.2L3 16M3 21v-5h5"/></svg>',
}
FLAG = {
 'gr': '<svg viewBox="0 0 27 18" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="27" height="18" fill="#0D5EAF"/><path d="M0 3h27M0 9h27M0 15h27" stroke="#fff" stroke-width="2"/><rect width="10" height="10" fill="#0D5EAF"/><path d="M5 0v10M0 5h10" stroke="#fff" stroke-width="2"/></svg>',
 'gb': '<svg viewBox="0 0 60 30" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><clipPath id="fgb"><path d="M0 0v30h60V0z"/></clipPath><g clip-path="url(#fgb)"><path d="M0 0v30h60V0z" fill="#012169"/><path d="M0 0l60 30m0-30L0 30" stroke="#fff" stroke-width="6"/><path d="M0 0l60 30m0-30L0 30" stroke="#C8102E" stroke-width="4"/><path d="M30 0v30M0 15h60" stroke="#fff" stroke-width="10"/><path d="M30 0v30M0 15h60" stroke="#C8102E" stroke-width="6"/></g></svg>',
}
FAQ = [
 ('Είναι όλα τα αυτοκίνητα με οδηγό;', 'Ναι. Ταξί, επταθέσιο και VIP αυτοκίνητα έρχονται πάντα με οδηγό — δεν ενοικιάζουμε αυτοκίνητα χωρίς οδηγό.',
  'Do all cars come with a driver?', 'Yes. Taxi, 7-seater and VIP cars always come with a driver — we do not rent cars without one.'),
 ('Πόσα άτομα χωράει το επταθέσιο;', 'Έως έξι επιβάτες, μαζί με τις αποσκευές τους. Είναι ιδανικό για οικογένειες και παρέες προς το αεροδρόμιο ή για μονοήμερες εκδρομές.',
  'How many people fit in the 7-seater?', 'Up to six passengers, with their luggage. It is ideal for families and groups going to the airport or on day trips.'),
 ('Ποια VIP αυτοκίνητα έχετε;', 'Mercedes, BMW και Audi, πάντα με οδηγό, για επαγγελματικά ραντεβού, εκδηλώσεις, γάμους και ειδικές περιστάσεις.',
  'Which VIP cars do you have?', 'Mercedes, BMW and Audi, always with a driver, for business meetings, events, weddings and special occasions.'),
 ('Έχετε υπερπολυτελή αυτοκίνητα ή αντίκες για γάμο;', 'Ναι. Αποκλειστικά για γάμους διαθέτουμε υπερπολυτελή αυτοκίνητα — Ferrari, Porsche Panamera, Audi Q8 — καθώς και παλιά αυτοκίνητα αντίκες, πάντα με οδηγό.',
  'Do you have super-luxury or vintage cars for weddings?', 'Yes. Exclusively for weddings we have super-luxury cars — Ferrari, Porsche Panamera, Audi Q8 — as well as vintage classic cars, always with a driver.'),
 ('Μπορώ να κλείσω αυτοκίνητο με οδηγό για πολλές ημέρες;', 'Ναι. Μπορείτε να έχετε ιδιωτικό αυτοκίνητο με τον οδηγό του στη διάθεσή σας από 1 ώρα έως 7 ημέρες: ανά ώρα, μονοήμερο, διήμερο, τριήμερο ή ως μία εβδομάδα.',
  'Can I book a car with driver for several days?', 'Yes. You can have a private car with its driver at your disposal from 1 hour up to 7 days: by the hour, for a day, two or three days, or up to a week.'),
 ('Κάνετε διαδρομές εκτός Αθήνας;', 'Ναι. Εκτός από την Αθήνα, τη Νέα Σμύρνη, τον Πειραιά και όλη την Αττική, κάνουμε και μεγάλες διαδρομές — για παράδειγμα αγκαζέ αυτοκίνητο για γάμο στη Θεσσαλονίκη.',
  'Do you travel outside Athens?', 'Yes. Besides Athens, Nea Smyrni, Piraeus and all of Attica, we also do long journeys — for example a reserved car for a wedding in Thessaloniki.'),
 ('Πώς κλείνω μια διαδρομή;', 'Τηλεφωνικά στο 694 222 2752 ή στο 697 281 2233, ή με μήνυμα σε Viber ή WhatsApp. Μπορείτε να ετοιμάσετε το μήνυμα από τη φόρμα «Κράτηση» της σελίδας.',
  'How do I book a ride?', 'By phone on +30 694 222 2752 or +30 697 281 2233, or by message on Viber or WhatsApp. You can prepare the message with the «Book» section of this page.'),
 ('Πηγαίνετε στο αεροδρόμιο και στο λιμάνι;', 'Ναι, στο αεροδρόμιο της Αθήνας και στο λιμάνι του Πειραιά, για αναχωρήσεις και αφίξεις.',
  'Do you go to the airport and the port?', 'Yes, to Athens airport and the port of Piraeus, for departures and arrivals.'),
]
def faq_html():
    o = []
    for q, a, qe, ae in FAQ:
        o.append(f'<details class="rv"><summary><span data-en="{H.escape(qe)}">{H.escape(q)}</span><i aria-hidden="true"></i></summary><p class="a" data-en="{H.escape(ae)}">{H.escape(a)}</p></details>')
    return '\n   '.join(o)

FONTS = [('Noto Serif Display', 300, 'normal', 'noto-serif-display-%s-300-normal'), ('Noto Serif Display', 400, 'normal', 'noto-serif-display-%s-400-normal'),
         ('Noto Serif Display', 400, 'italic', 'noto-serif-display-%s-400-italic'), ('Manrope', 500, 'normal', 'manrope-%s-500-normal'), ('Manrope', 700, 'normal', 'manrope-%s-700-normal')]
UR = {'greek': 'U+0370-0377,U+037A-037F,U+0384-038A,U+038C,U+038E-03A1,U+03A3-03FF',
      'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'}
def fonts_css():
    o = []
    for fam, w, st, f in FONTS:
        for sub in ('greek', 'latin'):
            o.append(f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};font-display:swap;src:url(assets/fonts/{f % sub}.woff2) format('woff2');unicode-range:{UR[sub]}}}")
    # Manrope 800 alias → 700 file (unused), keep 2 weights
    return '\n'.join(o)

def jsonld():
    biz = {'@type': 'LocalBusiness', '@id': '#business', 'name': 'GP & GP', 'alternateName': ['GP&GP', 'GP & GP Taxi · VIP Transfer'],
           'description': 'Ταξί, επταθέσιο για έως 6 επιβάτες και VIP αυτοκίνητα Mercedes, BMW, Audi — όλα με οδηγό. Αθήνα, Νέα Σμύρνη, Πειραιάς, αεροδρόμια, μονοήμερες και πολυήμερες διαδρομές.',
           'telephone': TEL1, 'email': MAIL1, 'address': {'@type': 'PostalAddress', 'addressLocality': 'Αθήνα', 'addressRegion': 'Αττική', 'addressCountry': 'GR'}, 'image': 'assets/img/gp-taxi-vip-metafores-athina-mercedes-akropoli-1800.webp', 'logo': 'assets/img/gp-and-gp-logo.svg',
           'areaServed': [{'@type': 'City', 'name': n} for n in ('Αθήνα', 'Νέα Σμύρνη', 'Πειραιάς')] + [{'@type': 'AdministrativeArea', 'name': 'Αττική'}, {'@type': 'Country', 'name': 'Ελλάδα'}],
           'contactPoint': [{'@type': 'ContactPoint', 'telephone': TEL1, 'contactType': 'reservations', 'availableLanguage': ['el', 'en']},
                            {'@type': 'ContactPoint', 'telephone': TEL2, 'contactType': 'reservations', 'availableLanguage': ['el', 'en']}],
           'knowsAbout': ['Ταξί Αθήνα', 'Ταξί Νέα Σμύρνη', 'Ταξί Πειραιάς', 'Μεταφορά αεροδρόμιο', 'Επταθέσιο ταξί', 'VIP μεταφορές με οδηγό', 'Αυτοκίνητο με οδηγό', 'Αγκαζέ αυτοκίνητο γάμου', 'Υπερπολυτελή αυτοκίνητα για γάμο', 'Αυτοκίνητα αντίκες για γάμο', 'Μονοήμερες εκδρομές'],
           'makesOffer': [{'@type': 'Offer', 'itemOffered': {'@type': 'TaxiService', 'name': n}} for n in ('Ταξί', 'Επταθέσιο έως 6 επιβάτες', 'VIP αυτοκίνητο με οδηγό (Mercedes, BMW, Audi)', 'Ενοικίαση αυτοκινήτου με οδηγό, από 1 ώρα έως 7 ημέρες', 'Αγκαζέ αυτοκίνητο για γάμους και εκδηλώσεις', 'Υπερπολυτελή αυτοκίνητα για γάμους (Ferrari, Porsche Panamera, Audi Q8)', 'Αυτοκίνητα αντίκες για γάμους')]}
    site = {'@type': 'WebSite', '@id': '#website', 'name': 'GP & GP', 'alternateName': ['GP&GP Taxi VIP Transfer'], 'inLanguage': ['el', 'en'], 'publisher': {'@id': '#business'}}
    faq = {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a, *_ in FAQ]}
    return json.dumps({'@context': 'https://schema.org', '@graph': [biz, site, faq]}, ensure_ascii=False)

TITLE = 'Ταξί & VIP μεταφορές με οδηγό Αθήνα | GP & GP'
DESC = 'GP & GP: ταξί, επταθέσιο για έως 6 επιβάτες και VIP Mercedes, BMW, Audi με οδηγό. Αθήνα, Νέα Σμύρνη, Πειραιάς, αεροδρόμια, εκδρομές, πολυήμερα.'

def main():
    body = rd('body.html').replace('</small></small>', '</small>')
    body = body.replace('{{FAQ}}', faq_html())
    for k, v in I.items(): body = body.replace('{{i:%s}}' % k, v)
    for k, v in FLAG.items(): body = body.replace('{{flag:%s}}' % k, v)
    js = rd('script.js')
    for k, v in VAL.items(): body = body.replace('{{%s}}' % k, v); js = js.replace('{{%s}}' % k, v)
    assert '{{' not in body and '{{' not in js, [x for x in body.split('{{')[1:3]]
    css = rd('style.css'); sprite = rd('sprite.html')
    pre = 'assets/fonts/noto-serif-display-greek-300-normal.woff2'
    out = f'''<!DOCTYPE html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{H.escape(TITLE)}</title>
<meta name="description" content="{H.escape(DESC)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<script id="advon-draft-guard">(function(){{var h=location.hostname;if(/(^|\\.)drafts\\.advonmedia\\.com$|\\.github\\.io$|\\.netlify\\.app$/.test(h)){{var m=document.createElement('meta');m.name='robots';m.content='noindex,nofollow';document.head.appendChild(m)}}}})();</script>
<meta name="theme-color" content="#0B0A09">
<meta name="color-scheme" content="light only">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GP &amp; GP">
<meta property="og:title" content="{H.escape(TITLE)}">
<meta property="og:description" content="{H.escape(DESC)}">
<meta property="og:image" content="assets/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ταξί Mercedes της GP &amp; GP με την Ακρόπολη">
<meta property="og:locale" content="el_GR"><meta property="og:locale:alternate" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{H.escape(TITLE)}">
<meta name="twitter:description" content="{H.escape(DESC)}">
<meta name="twitter:image" content="assets/img/og.jpg">
<link rel="preload" href="{pre}" as="font" type="font/woff2" crossorigin>
<link rel="preload" as="image" href="assets/img/gp-taxi-vip-metafores-athina-mercedes-akropoli-1800.webp" imagesrcset="assets/img/gp-taxi-vip-metafores-athina-mercedes-akropoli-1200.webp 1200w, assets/img/gp-taxi-vip-metafores-athina-mercedes-akropoli-1800.webp 1800w, assets/img/gp-taxi-vip-metafores-athina-mercedes-akropoli-2400.webp 2400w" imagesizes="100vw" media="(min-width:701px)">
<script>document.documentElement.classList.add('js')</script>
<style id="advon-fonts">
{fonts_css()}
</style>
<style>
{css}
</style>
<script type="application/ld+json">{jsonld()}</script>
</head>
<body>
{sprite}
{body}
<script>
{js}
</script>
</body>
</html>
'''
    open(os.path.join(R, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html', len(out))

if __name__ == '__main__': main()
