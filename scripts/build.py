#!/usr/bin/env python3
"""Builds the Nodly website: the TR/EN landing pages and the legal pages.

Run from the repository root:  python3 scripts/build.py
Legal texts are read from content/legal/*.md (copies of Nodly/legal).
Every page uses relative links, so the site works on a GitHub Pages
subpath (user.github.io/nodly-site/) and on a custom domain alike.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGAL = ROOT / "content" / "legal"

# Page routes, per language. A page's twin in the other language is the
# same key in the other dict.
ROUTES = {
    "en": {"home": "", "privacy": "privacy/", "terms": "terms/", "health": "health/"},
    "tr": {"home": "tr/", "privacy": "tr/gizlilik/", "terms": "tr/kosullar/", "health": "tr/saglik/"},
}

T = {
    "en": dict(
        lang="en", other="tr", switch="Türkçe", switch_label="Türkçe sürüme geç",
        title="Nodly: gentle neck breaks with your AirPods",
        description="Nodly uses your AirPods' motion sensors to guide gentle neck moves and count the reps for you. Motion data stays on your device.",
        h1="Gentle neck breaks for your desk days.",
        lead="Nodly uses your AirPods' motion sensors to follow your head angle, guide each move slowly and count the reps for you. Motion data is processed on your device.",
        cta="Download on the App Store", note="For iPhone and iPad · With compatible AirPods, or without",
        hero_alt="Woman at her desk with AirPods, leaning back and stretching her neck",
        how_e="How it works", how_h="Your first break in three steps.",
        how=[("Put in your AirPods", "Nodly uses the motion sensors in your earbuds. No camera, no extra device."),
             ("Save your starting point", "Look straight ahead and hold still for a few seconds. Nodly takes this as 0°."),
             ("Move slowly", "When you reach the target range, Nodly lets you know with a sound and a tap, and counts the rep for you.")],
        feat_e="What's inside", feat_h="Through the day, as much as you need.",
        feat=[("posture", "Posture Check", "Gently reminds you when your head stays down too long. Start it from the Lock Screen or with Siri.", "Woman with AirPods sitting by a window with her eyes closed"),
              ("breathing", "Breathing and eye breaks", "Short breathing exercises and a two-minute eye break away from the screen. No AirPods needed for these.", "Woman on a sofa breathing slowly with a hand on her chest"),
              ("progress", "Your progress", "Your streak and a desk that gets tidier as you practise. Your history syncs across your devices through iCloud.", "Woman with AirPods and her hands behind her head")],
        trust_e="Privacy and trust", trust_h="Calm, private and honest.",
        trust=[("Stays on your device", "Motion data is processed on your phone and raw motion is never stored. No account needed."),
               ("At your own pace", "Moves should feel slow and comfortable. If something feels off, stop right away. Nodly never pushes you."),
               ("Not a medical device", "Nodly is a wellness app; it doesn't diagnose or treat any condition. If you have a neck condition, check with a health professional before you start.")],
        legal_e="Legal", legal_h="The short version.",
        legal=[("privacy", "Privacy Policy", "No account, and your motion data stays on your device. We collect anonymous usage statistics only if you allow it. No ads, no tracking, no selling of data."),
               ("terms", "Terms of Use", "Nodly is offered as a monthly or yearly subscription, and eligible users get a 7-day free trial. You can cancel any time in your App Store account settings."),
               ("health", "Health & safety", "Move slowly and only within a comfortable range. Stop right away if you feel pain, dizziness or numbness.")],
        more="Read the full text",
        end_h="Take your first break today.", end_s="On the App Store, for iPhone and iPad.",
        disclaimer="Nodly is a wellness app, not a medical device.",
        nav={"privacy": "Privacy", "terms": "Terms", "health": "Health & safety"},
        home="Home", logo_alt="Nodly",
        health_title="Health & safety",
    ),
    "tr": dict(
        lang="tr", other="en", switch="English", switch_label="Switch to English",
        title="Nodly: AirPods ile nazik boyun molaları",
        description="Nodly, AirPods'unuzun hareket sensörleriyle boyun hareketlerinizi yavaşça yönlendirir ve tekrarları sizin yerinize sayar. Hareket verisi cihazınızda kalır.",
        h1="Masa başında boynunuza nazik molalar.",
        lead="Nodly, AirPods'unuzun hareket sensörleriyle başınızın açısını takip eder, hareketleri yavaşça yönlendirir ve tekrarları sizin yerinize sayar. Hareket verisi cihazınızda işlenir.",
        cta="App Store'dan indirin", note="iPhone ve iPad için · Uyumlu AirPods ile, ya da onlarsız",
        hero_alt="Masasında AirPods takarak arkasına yaslanan ve boynunu esneten kadın",
        how_e="Nasıl çalışır", how_h="Üç adımda ilk molanız.",
        how=[("AirPods'unuzu takın", "Nodly kulaklığın hareket sensörlerini kullanır. Kamera ya da ek bir cihaz gerekmez."),
             ("Başlangıç noktanızı kaydedin", "Tam karşıya bakın ve birkaç saniye sabit durun. Nodly bu duruşu 0° olarak alır."),
             ("Yavaşça hareket edin", "Hedef aralığa geldiğinizde Nodly sesle ve titreşimle haber verir, tekrarı sizin yerinize sayar.")],
        feat_e="Neler var", feat_h="Gün boyu, ihtiyacınız kadar.",
        feat=[("posture", "Duruş Takibi", "Başınız uzun süre öne eğik kaldığında nazikçe hatırlatır. Kilit Ekranı'ndan ya da Siri'yle başlatın.", "Pencere kenarında AirPods takmış, gözleri kapalı oturan kadın"),
              ("breathing", "Nefes ve göz molası", "Kısa nefes egzersizleri ve ekrandan uzaklaştıran iki dakikalık göz molası. Bunlar için AirPods gerekmez.", "Kanepede elini göğsüne koyup yavaşça nefes alan kadın"),
              ("progress", "İlerlemeniz", "Seri günleriniz ve pratik yaptıkça toparlanan masanız. Geçmişiniz iCloud ile cihazlarınız arasında eşitlenir.", "Elleri başının arkasında, AirPods takmış kadın")],
        trust_e="Gizlilik ve güven", trust_h="Sakin, özel ve dürüst.",
        trust=[("Cihazınızda kalır", "Hareket verisi telefonunuzda işlenir ve ham hareket kaydı tutulmaz. Hesap açmanız gerekmez."),
               ("Kendi hızınızda", "Hareketler yavaş ve rahat olmalı. Bir şey ters gelirse hemen durun; Nodly sizi asla zorlamaz."),
               ("Tıbbi cihaz değil", "Nodly bir wellness uygulamasıdır; hiçbir rahatsızlığı teşhis etmez ya da tedavi etmez. Boynunuzla ilgili bir rahatsızlığınız varsa önce bir sağlık profesyoneline danışın.")],
        legal_e="Yasal", legal_h="Kısaca bilmeniz gerekenler.",
        legal=[("privacy", "Gizlilik Politikası", "Hesap yok, hareket verileriniz cihazınızdan çıkmaz. Anonim kullanım istatistiklerini yalnızca izin verirseniz toplarız. Reklam, takip ve veri satışı yok."),
               ("terms", "Kullanım Koşulları", "Nodly aylık ya da yıllık abonelikle sunulur; uygun kullanıcılara 7 gün ücretsiz deneme vardır. Aboneliğinizi App Store hesap ayarlarınızdan istediğiniz zaman iptal edebilirsiniz."),
               ("health", "Sağlık ve güvenlik", "Hareketleri yavaş ve yalnızca rahat hissettiğiniz aralıkta yapın. Ağrı, baş dönmesi ya da uyuşma hissederseniz hemen durun.")],
        more="Tamamını okuyun",
        end_h="Bugün ilk molanızı verin.", end_s="iPhone ve iPad için, App Store'da.",
        disclaimer="Nodly bir wellness uygulamasıdır, tıbbi cihaz değildir.",
        nav={"privacy": "Gizlilik", "terms": "Koşullar", "health": "Sağlık ve güvenlik"},
        home="Ana sayfa", logo_alt="Nodly",
        health_title="Sağlık ve güvenlik",
    ),
}

# Replace with the App Store link once the app is live.
APP_STORE_URL = "#"

LEGAL_FILES = {
    ("en", "privacy"): "privacy-policy.md",
    ("en", "terms"): "terms-of-use.md",
    ("tr", "privacy"): "gizlilik-politikasi.md",
    ("tr", "terms"): "kullanim-kosullari.md",
}

e = html.escape


def rel(from_route: str, to_route: str) -> str:
    """Relative link between two routes ('' is the site root)."""
    depth = from_route.count("/")
    return "../" * depth + to_route if (depth or to_route) else "./"


def inline(text: str) -> str:
    """Markdown inline (bold, links) to HTML, escaping everything else."""
    out = e(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"\[(.+?)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', out)
    return out


def markdown(md: str) -> str:
    """The small Markdown subset the legal files use."""
    md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)
    lines = md.split("\n")
    out, para, items, table = [], [], [], []

    def flush():
        nonlocal para, items, table
        if para:
            out.append("<p>" + "<br>".join(inline(x) for x in para) + "</p>")
            para = []
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            items = []
        if table:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table]
            head, body = rows[0], rows[2:]
            t = "<div class=\"table\"><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(t + "</tbody></table></div>")
            table = []

    for raw in lines:
        s = raw.rstrip()
        if s.startswith("|"):
            if para or items:
                flush()
            table.append(s)
            continue
        if table:
            flush()
        if not s.strip():
            flush()
            continue
        m = re.match(r"^(#{1,3}) (.*)", s)
        if m:
            flush()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        if s.startswith("- "):
            if para:
                flush()
            items.append(s[2:])
            continue
        if items:
            flush()
        para.append(s)
    flush()
    return "\n".join(out)


def health_html(lang: str) -> str:
    md = (LEGAL / "saglik-feragatnamesi.md").read_text()
    section = md.split("## 1.")[1].split("## 2.")[0]
    col = 2 if lang == "tr" else 3
    rows = [[c.strip() for c in r.split("|")] for r in section.split("\n") if r.startswith("| Paragraf")]
    body = "".join(f"<p>{inline(r[col])}</p>" for r in rows)
    return f"<h1>{e(T[lang]['health_title'])}</h1>\n{body}"


def head(lang: str, route: str, key: str, title: str, description: str) -> str:
    t = T[lang]
    a = rel(route, "assets/")
    other = T[lang]["other"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#E4EEEC" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#103836" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{a}favicon.png">
<link rel="apple-touch-icon" href="{a}icon-180.png">
<link rel="alternate" hreflang="{other}" href="{rel(route, ROUTES[other][key])}">
<link rel="stylesheet" href="{a}style.css">
</head>
<body>
<header class="bar">
  <div class="wrap bar-inner">
    <a class="brand" href="{rel(route, ROUTES[lang]['home'])}"><img src="{a}logo.svg" alt="" width="40" height="24"><span>Nodly</span></a>
    <a class="switch" href="{rel(route, ROUTES[other][key])}" hreflang="{other}" lang="{other}" aria-label="{e(t['switch_label'])}">{e(t['switch'])}</a>
  </div>
</header>
"""


