"""Site copy in it. Read by scripts/build.py."""

SUPPORT = """# Assistenza

Ha una domanda o qualcosa non funziona? Ci scriva a **{{EMAIL}}**: risponderemo il prima possibile, di solito entro due giorni lavorativi. Se riguarda l’abbonamento, indichi l’ID anonimo che trova nell’app in Impostazioni › Assistenza, così potremo trovare i dati giusti.

## Abbonamento

### Annullare l’abbonamento
Apra Impostazioni di iOS › [il Suo nome] › Abbonamenti, scelga Nodly e tocchi Annulla abbonamento. Può arrivarci anche dall’app, in Impostazioni › Gestisci abbonamento. L’accesso resta attivo fino alla fine del periodo in corso.

### Ripristinare gli acquisti
Su un nuovo dispositivo o dopo aver reinstallato l’app, acceda con lo stesso Apple Account e tocchi Ripristina acquisti nella schermata dell’abbonamento nell’app.

### Chiedere un rimborso
Gli acquisti avvengono tramite Apple, quindi è Apple a gestire i rimborsi. Può richiederne uno su [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Domande frequenti

### Quali AirPods funzionano con Nodly?
Nodly richiede AirPods con sensori di movimento: AirPods Pro, AirPods Max e AirPods (3ª generazione) o successivi. Quando avvia un esercizio, l’app verifica se gli auricolari connessi sono supportati e La avvisa in caso contrario.

### Posso usare Nodly senza AirPods?
Sì. Gli esercizi per il collo possono seguire un timer senza AirPods; in questo caso Nodly scandisce il ritmo ma non misura i movimenti. Gli esercizi di respirazione, la pausa per gli occhi e gli esercizi sotto la scrivania non richiedono mai gli AirPods.

### Dove sono i miei dati e come li elimino?
I dati di movimento vengono elaborati sul dispositivo e non lo lasciano mai. Per eliminare la cronologia degli esercizi, vada nell’app in Impostazioni › Elimina cronologia sessioni. Eliminando l’app si rimuove il resto; per eliminare anche la copia su iCloud, vada in Impostazioni di iOS › [il Suo nome] › iCloud › Gestisci spazio account › Nodly. Maggiori dettagli nell’[Informativa sulla privacy](../privacy/).

### Nodly è un’app medica?
No. Nodly è un’app per il benessere, non un dispositivo medico. Se ha un problema al collo, si rivolga a un professionista sanitario prima di iniziare. Consulti [Salute e sicurezza](../salute/).
"""

