"""Site copy in nl. Read by scripts/build.py."""

SUPPORT = """# Support

Hebt u een vraag of werkt er iets niet? Schrijf ons op **{{EMAIL}}**; we antwoorden zo snel mogelijk, meestal binnen twee werkdagen. Gaat het om uw abonnement, vermeld dan de anonieme ID die in de app staat onder Instellingen › Support, zodat we het juiste record kunnen vinden.

## Abonnement

### Uw abonnement opzeggen
Open in iOS Instellingen › [uw naam] › Abonnementen, kies Nodly en tik op 'Zeg abonnement op'. U komt er ook via Instellingen › Beheer abonnement in de app. U houdt toegang tot het einde van de lopende periode.

### Uw aankopen herstellen
Log op een nieuw apparaat of na opnieuw installeren in met dezelfde Apple Account en tik in de app op het abonnementsscherm op 'Herstel aankopen'.

### Een terugbetaling aanvragen
Aankopen lopen via Apple, dus terugbetalingen worden door Apple afgehandeld. Vraag er een aan op [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Veelgestelde vragen

### Welke AirPods werken met Nodly?
Nodly heeft AirPods met bewegingssensoren nodig: AirPods Pro, AirPods Max en AirPods (3e generatie) of nieuwer. Als u een oefening start, controleert de app of uw verbonden koptelefoon wordt ondersteund en laat het u weten als dat niet zo is.

### Kan ik Nodly zonder AirPods gebruiken?
Ja. Nekoefeningen kunnen zonder AirPods op tijd lopen; Nodly geeft dan het tempo aan, maar meet uw beweging niet. Ademhalingsoefeningen, de oogpauze en de oefeningen onder het bureau hebben nooit AirPods nodig.

### Waar staan mijn gegevens en hoe verwijder ik ze?
Bewegingsgegevens worden op uw apparaat verwerkt en verlaten het nooit. Uw oefengeschiedenis verwijdert u in de app via Instellingen › Verwijder sessiegeschiedenis. Als u de app verwijdert, verdwijnt de rest; om ook de kopie in iCloud te verwijderen, gaat u in iOS naar Instellingen › [uw naam] › iCloud › Beheer accountopslag › Nodly. Meer hierover in het [privacybeleid](../privacy/).

### Is Nodly een medische app?
Nee. Nodly is een welzijnsapp, geen medisch hulpmiddel. Hebt u een nekaandoening, overleg dan met een zorgverlener voordat u begint. Zie [Gezondheid en veiligheid](../gezondheid/).
"""

