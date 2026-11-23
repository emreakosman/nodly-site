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
    "en": {"home": "", "privacy": "privacy/", "terms": "terms/", "health": "health/", "support": "support/"},
    "tr": {"home": "tr/", "privacy": "tr/gizlilik/", "terms": "tr/kosullar/", "health": "tr/saglik/", "support": "tr/destek/"},
}

# The support page App Store Connect needs as the Support URL. Markdown,
# rendered with the same converter as the legal texts.
SUPPORT = {
    "en": """# Support

Have a question or something isn't working? Write to us at **{{EMAIL}}** and we'll reply as soon as we can, usually within two business days. If it's about your subscription, include the anonymous ID shown in the app under Settings › Support, so we can find the right record.

## Subscription

### Cancel your subscription
Open iOS Settings › [your name] › Subscriptions, choose Nodly and tap Cancel Subscription. You can also get there from Settings › Manage Subscription in the app. You keep access until the end of the current period.

### Restore your purchases
On a new device or after reinstalling, sign in with the same Apple Account and tap Restore Purchases on the subscription screen in the app.

### Ask for a refund
Purchases are made through Apple, so refunds are handled by Apple. Request one at [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Frequently asked questions

### Which AirPods work with Nodly?
Nodly needs AirPods with motion sensors: AirPods Pro, AirPods Max and AirPods (3rd generation) or later. When you start an exercise, the app checks whether your connected headphones are supported and tells you if they aren't.

### Can I use Nodly without AirPods?
Yes. Neck exercises can run on a timer without AirPods; Nodly then guides the pace but doesn't measure your movement. Breathing exercises, the eye break and the under-desk exercises never need AirPods.

### Where is my data, and how do I delete it?
Motion data is processed on your device and never leaves it. To delete your exercise history, go to Settings › Delete session history in the app. Deleting the app removes the rest; to delete the iCloud copy too, go to iOS Settings › [your name] › iCloud › Manage Account Storage › Nodly. More in the [Privacy Policy](../privacy/).

### Is Nodly a medical app?
No. Nodly is a wellness app, not a medical device. If you have a neck condition, check with a health professional before you start. See [Health & safety](../health/).
""",
    "tr": """# Destek

Bir sorunuz mu var, ya da bir şey çalışmıyor mu? **{{EMAIL}}** adresine yazın; genellikle iki iş günü içinde yanıtlarız. Konu aboneliğinizle ilgiliyse, kaydınızı bulabilmemiz için uygulamada Ayarlar › Destek bölümünde görünen anonim kimliği de ekleyin.

## Abonelik

### Aboneliği iptal etmek
iOS Ayarlar › [adınız] › Abonelikler bölümünü açın, Nodly'yi seçin ve Aboneliği İptal Et'e dokunun. Uygulamadaki Ayarlar › Aboneliği Yönet bölümünden de aynı yere ulaşabilirsiniz. Erişiminiz mevcut dönemin sonuna kadar sürer.

### Satın alımları geri yüklemek
Yeni bir cihazda ya da uygulamayı yeniden yükledikten sonra aynı Apple Hesabı ile giriş yapın ve uygulamadaki abonelik ekranında Satın Alımları Geri Yükle'ye dokunun.

### İade istemek
Satın alımlar Apple üzerinden yapıldığı için iadeleri Apple yönetir. Talebinizi [reportaproblem.apple.com](https://reportaproblem.apple.com) adresinden iletebilirsiniz.

## Sık sorulan sorular

### Hangi AirPods modelleri Nodly ile çalışır?
Nodly için hareket sensörlü AirPods gerekir: AirPods Pro, AirPods Max ve AirPods (3. nesil) ve sonrası. Bir egzersize başladığınızda uygulama bağlı kulaklığınızın uyumlu olup olmadığını kontrol eder ve uyumlu değilse size söyler.

### Nodly'yi AirPods olmadan kullanabilir miyim?
Evet. Boyun egzersizleri AirPods olmadan, süreyle de yapılabilir; bu durumda Nodly temposu yönlendirir ama hareketinizi ölçmez. Nefes egzersizleri, göz molası ve masa altı egzersizleri için AirPods hiç gerekmez.

### Verilerim nerede, nasıl silerim?
Hareket verisi cihazınızda işlenir ve cihazınızdan çıkmaz. Egzersiz geçmişinizi silmek için uygulamada Ayarlar › Oturum geçmişini sil'e dokunun. Uygulamayı silmek geri kalanını kaldırır; iCloud'daki kopyayı da silmek için iOS Ayarlar › [adınız] › iCloud › Hesap Depolamasını Yönet › Nodly yolunu izleyin. Ayrıntılar için [Gizlilik Politikası](../gizlilik/).

### Nodly bir tıbbi uygulama mı?
Hayır. Nodly bir wellness uygulamasıdır, tıbbi cihaz değildir. Boynunuzla ilgili bir rahatsızlığınız varsa başlamadan önce bir sağlık profesyoneline danışın. Bkz. [Sağlık ve güvenlik](../saglik/).
""",
}