T = dict(
    lang="it", lang_label="Lingua",
    title="Nodly: brevi pause per il collo, la postura e tutto il resto",
    description="Brevi esercizi per collo, respirazione, occhi, mani, gambe e yoga alla scrivania. Con gli AirPods, Nodly misura i movimenti del collo e La avvisa quando la testa resta abbassata. I dati di movimento restano sul dispositivo.",
    h1="Pause leggere per le giornate alla scrivania.",
    lead="Brevi esercizi per collo, respirazione, occhi, mani e gambe, e yoga alla scrivania. Con gli AirPods, Nodly misura i movimenti del collo, segue la postura e La avvisa quando la testa resta abbassata troppo a lungo.",
    cta="Scarica su App Store", note="Per iPhone e iPad · Con AirPods compatibili o senza",
    nav_links=[("areas", "Esercizi"), ("measure", "Come funziona"), ("posture", "Controllo postura"), ("progress", "Progressi")],
    gauge=dict(side_r="Destra", side_l="Sinistra", back="Torni al centro", reached="Obiettivo raggiunto"),
    screen_alt="La schermata di esercizio di Nodly: una rotazione a destra misurata a 51°, ripetizione 1 di 5",
    chips=["Collo", "Postura", "Respirazione", "Pausa per gli occhi"],
    areas_e="Non solo il collo", areas_h="Sei zone, pochi minuti ciascuna.",
    areas=[("neck", "Collo", "Rotazioni, inclinazioni laterali, sguardo in basso e in alto, retrazione del mento. Gli AirPods misurano l’angolo e contano le ripetizioni; senza, Nodly scandisce il ritmo con un timer."),
           ("breath", "Respirazione", "Espirazione lunga, respirazione quadrata e respirazione regolare, per 1, 2 o 3 minuti, guidate da un disegno e da una leggera vibrazione."),
           ("eyes", "Occhi", "Una pausa di due minuti lontano dallo schermo: guardare lontano, sbattere lentamente le palpebre, poi riposare a occhi chiusi."),
           ("hands", "Mani e polsi", "Allungamenti dei polsi, circonduzioni e apertura e chiusura delle mani, per le giornate passate a tastiera e mouse."),
           ("legs", "Sotto la scrivania", "Sollevamento dei talloni e delle punte, estensione del ginocchio e marcia da seduti, senza alzarsi dalla sedia."),
           ("yoga", "Yoga alla scrivania", "Gatto-mucca, piegamento laterale e torsione da seduti, più movimenti per le spalle per sciogliersi tra una riunione e l’altra.")],
    areas_note="Solo il rilevamento del collo usa gli AirPods. Tutto il resto funziona senza.",
    measure_e="Misurato con gli AirPods", measure_h="Nodly Le dice quando ha raggiunto l’obiettivo.",
    measure_p="I sensori di movimento degli auricolari seguono l’angolazione della testa. Quando raggiunge l’intervallo obiettivo, Nodly La avvisa con un suono e una vibrazione e conta la ripetizione per Lei. Gli obiettivi si adattano alla Sua mobilità.",
    demo_label="Provi: giri la testa", demo_hint="Trascini verso destra fino all’intervallo verde, poi torni al centro.",
    demo_reps="Ripetizioni",
    how=[("Indossi gli AirPods", "Nodly usa i sensori di movimento degli auricolari. Nessuna fotocamera, nessun dispositivo in più."),
         ("Salvi la posizione di partenza", "Guardi dritto davanti a sé e resti immobile per qualche secondo. Nodly la considera 0°."),
         ("Si muova lentamente", "Quando raggiunge l’intervallo obiettivo, Nodly La avvisa con un suono e una vibrazione e conta la ripetizione per Lei.")],
    posture_e="Controllo postura", posture_h="Un avviso discreto quando la testa si abbassa.",
    posture=[("desk", "Alla scrivania", "Segue la testa mentre lavora, da 30 minuti a 2 ore, oppure in cicli Pomodoro di 25 minuti di lavoro e 5 di pausa."),
             ("workout", "Durante l’allenamento", "Se la testa si abbassa durante gli esercizi in piedi, Nodly La avvisa in pochi secondi. Per gli esercizi da sdraiati, basta metterlo in pausa."),
             ("lock", "Nella schermata di blocco", "Blocchi il telefono e continui a lavorare. Vede il tempo rimanente nella schermata di blocco e da lì può mettere in pausa o terminare."),
             ("quick", "Lo avvii come preferisce", "Con Siri, dal Centro di Controllo o con un’automazione Full immersion in Comandi Rapidi.")],
    siri="“Avvia il Controllo postura con Nodly”",
    toast="Basta riportare lo sguardo in avanti.",
    today_alt="La schermata Oggi di Nodly con Controllo postura: Alla scrivania e Durante l’allenamento",
    pomodoro_alt="Controllo postura in modalità Pomodoro: 24:58 rimanenti nel ciclo 1 di 4, la testa è dritta",
    routines_e="Routine", routines_h="Routine pronte, o nell’ordine che preferisce.",
    routines_p="Parta da una routine pronta come Buon inizio o Pausa dallo schermo, oppure scelga i movimenti dalla raccolta e li metta nell’ordine che preferisce. Nella schermata Oggi, Su misura Le suggerisce quella più adatta alla Sua giornata e alle ore più intense.",
    routine_name="Pausa breve", routine_meta="4 esercizi · 6 min",
    routine_steps=[("breath", "Espirazione lunga"), ("neck", "Rotazione a destra e sinistra"), ("neck", "Retrazione del mento"), ("legs", "Sollevamento dei talloni")],
    suggest=["Buon inizio", "Pausa dallo schermo", "Pausa per i polsi", "Yoga alla scrivania", "Fine giornata"],
    progress_e="Progressi", progress_h="Piccoli passi che si sommano, sotto i Suoi occhi.",
    progress_p="La serie, la settimana e come il tempo si divide tra collo, respirazione, occhi, mani e gambe, a colpo d’occhio. E mentre si esercita, una piccola scrivania in 3D si riordina da sola.",
    streak="giorni di fila", week=["L", "M", "M", "G", "V", "S", "D"], areas_title="Questa settimana per zona",
    bars=[("Collo", 86), ("Respirazione", 64), ("Occhi", 42), ("Mani", 30), ("Gambe", 52)],
    details_e="I dettagli", details_h="Si adatta alla Sua giornata.",
    details=[("cloud", "Sincronizzato con iCloud", "Cronologia e routine si sincronizzano tra iPhone e iPad tramite il Suo iCloud."),
             ("nopods", "Anche senza AirPods", "Gli esercizi per il collo possono seguire un timer. Gli altri esercizi non richiedono mai gli AirPods."),
             ("bell", "Promemoria a scelta", "Un promemoria quotidiano, pause alla scrivania nelle ore più intense e un riepilogo settimanale, tutti facoltativi."),
             ("voice", "Guidato dal suono", "Indicazioni vocali, suoni e vibrazioni La guidano, così lo sguardo può restare lontano dallo schermo."),
             ("a11y", "Pensato per tutti", "Testo dinamico, VoiceOver e Riduci movimento, su iPhone e iPad."),
             ("globe", "12 lingue", "Italiano, inglese, turco, tedesco, spagnolo, francese, portoghese, olandese, russo, giapponese, coreano e cinese (semplificato e tradizionale).")],
    trust_e="Privacy e fiducia", trust_h="Calmo, riservato e onesto.",
    trust=[("Resta sul dispositivo", "I dati di movimento vengono elaborati sul telefono e i dati grezzi non vengono mai archiviati. Non serve alcun account."),
           ("Al Suo ritmo", "I movimenti devono risultare lenti e comodi. Se qualcosa non va, si fermi subito. Nodly non La spinge mai oltre."),
           ("Non è un dispositivo medico", "Nodly è un’app per il benessere; non diagnostica né cura alcuna condizione. Se ha un problema al collo, si rivolga a un professionista sanitario prima di iniziare.")],
    legal_e="Note legali", legal_h="In breve.",
    legal=[("privacy", "Informativa sulla privacy", "Nessun account, e i dati di movimento restano sul dispositivo. Raccogliamo statistiche d’uso anonime solo se Lei lo consente. Niente pubblicità, niente tracciamento, nessuna vendita di dati."),
           ("terms", "Condizioni d’uso", "Nodly è offerta con un abbonamento mensile o annuale, e gli utenti idonei hanno 7 giorni di prova gratuita. Può annullare in qualsiasi momento nelle impostazioni del Suo account App Store."),
           ("health", "Salute e sicurezza", "Si muova lentamente e solo entro un’ampiezza comoda. Si fermi subito in caso di dolore, capogiri o intorpidimento.")],
    more="Leggi il testo completo",
    end_h="Faccia la Sua prima pausa oggi.", end_s="Su App Store, per iPhone e iPad.",
    disclaimer="Nodly è un’app per il benessere, non un dispositivo medico.",
    nav={"privacy": "Privacy", "terms": "Condizioni", "health": "Salute e sicurezza", "support": "Assistenza"},
    home="Home",
    health_title="Salute e sicurezza",
)