def footer(lang: str, route: str) -> str:
    t = T[lang]
    links = " ".join(f'<a href="{rel(route, ROUTES[lang][k])}">{e(v)}</a>' for k, v in t["nav"].items())
    return f"""<footer class="foot">
  <div class="wrap">
    <p class="disclaimer">{e(t['disclaimer'])}</p>
    <nav class="foot-links">{links}</nav>
    <p class="copy">© 2026 Nodly</p>
  </div>
</footer>
</body>
</html>
"""


def landing(lang: str) -> str:
    t = T[lang]
    route = ROUTES[lang]["home"]
    a = rel(route, "assets/")
    steps = "".join(
        f'<li class="step"><span class="num" aria-hidden="true">{i}</span><h3>{e(h)}</h3><p>{e(p)}</p></li>'
        for i, (h, p) in enumerate(t["how"], 1))
    cards = "".join(
        f'<article class="card"><img src="{a}img/{img}.jpg" alt="{e(alt)}" loading="lazy" width="1400" height="939"><div class="card-body"><h3>{e(h)}</h3><p>{e(p)}</p></div></article>'
        for img, h, p, alt in t["feat"])
    trust = "".join(f'<div class="point"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in t["trust"])
    legal = "".join(
        f'<div class="point"><h3>{e(h)}</h3><p>{e(p)}</p><a class="more" href="{rel(route, ROUTES[lang][k])}">{e(t["more"])} <span aria-hidden="true">→</span></a></div>'
        for k, h, p in t["legal"])
    return head(lang, route, "home", t["title"], t["description"]) + f"""<main>
<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <h1>{e(t['h1'])}</h1>
      <p class="lead">{e(t['lead'])}</p>
      <a class="button" href="{APP_STORE_URL}">{e(t['cta'])}</a>
      <p class="note">{e(t['note'])}</p>
    </div>
    <img class="hero-img" src="{a}img/hero.jpg" alt="{e(t['hero_alt'])}" width="1400" height="939">
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">{e(t['how_e'])}</p>
    <h2>{e(t['how_h'])}</h2>
    <ol class="grid3 steps">{steps}</ol>
  </div>
</section>

<section class="section tinted">
  <div class="wrap">
    <p class="eyebrow">{e(t['feat_e'])}</p>
    <h2>{e(t['feat_h'])}</h2>
    <div class="grid3">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">{e(t['trust_e'])}</p>
    <h2>{e(t['trust_h'])}</h2>
    <div class="grid3 points">{trust}</div>
  </div>
</section>

<section class="section tinted">
  <div class="wrap">
    <p class="eyebrow">{e(t['legal_e'])}</p>
    <h2>{e(t['legal_h'])}</h2>
    <div class="grid3 points plain">{legal}</div>
  </div>
</section>

<section class="end">
  <div class="wrap">
    <img src="{a}logo-white.svg" alt="" width="96" height="57">
    <h2>{e(t['end_h'])}</h2>
    <p>{e(t['end_s'])}</p>
    <a class="button light" href="{APP_STORE_URL}">{e(t['cta'])}</a>
  </div>
</section>
</main>
""" + footer(lang, route)


def legal_page(lang: str, key: str) -> str:
    t = T[lang]
    route = ROUTES[lang][key]
    body = health_html(lang) if key == "health" else markdown((LEGAL / LEGAL_FILES[(lang, key)]).read_text())
    title = f"{t['nav'][key]} · Nodly"
    return head(lang, route, key, title, t["description"]) + f"""<main class="doc">
  <div class="wrap narrow">
    <a class="back" href="{rel(route, ROUTES[lang]['home'])}"><span aria-hidden="true">←</span> {e(t['home'])}</a>
    <article>
{body}
    </article>
  </div>
</main>
""" + footer(lang, route)


def write(route: str, content: str) -> None:
    path = ROOT / route / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    print("wrote", path.relative_to(ROOT))


def main() -> None:
    for lang in ("en", "tr"):
        write(ROUTES[lang]["home"], landing(lang))
        for key in ("privacy", "terms", "health"):
            write(ROUTES[lang][key], legal_page(lang, key))


if __name__ == "__main__":
    main()