T = {
    "en": dict(
        lang="en", other="tr", switch_label="Türkçe sürüme geç",
        title="Nodly: short breaks for your neck, posture and the rest of you",
        description="Short exercises for your neck, breath, eyes, hands, legs and desk yoga. With your AirPods, Nodly measures your neck moves and reminds you when your head stays down. Motion data stays on your device.",
        h1="Gentle breaks for your desk days.",
        lead="Short exercises for your neck, breath, eyes, hands and legs, and desk yoga. With your AirPods, Nodly measures your neck moves, follows your posture and lets you know when your head stays down too long.",
        cta="Download on the App Store", note="For iPhone and iPad · With compatible AirPods, or without",
        nav_links=[("areas", "Exercises"), ("measure", "How it works"), ("posture", "Posture Check"), ("progress", "Progress")],
        gauge=dict(side_r="Right", side_l="Left", back="Back to center", reached="Target reached"),
        screen_alt="Nodly's exercise screen: a turn to the right measured at 51°, rep 1 of 5",
        chips=["Neck", "Posture", "Breathing", "Eye break"],
        areas_e="Not just your neck", areas_h="Six areas, a few minutes each.",
        areas=[("neck", "Neck", "Turns, side tilts, looking down and up, chin tucks. AirPods measure the angle and count reps; without them, Nodly paces you on a timer."),
               ("breath", "Breathing", "Long exhale, box breathing and even breathing, for 1, 2 or 3 minutes, paced by a drawing and a soft tap."),
               ("eyes", "Eyes", "A two-minute break away from the screen: look far away, blink slowly, then rest with your eyes closed."),
               ("hands", "Hands and wrists", "Wrist stretches, wrist circles and opening and closing your hands, for days spent on a keyboard and mouse."),
               ("legs", "Under the desk", "Heel raises, toe raises, knee extensions and seated marching, without leaving your chair."),
               ("yoga", "Desk yoga", "Seated cat-cow, side bend and twist, plus shoulder moves to loosen up between meetings.")],
        areas_note="Only neck tracking uses AirPods. Everything else works without them.",
        measure_e="Measured with your AirPods", measure_h="Nodly tells you when you're there.",
        measure_p="The motion sensors in your earbuds follow your head angle. When you reach the target range, Nodly lets you know with a sound and a tap and counts the rep for you. Targets adapt to your own range of motion.",
        demo_label="Try it: turn your head", demo_hint="Drag to the right until you reach the green range, then come back to center.",
        demo_reps="Reps", demo_angle="Head angle",
        how=[("Put in your AirPods", "Nodly uses the motion sensors in your earbuds. No camera, no extra device."),
             ("Save your starting point", "Look straight ahead and hold still for a few seconds. Nodly takes this as 0°."),
             ("Move slowly", "When you reach the target range, Nodly lets you know with a sound and a tap, and counts the rep for you.")],
        posture_e="Posture Check", posture_h="A gentle reminder when your head drops.",
        posture=[("desk", "At the desk", "Follows your head while you work, for 30 minutes up to 2 hours, or in Pomodoro rounds of 25 minutes' work and 5 minutes' rest."),
                 ("workout", "During a workout", "If your head drops during standing exercises, Nodly lets you know within seconds. For exercises done lying down, just pause it."),
                 ("lock", "On the Lock Screen", "Lock your phone and keep working. You see the time left on the Lock Screen and pause or end from there."),
                 ("quick", "Start it your way", "With Siri, from Control Center, or with a Focus automation in Shortcuts.")],
        siri="“Start posture check with Nodly”",
        toast="Just lift your gaze straight ahead.",
        today_alt="Nodly's Today screen with Posture Check: At the desk and Working out",
        pomodoro_alt="Posture Check running in Pomodoro mode: 24:58 left in round 1 of 4, your head is upright",
        routines_e="Routines", routines_h="Ready-made routines, or your own order.",
        routines_p="Start with a ready-made routine like Day Opener or Screen Break, or pick moves from the library and put them in your own order. For you on the Today screen suggests one that suits your day and your busiest hours.",
        routine_name="Quick Break", routine_meta="4 exercises · 6 min",
        routine_steps=[("breath", "Long exhale"), ("neck", "Turn Left & Right"), ("neck", "Chin tucks"), ("legs", "Heel raises")],
        suggest=["Day Opener", "Screen Break", "Wrist Break", "Desk Yoga", "Day's End"],
        progress_e="Progress", progress_h="Small steps you can see adding up.",
        progress_p="Your streak, your week, and how your time splits across your neck, breath, eyes, hands and legs, at a glance. And as you practise, a little 3D desk tidies itself up.",
        streak="day streak", week=["M", "T", "W", "T", "F", "S", "S"], areas_title="This week by area",
        bars=[("Neck", 86), ("Breathing", 64), ("Eyes", 42), ("Hands", 30), ("Legs", 52)],
        details_e="The details", details_h="Fits into your day.",
        details=[("cloud", "Synced through iCloud", "Your history and routines sync across your iPhone and iPad through your own iCloud."),
                 ("nopods", "Without AirPods, too", "Neck exercises can run on a timer. The other exercises never need AirPods."),
                 ("bell", "Reminders you choose", "A daily reminder, desk breaks through your busy hours and a weekly summary, each one optional."),
                 ("voice", "Guided by sound", "Spoken cues, sounds and haptics guide you, so your eyes can stay off the screen."),
                 ("a11y", "Made for everyone", "Dynamic Type, VoiceOver and Reduce Motion, on iPhone and iPad."),
                 ("globe", "Six languages", "English, Turkish, German, Spanish, French and Japanese.")],
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
        nav={"privacy": "Privacy", "terms": "Terms", "health": "Health & safety", "support": "Support"},
        home="Home", logo_alt="Nodly",
        health_title="Health & safety",
    ),
    "tr": dict(
        lang="tr", other="en", switch_label="Switch to English",
        title="Nodly: boynunuz, duruşunuz ve bedeniniz için kısa molalar",
        description="Boyun, nefes, göz, el, bacak ve masa başı yoga için kısa egzersizler. Nodly, AirPods'unuzla boyun hareketlerinizi ölçer ve başınız önde kaldığında hatırlatır. Hareket verisi cihazınızda kalır.",
        h1="Masa başında geçen güne nazik molalar.",
        lead="Boyun, nefes, göz, el ve bacaklar için kısa egzersizler ve masa başı yoga. Nodly, AirPods'unuzla boyun hareketlerinizi ölçer, duruşunuzu takip eder ve başınız uzun süre önde kalınca nazikçe haber verir.",
        cta="App Store'dan indirin", note="iPhone ve iPad için · Uyumlu AirPods ile, ya da onlarsız",
        nav_links=[("areas", "Egzersizler"), ("measure", "Nasıl çalışır"), ("posture", "Duruş Takibi"), ("progress", "İlerleme")],
        gauge=dict(side_r="Sağ", side_l="Sol", back="Merkeze dönün", reached="Hedefe ulaştınız"),
        screen_alt="Nodly'nin egzersiz ekranı: sağa dönüş 51° ölçülüyor, tekrar 2/5",
        chips=["Boyun", "Duruş", "Nefes", "Göz molası"],
        areas_e="Yalnızca boyun değil", areas_h="Altı bölge, birkaç dakikalık hareketler.",
        areas=[("neck", "Boyun", "Sağa ve sola dönüş, yana eğme, aşağı ve yukarı bakış, çene içe çekme. AirPods açıyı ölçer, tekrarları sayar; AirPods yoksa Nodly süreyle yönlendirir."),
               ("breath", "Nefes", "Uzun nefes verme, kutu nefesi ve dengeli nefes. Bir çizim ve hafif bir titreşim eşliğinde 1, 2 ya da 3 dakika."),
               ("eyes", "Gözler", "Ekrandan uzaklaştıran iki dakikalık mola: uzağa bakın, yavaşça kırpın, ardından gözleriniz kapalı dinlenin."),
               ("hands", "El ve bilek", "Bilek esnetme, bilek çevirme, yumruk açıp kapama. Klavye ve fareyle geçen günler için."),
               ("legs", "Masa altı", "Parmak ucunda yükselme, ayak ucu kaldırma, diz uzatma ve oturarak adım. Sandalyenizden kalkmadan."),
               ("yoga", "Masa başı yoga", "Oturarak kedi-inek, yana eğilme ve burgu; toplantı aralarında gevşemek için omuz hareketleri.")],
        areas_note="Yalnızca boyun takibi AirPods kullanır. Diğer tüm egzersizler onlarsız çalışır.",
        measure_e="AirPods ile ölçüm", measure_h="Hedefe geldiğinizi Nodly söyler.",
        measure_p="Kulaklığınızın hareket sensörleri başınızın açısını izler. Hedef aralığa ulaştığınızda Nodly sesle ve titreşimle haber verir, tekrarı sizin yerinize sayar. Hedefler sizin hareket açıklığınıza göre ayarlanır.",
        demo_label="Deneyin: başınızı çevirin", demo_hint="Yeşil aralığa gelene kadar sağa sürükleyin, ardından merkeze dönün.",
        demo_reps="Tekrar", demo_angle="Baş açısı",
        how=[("AirPods'unuzu takın", "Nodly kulaklığın hareket sensörlerini kullanır. Kamera ya da ek bir cihaz gerekmez."),
             ("Başlangıç noktanızı kaydedin", "Tam karşıya bakın ve birkaç saniye sabit durun. Nodly bu duruşu 0° olarak alır."),
             ("Yavaşça hareket edin", "Hedef aralığa geldiğinizde Nodly sesle ve titreşimle haber verir, tekrarı sizin yerinize sayar.")],
        posture_e="Duruş Takibi", posture_h="Başınız öne düştüğünde nazik bir hatırlatma.",
        posture=[("desk", "Masa başında", "Çalışırken başınızı 30 dakikadan 2 saate kadar ya da 25 dakika çalışma, 5 dakika moladan oluşan Pomodoro turlarıyla takip eder."),
                 ("workout", "Antrenman sırasında", "Ayakta yaptığınız hareketlerde başınız düşerse saniyeler içinde uyarır. Yatarak yaptığınız hareketlerde duraklatmanız yeterli."),
                 ("lock", "Kilit ekranında", "Telefonu kilitleyip çalışmaya devam edin. Kalan süreyi kilit ekranında görür, oradan duraklatır ya da bitirirsiniz."),
                 ("quick", "Size uygun yoldan başlatın", "Siri ile, Denetim Merkezi'nden ya da Kestirmeler'de kuracağınız bir Odak modu otomasyonuyla.")],
        siri="“Nodly ile duruş takibini başlat”",
        toast="Bakışınızı karşıya kaldırmanız yeterli.",
        today_alt="Nodly'nin Bugün ekranında Duruş Takibi: Masa başında ve Sporda",
        pomodoro_alt="Pomodoro modunda çalışan Duruş Takibi: 1/4. turda 24:59 kaldı, başınız dik",
        routines_e="Rutinler", routines_h="Hazır rutinler ya da kendi sıranız.",
        routines_p="Güne Açılış ya da Ekran Molası gibi hazır bir rutinle başlayın veya kütüphaneden hareketleri seçip kendi sıranızı kurun. Bugün ekranındaki Sizin için bölümü, gününüze ve yoğun saatlerinize uygun bir rutin önerir.",
        routine_name="Kısa Mola", routine_meta="4 egzersiz · 6 dk",
        routine_steps=[("breath", "Uzun nefes verme"), ("neck", "Sağa ve Sola Dönüş"), ("neck", "Çene içe çekme"), ("legs", "Parmak ucunda yükselme")],
        suggest=["Güne Açılış", "Ekran Molası", "Bilek Molası", "Masa Başı Yoga", "Gün Sonu"],
        progress_e="İlerleme", progress_h="Küçük adımlar, görünür ilerleme.",
        progress_p="Seri günleriniz, haftanız ve zamanınızın boyun, nefes, göz, el ve bacaklar arasında nasıl dağıldığı tek bakışta. Pratik yaptıkça küçük bir 3B masa da kendiliğinden toparlanır.",
        streak="günlük seri", week=["Pt", "Sa", "Ça", "Pe", "Cu", "Ct", "Pa"], areas_title="Bu hafta bölgelere göre",
        bars=[("Boyun", 86), ("Nefes", 64), ("Gözler", 42), ("Eller", 30), ("Bacaklar", 52)],
        details_e="Ayrıntılar", details_h="Gününüze uyum sağlar.",
        details=[("cloud", "iCloud ile eşitlenir", "Geçmişiniz ve rutinleriniz kendi iCloud hesabınız üzerinden iPhone ve iPad'iniz arasında eşitlenir."),
                 ("nopods", "AirPods olmadan da", "Boyun egzersizleri süreyle de yapılabilir. Diğer egzersizler için AirPods hiç gerekmez."),
                 ("bell", "Seçtiğiniz hatırlatmalar", "Günlük hatırlatma, yoğun saatlerinizde masa başı molası ve haftalık özet; her biri isteğe bağlı."),
                 ("voice", "Sesle yönlendirir", "Sesli yönlendirme, sesler ve titreşimler eşlik eder; gözleriniz ekrandan uzak kalabilir."),
                 ("a11y", "Herkes için", "iPhone ve iPad'de büyük yazı boyutları, VoiceOver ve Hareketi Azalt desteği."),
                 ("globe", "Altı dil", "Türkçe, İngilizce, Almanca, İspanyolca, Fransızca ve Japonca.")],
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
        nav={"privacy": "Gizlilik", "terms": "Koşullar", "health": "Sağlık ve güvenlik", "support": "Destek"},
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
    out = re.sub(r"\[([^\[\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener">\1</a>', out)
    out = re.sub(r"\[([^\[\]]+)\]\((\.\./[^)\s]*)\)", r'<a href="\2">\1</a>', out)
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


def head(lang: str, route: str, key: str, title: str, description: str, extra: str = "", nav: str = "") -> str:
    """extra goes into <head>, nav into the header bar; only the landing page uses them."""
    t = T[lang]
    a = rel(route, "assets/")
    other = T[lang]["other"]
    # Both languages, the current one marked, so the page's language is never in doubt.
    lang_toggle = "".join(
        f'<span aria-current="true">{code.upper()}</span>' if code == lang else
        f'<a href="{rel(route, ROUTES[code][key])}" hreflang="{code}" lang="{code}" aria-label="{e(t["switch_label"])}">{code.upper()}</a>'
        for code in ("tr", "en"))
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
{extra}</head>
<body>
<header class="bar">
  <div class="wrap bar-inner">
    <a class="brand" href="{rel(route, ROUTES[lang]['home'])}"><img src="{a}logo.svg" alt="" width="40" height="24"><span>Nodly</span></a>
    {nav}<div class="lang">{lang_toggle}</div>
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


# Line icons for the landing page (24×24, stroke = currentColor).
ICON = {
    "neck": '<circle cx="12" cy="8" r="4.5"/><path d="M9.5 12.5v2.5M14.5 12.5v2.5M4 21c1-3.5 4.5-5.5 8-5.5s7 2 8 5.5"/>',
    "breath": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="3.5" r="1.4" fill="currentColor"/>',
    "eyes": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>',
    "hands": '<path d="M7 21v-6.5L4.5 11a1.6 1.6 0 0 1 2.6-1.9L9 11.5V4.5a1.5 1.5 0 0 1 3 0V10m0-4a1.5 1.5 0 0 1 3 0v4m0-2.5a1.5 1.5 0 0 1 3 0V15c0 3-2 6-5.5 6"/>',
    "legs": '<path d="M5 4h7v9l2.5 6.5M14.5 19.5H20M5 4v6h7"/>',
    "yoga": '<circle cx="12" cy="4.5" r="2"/><path d="M12 7.5v6.5M5 11l7-2 7 2M6.5 20.5 12 14l5.5 6.5"/>',
    "desk": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M9 20h6M12 16v4"/>',
    "workout": '<path d="M6.5 6.5v11M17.5 6.5v11M3.5 9.5v5M20.5 9.5v5M6.5 12h11"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
    "quick": '<path d="M13 2.5 5 13.5h6l-1 8 8-11h-6l1-8Z"/>',
    "cloud": '<path d="M7 18.5a4.5 4.5 0 0 1-.6-9A6 6 0 0 1 18 8.5a4.5 4.5 0 0 1-.5 10Z"/>',
    "nopods": '<path d="M8 4.5a3 3 0 0 0-3 3v3a3 3 0 0 0 2 2.8V19a1.5 1.5 0 0 0 3 0V7.5a3 3 0 0 0-2-3ZM16 4.5a3 3 0 0 1 3 3v3a3 3 0 0 1-2 2.8V19a1.5 1.5 0 0 1-3 0V7.5a3 3 0 0 1 2-3Z"/>',
    "bell": '<path d="M6 16.5V11a6 6 0 0 1 12 0v5.5l1.5 2h-15ZM10 21h4"/>',
    "voice": '<path d="M4 9.5v5h3.5L12 18.5v-13L7.5 9.5ZM15.5 9a4 4 0 0 1 0 6M18 6.5a7.5 7.5 0 0 1 0 11"/>',
    "a11y": '<circle cx="12" cy="4.5" r="1.8"/><path d="M5 8.5c4.5 1.2 9.5 1.2 14 0M12 9.8V14m0 0-3 7m3-7 3 7"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9s1-6.5 3.5-9Z"/>',
    "shield": '<path d="M12 2.5 4.5 5.5v6c0 4.5 3.2 8.4 7.5 10 4.3-1.6 7.5-5.5 7.5-10v-6Z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    "leaf": '<path d="M5 19c0-8 5-13.5 14-14-.5 9-6 14-14 14Zm0 0 7-7"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5.5M12 7.5v.5"/>',
}


def icon(name: str, cls: str = "ico") -> str:
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>'


def arc_point(deg: float, r: float, c: float = 150.0):
    import math
    rad = math.radians(deg)
    return round(c + r * math.sin(rad), 2), round(c - r * math.cos(rad), 2)


def arc(a1: float, a2: float, r: float = 118) -> str:
    """SVG arc on the gauge; 0° is straight ahead, positive is to the right."""
    x1, y1 = arc_point(a1, r)
    x2, y2 = arc_point(a2, r)
    return f"M{x1} {y1}A{r} {r} 0 0 1 {x2} {y2}"


def gauge(t: dict) -> str:
    """The exercise screen's arc: target bands both sides, a marker for the
    head angle, and the head from above. The try-it slider drives it."""
    ticks = "".join(f'<path class="g-tick" d="M{arc_point(d, 132)[0]} {arc_point(d, 132)[1]}L{arc_point(d, 140)[0]} {arc_point(d, 140)[1]}"/>' for d in range(-90, 91, 15))
    return f"""<div class="gauge" data-gauge>
  <svg viewBox="0 0 300 190" aria-hidden="true">
    {ticks}
    <path class="g-track" d="{arc(-90, 90)}"/>
    <path class="g-band" d="{arc(-70, -45)}"/>
    <path class="g-band" d="{arc(45, 70)}"/>
    <path class="g-fill" data-fill d="{arc(0, 0.01)}"/>
    <circle class="g-dot" data-dot cx="150" cy="32" r="9"/>
    <g data-head transform="rotate(0 150 150)">
      <ellipse class="g-head" cx="150" cy="150" rx="26" ry="30"/>
      <path class="g-nose" d="M143 122l7-10 7 10"/>
      <rect class="g-pod" x="118" y="140" width="8" height="18" rx="4"/>
      <rect class="g-pod" x="174" y="140" width="8" height="18" rx="4"/>
    </g>
  </svg>
  <p class="g-angle"><span data-angle>0</span>°</p>
  <p class="g-status" data-status data-r="{e(t['side_r'])}" data-l="{e(t['side_l'])}" data-back="{e(t['back'])}" data-reached="{e(t['reached'])}">{e(t['side_r'])}</p>
</div>"""


def phone(src: str, alt: str, cls: str = "") -> str:
    """An app screenshot in a phone frame."""
    return f'<div class="phone {cls}"><img class="phone-screen" src="{src}" alt="{e(alt)}" width="660" height="1434"></div>'


def landing(lang: str) -> str:
    t = T[lang]
    route = ROUTES[lang]["home"]
    a = rel(route, "assets/")
    extra = f'<link rel="stylesheet" href="{a}landing.css">\n<script src="{a}landing.js" defer></script>\n'
    extra += '<noscript><style>.reveal,.r-steps li{opacity:1;transform:none}.b-fill,.week li span{transform:none}.week li.on span{background:var(--brand)}.st-ring{stroke-dashoffset:47}</style></noscript>\n'
    nav = '<nav class="bar-nav" aria-label="Nodly">' + "".join(f'<a href="#{k}">{e(v)}</a>' for k, v in t["nav_links"]) + "</nav>\n    "
    chips = "".join(f'<span class="chip chip-{i}" style="--i:{i}">{e(c)}</span>' for i, c in enumerate(t["chips"]))
    areas = "".join(
        f'<article class="area reveal" style="--i:{i}"><div class="area-art"><img src="{a}img/areas/{k}.webp" alt="" loading="lazy" width="558" height="360"></div><h3>{icon(k)}{e(h)}</h3><p>{e(p)}</p></article>'
        for i, (k, h, p) in enumerate(t["areas"]))
    steps = "".join(
        f'<li class="step reveal" style="--i:{i}"><span class="num" aria-hidden="true">{i + 1}</span><div><h3>{e(h)}</h3><p>{e(p)}</p></div></li>'
        for i, (h, p) in enumerate(t["how"]))
    posture = "".join(
        f'<li class="reveal" style="--i:{i}">{icon(k, "ico ico-badge")}<div><h3>{e(h)}</h3><p>{e(p)}</p>'
        + (f'<p class="siri">{e(t["siri"])}</p>' if k == "quick" else "") + "</div></li>"
        for i, (k, h, p) in enumerate(t["posture"]))
    rsteps = "".join(
        f'<li style="--i:{i}"><span class="r-ico">{icon(k)}</span>{e(n)}</li>'
        for i, (k, n) in enumerate(t["routine_steps"]))
    suggest = "".join(f'<span class="pill">{e(s)}</span>' for s in t["suggest"])
    days = "".join(f'<li class="{"on" if i < 6 else ""}" style="--i:{i}"><span></span>{e(d)}</li>' for i, d in enumerate(t["week"]))
    bars = "".join(f'<li><span class="b-name">{e(n)}</span><span class="b-track"><span class="b-fill" style="--w:{w}%"></span></span></li>' for n, w in t["bars"])
    details = "".join(
        f'<div class="detail reveal" style="--i:{i}">{icon(k, "ico ico-badge")}<h3>{e(h)}</h3><p>{e(p)}</p></div>'
        for i, (k, h, p) in enumerate(t["details"]))
    trust = "".join(
        f'<div class="point reveal" style="--i:{i}">{icon(k, "ico ico-badge")}<h3>{e(h)}</h3><p>{e(p)}</p></div>'
        for i, (k, (h, p)) in enumerate(zip(("shield", "leaf", "info"), t["trust"])))
    legal = "".join(
        f'<div class="point"><h3>{e(h)}</h3><p>{e(p)}</p><a class="more" href="{rel(route, ROUTES[lang][k])}">{e(t["more"])} <span aria-hidden="true">→</span></a></div>'
        for k, h, p in t["legal"])
    return head(lang, route, "home", t["title"], t["description"], extra, nav) + f"""<div class="progress-bar" aria-hidden="true"></div>
<main class="landing">
<section class="hero">
  <div class="blobs" aria-hidden="true"><span></span><span></span><span></span></div>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <h1 class="rise">{e(t['h1'])}</h1>
      <p class="lead rise" style="--i:1">{e(t['lead'])}</p>
      <a class="button rise" style="--i:2" href="{APP_STORE_URL}">{e(t['cta'])}</a>
      <p class="note rise" style="--i:3">{e(t['note'])}</p>
    </div>
    <div class="hero-stage rise" style="--i:2">
      <div class="chips" aria-hidden="true">{chips}</div>
      {phone(f'{a}img/screen-{lang}.webp', t['screen_alt'])}
    </div>
  </div>
</section>

<section class="section" id="areas">
  <div class="wrap">
    <p class="eyebrow reveal">{e(t['areas_e'])}</p>
    <h2 class="reveal">{e(t['areas_h'])}</h2>
    <div class="areas">{areas}</div>
    <p class="aside reveal">{icon('nopods')}{e(t['areas_note'])}</p>
  </div>
</section>

<section class="section tinted" id="measure">
  <div class="wrap split">
    <div>
      <p class="eyebrow reveal">{e(t['measure_e'])}</p>
      <h2 class="reveal">{e(t['measure_h'])}</h2>
      <p class="body reveal">{e(t['measure_p'])}</p>
      <ol class="steps">{steps}</ol>
    </div>
    <div class="demo card-glass reveal">
      {gauge(t['gauge'])}
      <label class="demo-label" for="demo-range">{e(t['demo_label'])}</label>
      <input id="demo-range" type="range" min="-80" max="80" value="0" step="1" aria-describedby="demo-hint" data-demo>
      <p id="demo-hint" class="demo-hint">{e(t['demo_hint'])}</p>
      <p class="demo-reps">{e(t['demo_reps'])}: <b data-demo-reps aria-live="polite">0</b></p>
    </div>
  </div>
</section>

<section class="section" id="posture">
  <div class="wrap split reverse">
    <div class="duo reveal" data-duo>
      {phone(f'{a}img/today-{lang}.webp', t['today_alt'], 'back')}
      {phone(f'{a}img/pomodoro-{lang}.webp', t['pomodoro_alt'], 'front')}
      <div class="toast" aria-hidden="true"><img src="{a}icon-180.png" alt="" width="32" height="32"><p><b>Nodly</b>{e(t['toast'])}</p></div>
    </div>
    <div>
      <p class="eyebrow reveal">{e(t['posture_e'])}</p>
      <h2 class="reveal">{e(t['posture_h'])}</h2>
      <ul class="features">{posture}</ul>
    </div>
  </div>
</section>

<section class="section tinted" id="routines">
  <div class="wrap split">
    <div>
      <p class="eyebrow reveal">{e(t['routines_e'])}</p>
      <h2 class="reveal">{e(t['routines_h'])}</h2>
      <p class="body reveal">{e(t['routines_p'])}</p>
    </div>
    <div class="routine card-glass reveal">
      <div class="r-head"><b>{e(t['routine_name'])}</b><span>{e(t['routine_meta'])}</span></div>
      <ol class="r-steps">{rsteps}</ol>
    </div>
  </div>
  <div class="marquee" aria-hidden="true"><div class="marquee-row">{suggest * 8}</div></div>
</section>

<section class="section" id="progress">
  <div class="wrap split reverse">
    <div class="stats reveal" aria-hidden="true">
      <div class="streak card-glass">
        <svg viewBox="0 0 120 120"><circle class="st-track" cx="60" cy="60" r="50"/><circle class="st-ring" cx="60" cy="60" r="50"/></svg>
        <p><b data-count="12">0</b><span>{e(t['streak'])}</span></p>
        <ul class="week">{days}</ul>
      </div>
      <div class="bars card-glass">
        <p class="bars-title">{e(t['areas_title'])}</p>
        <ul>{bars}</ul>
      </div>
    </div>
    <div>
      <p class="eyebrow reveal">{e(t['progress_e'])}</p>
      <h2 class="reveal">{e(t['progress_h'])}</h2>
      <p class="body reveal">{e(t['progress_p'])}</p>
    </div>
  </div>
</section>

<section class="section tinted">
  <div class="wrap">
    <p class="eyebrow reveal">{e(t['details_e'])}</p>
    <h2 class="reveal">{e(t['details_h'])}</h2>
    <div class="grid3 details">{details}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow reveal">{e(t['trust_e'])}</p>
    <h2 class="reveal">{e(t['trust_h'])}</h2>
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
  <div class="blobs" aria-hidden="true"><span></span><span></span></div>
  <div class="wrap">
    <img class="end-logo" src="{a}logo-white.svg" alt="" width="96" height="57">
    <h2 class="reveal">{e(t['end_h'])}</h2>
    <p class="reveal">{e(t['end_s'])}</p>
    <a class="button light reveal" href="{APP_STORE_URL}">{e(t['cta'])}</a>
  </div>
</section>
</main>
""" + footer(lang, route)


def legal_page(lang: str, key: str) -> str:
    t = T[lang]
    route = ROUTES[lang][key]
    if key == "health":
        body = health_html(lang)
    elif key == "support":
        body = markdown(SUPPORT[lang])
    else:
        md = (LEGAL / LEGAL_FILES[(lang, key)]).read_text()
        # The legal texts link to each other by {{DOMAIN}} address; on the
        # site, point those links at the sibling page instead.
        md = md.replace("https://{{DOMAIN}}/tr/gizlilik", "../gizlilik/").replace("https://{{DOMAIN}}/privacy", "../privacy/")
        body = markdown(md)
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
        for key in ("privacy", "terms", "health", "support"):
            write(ROUTES[lang][key], legal_page(lang, key))


if __name__ == "__main__":
    main()
