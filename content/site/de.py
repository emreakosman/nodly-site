"""Site copy in de. Read by scripts/build.py."""

SUPPORT = """# Support

Haben Sie eine Frage, oder funktioniert etwas nicht? Schreiben Sie uns an **{{EMAIL}}**; wir antworten meist innerhalb von zwei Werktagen. Geht es um Ihr Abonnement, fügen Sie bitte die anonyme Kennung aus der App (Einstellungen › Support) hinzu, damit wir den richtigen Eintrag finden.

## Abonnement

### Abonnement kündigen
Öffnen Sie iOS-Einstellungen › [Ihr Name] › Abonnements, wählen Sie Nodly und tippen Sie auf „Abo kündigen“. Sie gelangen auch über Einstellungen › Abonnement verwalten in der App dorthin. Der Zugang bleibt bis zum Ende des laufenden Zeitraums erhalten.

### Käufe wiederherstellen
Melden Sie sich auf einem neuen Gerät oder nach einer Neuinstallation mit demselben Apple Account an und tippen Sie auf dem Abo-Bildschirm der App auf „Käufe wiederherstellen“.

### Erstattung beantragen
Käufe erfolgen über Apple, daher bearbeitet Apple auch Erstattungen. Sie beantragen sie unter [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Häufige Fragen

### Welche AirPods funktionieren mit Nodly?
Nodly braucht AirPods mit Bewegungssensoren: AirPods Pro, AirPods Max und AirPods (3. Generation) oder neuer. Wenn Sie eine Übung starten, prüft die App, ob Ihre verbundenen Kopfhörer unterstützt werden, und sagt es Ihnen, falls nicht.

### Kann ich Nodly ohne AirPods nutzen?
Ja. Nackenübungen laufen ohne AirPods auch nach Zeit; Nodly gibt dann das Tempo vor, misst Ihre Bewegung aber nicht. Atemübungen, die Augenpause und die Übungen unter dem Schreibtisch brauchen nie AirPods.

### Wo sind meine Daten, und wie lösche ich sie?
Bewegungsdaten werden auf Ihrem Gerät verarbeitet und verlassen es nie. Ihren Übungsverlauf löschen Sie in der App unter Einstellungen › Verlauf der Einheiten löschen. Wenn Sie die App löschen, wird der Rest entfernt; die Kopie in iCloud löschen Sie unter iOS-Einstellungen › [Ihr Name] › iCloud › Accountspeicher verwalten › Nodly. Mehr dazu in der [Datenschutzrichtlinie](../datenschutz/).

### Ist Nodly eine medizinische App?
Nein. Nodly ist eine Wellness-App und kein Medizinprodukt. Haben Sie Beschwerden am Nacken, sprechen Sie vor dem Beginn mit einer Fachperson im Gesundheitswesen. Siehe [Gesundheit und Sicherheit](../gesundheit/).
"""