T = dict(
    lang="nl", lang_label="Taal",
    title="Nodly: korte pauzes voor uw nek, uw houding en de rest van u",
    description="Korte oefeningen voor uw nek, ademhaling, ogen, handen, benen en bureauyoga. Met uw AirPods meet Nodly uw nekbewegingen en laat het u weten als uw hoofd omlaag blijft. Bewegingsgegevens blijven op uw apparaat.",
    h1="Rustige pauzes voor uw dagen aan het bureau.",
    lead="Korte oefeningen voor uw nek, ademhaling, ogen, handen en benen, en bureauyoga. Met uw AirPods meet Nodly uw nekbewegingen, volgt het uw houding en laat het u weten als uw hoofd te lang omlaag blijft.",
    cta="Download in de App Store", note="Voor iPhone en iPad · Met compatibele AirPods, of zonder",
    nav_links=[("areas", "Oefeningen"), ("measure", "Zo werkt het"), ("posture", "Houdingscheck"), ("progress", "Voortgang")],
    gauge=dict(side_r="Rechts", side_l="Links", back="Terug naar het midden", reached="Doel bereikt"),
    screen_alt="Oefenscherm van Nodly: een draai naar rechts gemeten op 51°, herhaling 1 van 5",
    chips=["Nek", "Houding", "Ademhaling", "Oogpauze"],
    areas_e="Niet alleen uw nek", areas_h="Zes gebieden, elk een paar minuten.",
    areas=[("neck", "Nek", "Draaien, zijwaarts kantelen, omlaag en omhoog kijken, kin intrekken. AirPods meten de hoek en tellen de herhalingen; zonder AirPods geeft Nodly het tempo aan op tijd."),
           ("breath", "Ademhaling", "Lange uitademing, boxademhaling en gelijkmatige ademhaling, 1, 2 of 3 minuten, in het tempo van een tekening en een zachte tik."),
           ("eyes", "Ogen", "Een pauze van twee minuten weg van het scherm: kijk in de verte, knipper langzaam en rust daarna met uw ogen dicht."),
           ("hands", "Handen en polsen", "Polsrekoefeningen, polsrondjes en handen openen en sluiten, voor dagen achter toetsenbord en muis."),
           ("legs", "Onder het bureau", "Hielheffen, tenen heffen, knie strekken en zittend marcheren, zonder van uw stoel op te staan."),
           ("yoga", "Bureauyoga", "Zittende kat-koe, zijwaarts buigen en draaien, plus schouderoefeningen om los te komen tussen afspraken.")],
    areas_note="Alleen de nekmeting gebruikt AirPods. Al het andere werkt zonder.",
    measure_e="Gemeten met uw AirPods", measure_h="Nodly laat weten wanneer u er bent.",
    measure_p="De bewegingssensoren in uw oordopjes volgen de hoek van uw hoofd. Bereikt u het doelbereik, dan laat Nodly dat weten met een geluid en een tik en telt het de herhaling voor u. De doelen passen zich aan uw eigen bewegingsbereik aan.",
    demo_label="Probeer het: draai uw hoofd", demo_hint="Sleep naar rechts tot u het groene bereik haalt en kom dan terug naar het midden.",
    demo_reps="Herhalingen",
    how=[("Doe uw AirPods in", "Nodly gebruikt de bewegingssensoren in uw oordopjes. Geen camera, geen extra apparaat."),
         ("Leg uw beginpositie vast", "Kijk recht vooruit en houd u een paar seconden stil. Nodly neemt dit als 0°."),
         ("Beweeg langzaam", "Bereikt u het doelbereik, dan laat Nodly dat weten met een geluid en een tik, en telt het de herhaling voor u.")],
    posture_e="Houdingscheck", posture_h="Een zacht seintje als uw hoofd zakt.",
    posture=[("desk", "Aan het bureau", "Volgt uw hoofd terwijl u werkt, van 30 minuten tot 2 uur, of in Pomodoro-rondes van 25 minuten werk en 5 minuten rust."),
             ("workout", "Tijdens een training", "Zakt uw hoofd bij staande oefeningen, dan laat Nodly het binnen enkele seconden weten. Bij oefeningen die u liggend doet, pauzeert u het gewoon."),
             ("lock", "Op het toegangsscherm", "Vergrendel uw telefoon en werk door. U ziet de resterende tijd op het toegangsscherm en kunt daar pauzeren of stoppen."),
             ("quick", "Start het zoals u wilt", "Met Siri, via het bedieningspaneel of met een focusautomatisering in Opdrachten.")],
    siri="“Start Houdingscheck in Nodly”",
    toast="Kijk gewoon weer recht vooruit.",
    today_alt="Het scherm Vandaag van Nodly met Houdingscheck: Aan het bureau en Tijdens het sporten",
    pomodoro_alt="Houdingscheck in Pomodoro-modus: nog 24:58 in ronde 1 van 4, uw hoofd is rechtop",
    routines_e="Routines", routines_h="Kant-en-klare routines, of uw eigen volgorde.",
    routines_p="Begin met een kant-en-klare routine zoals Goed begin of Schermpauze, of kies bewegingen uit de bibliotheek en zet ze in uw eigen volgorde. 'Voor u' op het scherm Vandaag stelt er een voor die past bij uw dag en uw drukste uren.",
    routine_name="Korte pauze", routine_meta="4 oefeningen · 6 min",
    routine_steps=[("breath", "Lange uitademing"), ("neck", "Links en rechts draaien"), ("neck", "Kin intrekken"), ("legs", "Hielheffen")],
    suggest=["Goed begin", "Schermpauze", "Polspauze", "Bureauyoga", "Einde van de dag"],
    progress_e="Voortgang", progress_h="Kleine stappen die u ziet optellen.",
    progress_p="Uw reeks, uw week en hoe uw tijd verdeeld is over nek, ademhaling, ogen, handen en benen, in één oogopslag. En terwijl u oefent, ruimt een klein 3D-bureau zichzelf op.",
    streak="dagen op rij", week=["M", "D", "W", "D", "V", "Z", "Z"], areas_title="Deze week per gebied",
    bars=[("Nek", 86), ("Ademhaling", 64), ("Ogen", 42), ("Handen", 30), ("Benen", 52)],
    details_e="De details", details_h="Past in uw dag.",
    details=[("cloud", "Gesynchroniseerd via iCloud", "Uw geschiedenis en routines worden via uw eigen iCloud gesynchroniseerd tussen uw iPhone en iPad."),
             ("nopods", "Ook zonder AirPods", "Nekoefeningen kunnen op tijd lopen. De andere oefeningen hebben nooit AirPods nodig."),
             ("bell", "Herinneringen naar keuze", "Een dagelijkse herinnering, bureaupauzes tijdens uw drukke uren en een weekoverzicht, elk optioneel."),
             ("voice", "Met geluid begeleid", "Gesproken aanwijzingen, geluiden en haptische feedback begeleiden u, zodat uw ogen van het scherm kunnen blijven."),
             ("a11y", "Voor iedereen gemaakt", "Grotere tekst, VoiceOver en Verminder beweging, op iPhone en iPad."),
             ("globe", "12 talen", "Nederlands, Engels, Turks, Duits, Spaans, Frans, Italiaans, Portugees, Russisch, Japans, Koreaans en Chinees (vereenvoudigd en traditioneel).")],
    trust_e="Privacy en vertrouwen", trust_h="Rustig, privé en eerlijk.",
    trust=[("Blijft op uw apparaat", "Bewegingsgegevens worden op uw telefoon verwerkt en ruwe bewegingsgegevens worden nooit bewaard. Geen account nodig."),
           ("In uw eigen tempo", "Bewegingen horen langzaam en prettig te voelen. Voelt iets niet goed, stop dan meteen. Nodly dwingt u nooit."),
           ("Geen medisch hulpmiddel", "Nodly is een welzijnsapp; het stelt geen diagnose en behandelt geen aandoening. Hebt u een nekaandoening, overleg dan met een zorgverlener voordat u begint.")],
    legal_e="Juridisch", legal_h="De korte versie.",
    legal=[("privacy", "Privacybeleid", "Geen account, en uw bewegingsgegevens blijven op uw apparaat. We verzamelen alleen anonieme gebruiksstatistieken als u dat toestaat. Geen advertenties, geen tracking, geen verkoop van gegevens."),
           ("terms", "Gebruiksvoorwaarden", "Nodly wordt aangeboden als maand- of jaarabonnement, en wie in aanmerking komt, krijgt een gratis proefperiode van 7 dagen. U kunt altijd opzeggen in de instellingen van uw App Store-account."),
           ("health", "Gezondheid en veiligheid", "Beweeg langzaam en alleen binnen een prettig bereik. Stop meteen als u pijn, duizeligheid of een doof gevoel hebt.")],
    more="Lees de volledige tekst",
    end_h="Neem vandaag uw eerste pauze.", end_s="In de App Store, voor iPhone en iPad.",
    disclaimer="Nodly is een welzijnsapp, geen medisch hulpmiddel.",
    nav={"privacy": "Privacy", "terms": "Voorwaarden", "health": "Gezondheid en veiligheid", "support": "Support"},
    home="Home",
    health_title="Gezondheid en veiligheid",
)