T = dict(
    lang="de", lang_label="Sprache",
    title="Nodly: kurze Pausen für Nacken, Haltung und den ganzen Körper",
    description="Kurze Übungen für Nacken, Atmung, Augen, Hände, Beine und Büro-Yoga. Mit Ihren AirPods misst Nodly Ihre Nackenbewegungen und erinnert Sie, wenn Ihr Kopf gesenkt bleibt. Bewegungsdaten bleiben auf Ihrem Gerät.",
    h1="Sanfte Pausen für Ihre Tage am Schreibtisch.",
    lead="Kurze Übungen für Nacken, Atmung, Augen, Hände und Beine, dazu Büro-Yoga. Mit Ihren AirPods misst Nodly Ihre Nackenbewegungen, achtet auf Ihre Haltung und meldet sich, wenn Ihr Kopf zu lange gesenkt bleibt.",
    cta="Im App Store laden", note="Für iPhone und iPad · Mit kompatiblen AirPods oder ohne",
    nav_links=[("areas", "Übungen"), ("measure", "So funktioniert’s"), ("posture", "Haltungscheck"), ("progress", "Fortschritt")],
    gauge=dict(side_r="Rechts", side_l="Links", back="Zurück zur Mitte", reached="Ziel erreicht"),
    screen_alt="Übungsbildschirm von Nodly: eine Kopfdrehung nach rechts, gemessen bei rund 50°",
    chips=["Nacken", "Haltung", "Atmung", "Augenpause"],
    areas_e="Nicht nur der Nacken", areas_h="Sechs Bereiche, jeweils wenige Minuten.",
    areas=[("neck", "Nacken", "Kopfdrehung, Seitneigung, Blick nach unten und oben, Kinn einziehen. AirPods messen den Winkel und zählen die Wiederholungen; ohne sie gibt Nodly das Tempo nach Zeit vor."),
           ("breath", "Atmung", "Langes Ausatmen, Box-Atmung und gleichmäßiges Atmen, 1, 2 oder 3 Minuten lang, geführt von einer Zeichnung und einem sanften Tippen."),
           ("eyes", "Augen", "Eine zweiminütige Pause vom Bildschirm: in die Ferne schauen, langsam blinzeln, dann mit geschlossenen Augen ausruhen."),
           ("hands", "Hände & Handgelenke", "Handgelenke dehnen, Handgelenkkreisen, Faust öffnen und schließen – für Tage mit Tastatur und Maus."),
           ("legs", "Unter dem Schreibtisch", "Fersenheben, Zehenheben, Kniestrecken und Marschieren im Sitzen, ohne aufzustehen."),
           ("yoga", "Büro-Yoga", "Katze-Kuh, Seitbeuge und Drehung im Sitzen, dazu Schulterübungen zum Lockern zwischen zwei Meetings.")],
    areas_note="Nur die Nackenmessung nutzt AirPods. Alles andere funktioniert ohne.",
    measure_e="Gemessen mit Ihren AirPods", measure_h="Nodly sagt Ihnen, wann Sie da sind.",
    measure_p="Die Bewegungssensoren Ihrer AirPods verfolgen Ihren Kopfwinkel. Erreichen Sie den Zielbereich, meldet sich Nodly mit einem Ton und einem Tippen und zählt die Wiederholung für Sie. Die Ziele passen sich Ihrem eigenen Bewegungsumfang an.",
    demo_label="Probieren Sie es: Drehen Sie den Kopf", demo_hint="Ziehen Sie nach rechts bis in den grünen Bereich und dann zurück zur Mitte.",
    demo_reps="Wiederholungen",
    how=[("AirPods einsetzen", "Nodly nutzt die Bewegungssensoren Ihrer AirPods. Keine Kamera, kein zusätzliches Gerät."),
         ("Ausgangspunkt speichern", "Schauen Sie geradeaus und halten Sie einige Sekunden still. Nodly nimmt diese Haltung als 0°."),
         ("Langsam bewegen", "Erreichen Sie den Zielbereich, meldet sich Nodly mit einem Ton und einem Tippen und zählt die Wiederholung für Sie.")],
    posture_e="Haltungscheck", posture_h="Eine sanfte Erinnerung, wenn Ihr Kopf absinkt.",
    posture=[("desk", "Am Schreibtisch", "Achtet beim Arbeiten auf Ihren Kopf – 30 Minuten bis 2 Stunden lang oder in Pomodoro-Runden aus 25 Minuten Arbeit und 5 Minuten Pause."),
             ("workout", "Beim Training", "Bei Übungen im Stehen erinnert er Sie innerhalb von Sekunden, wenn Ihr Kopf absinkt. Bei Übungen im Liegen pausieren Sie ihn einfach."),
             ("lock", "Auf dem Sperrbildschirm", "Sperren Sie Ihr iPhone und arbeiten Sie weiter. Die verbleibende Zeit sehen Sie auf dem Sperrbildschirm, und dort können Sie auch pausieren oder beenden."),
             ("quick", "So starten, wie es Ihnen passt", "Mit Siri, über das Kontrollzentrum oder mit einer Fokus-Automation in „Kurzbefehle“.")],
    siri="„Haltungscheck in Nodly starten“",
    toast="Heben Sie einfach den Blick.",
    today_alt="Heute-Bildschirm von Nodly mit dem Haltungscheck: Am Schreibtisch und Beim Training",
    pomodoro_alt="Haltungscheck im Pomodoro-Modus: Runde 1 von 4 läuft, Ihr Kopf ist aufrecht",
    routines_e="Routinen", routines_h="Fertige Routinen oder Ihre eigene Reihenfolge.",
    routines_p="Beginnen Sie mit einer fertigen Routine wie „Guter Start“ oder „Bildschirmpause“, oder wählen Sie Übungen aus der Bibliothek und bringen Sie sie in Ihre eigene Reihenfolge. „Für Sie“ auf dem Heute-Bildschirm schlägt eine Routine vor, die zu Ihrem Tag und Ihren vollsten Stunden passt.",
    routine_name="Kurze Pause", routine_meta="4 Übungen · 6 Min.",
    routine_steps=[("breath", "Langes Ausatmen"), ("neck", "Kopfdrehung"), ("neck", "Kinn einziehen"), ("legs", "Fersenheben")],
    suggest=["Guter Start", "Bildschirmpause", "Handgelenkpause", "Büro-Yoga", "Feierabend"],
    progress_e="Fortschritt", progress_h="Kleine Schritte, die sichtbar werden.",
    progress_p="Ihre Serie, Ihre Woche und wie sich Ihre Zeit auf Nacken, Atmung, Augen, Hände und Beine verteilt – auf einen Blick. Und je mehr Sie üben, desto aufgeräumter wird ein kleiner 3D-Schreibtisch.",
    streak="Tage in Serie", week=["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"], areas_title="Diese Woche nach Bereich",
    bars=[("Nacken", 86), ("Atmung", 64), ("Augen", 42), ("Hände", 30), ("Beine", 52)],
    details_e="Die Details", details_h="Passt in Ihren Tag.",
    details=[("cloud", "Über iCloud synchronisiert", "Ihr Verlauf und Ihre Routinen werden über Ihre eigene iCloud zwischen iPhone und iPad synchronisiert."),
             ("nopods", "Auch ohne AirPods", "Nackenübungen laufen auch nach Zeit. Die anderen Übungen brauchen nie AirPods."),
             ("bell", "Erinnerungen nach Wahl", "Eine tägliche Erinnerung, Schreibtischpausen in Ihren vollsten Stunden und ein Wochenrückblick – jeweils optional."),
             ("voice", "Mit Ton geführt", "Sprachanleitung, Töne und Haptik führen Sie, damit Ihre Augen vom Bildschirm wegbleiben können."),
             ("a11y", "Für alle gemacht", "Große Schriftgrößen, VoiceOver und „Bewegung reduzieren“ auf iPhone und iPad."),
             ("globe", "12 Sprachen", "Deutsch, Englisch, Türkisch, Spanisch, Französisch, Italienisch, Portugiesisch, Niederländisch, Russisch, Japanisch, Koreanisch und Chinesisch (vereinfacht und traditionell).")],
    trust_e="Datenschutz und Vertrauen", trust_h="Ruhig, privat und ehrlich.",
    trust=[("Bleibt auf Ihrem Gerät", "Bewegungsdaten werden auf Ihrem iPhone verarbeitet, rohe Bewegungsdaten nie gespeichert. Kein Account nötig."),
           ("In Ihrem Tempo", "Bewegungen sollen sich langsam und angenehm anfühlen. Fühlt sich etwas nicht richtig an, hören Sie sofort auf. Nodly drängt Sie nie."),
           ("Kein Medizinprodukt", "Nodly ist eine Wellness-App; sie diagnostiziert oder behandelt keine Erkrankung. Haben Sie Beschwerden am Nacken, sprechen Sie vor dem Beginn mit einer Fachperson im Gesundheitswesen.")],
    legal_e="Rechtliches", legal_h="Das Wichtigste in Kürze.",
    legal=[("privacy", "Datenschutzrichtlinie", "Kein Account, und Ihre Bewegungsdaten verlassen Ihr Gerät nicht. Anonyme Nutzungsstatistiken erheben wir nur mit Ihrer Erlaubnis. Keine Werbung, kein Tracking, kein Verkauf von Daten."),
           ("terms", "Nutzungsbedingungen", "Nodly gibt es im Monats- oder Jahresabo; berechtigte Nutzerinnen und Nutzer erhalten 7 Tage kostenlos. Sie können jederzeit in den Einstellungen Ihres App Store-Accounts kündigen."),
           ("health", "Gesundheit und Sicherheit", "Bewegen Sie sich langsam und nur in einem angenehmen Bereich. Hören Sie sofort auf, wenn Sie Schmerzen, Schwindel oder Taubheit spüren.")],
    more="Vollständigen Text lesen",
    end_h="Machen Sie heute Ihre erste Pause.", end_s="Im App Store, für iPhone und iPad.",
    disclaimer="Nodly ist eine Wellness-App, kein Medizinprodukt.",
    nav={"privacy": "Datenschutz", "terms": "Nutzungsbedingungen", "health": "Gesundheit und Sicherheit", "support": "Support"},
    home="Startseite",
    health_title="Gesundheit und Sicherheit",
)
