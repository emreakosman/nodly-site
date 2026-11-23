"""Site copy in fr. Read by scripts/build.py."""

SUPPORT = """# Assistance

Une question, ou quelque chose ne fonctionne pas ? Écrivez-nous à **{{EMAIL}}** ; nous répondons en général sous deux jours ouvrés. S’il s’agit de votre abonnement, joignez l’identifiant anonyme affiché dans l’app sous Réglages › Assistance, afin que nous retrouvions votre dossier.

## Abonnement

### Résilier votre abonnement
Ouvrez Réglages d’iOS › [votre nom] › Abonnements, choisissez Nodly et touchez Annuler l’abonnement. Vous pouvez aussi y accéder depuis Réglages › Gérer l’abonnement dans l’app. Vous gardez l’accès jusqu’à la fin de la période en cours.

### Restaurer vos achats
Sur un nouvel appareil ou après une réinstallation, connectez-vous avec le même compte Apple et touchez Restaurer les achats sur l’écran d’abonnement de l’app.

### Demander un remboursement
Les achats se font via Apple ; c’est donc Apple qui gère les remboursements. Faites votre demande sur [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Questions fréquentes

### Quels AirPods fonctionnent avec Nodly ?
Nodly a besoin d’AirPods dotés de capteurs de mouvement : AirPods Pro, AirPods Max et AirPods (3ᵉ génération) ou modèles plus récents. Lorsque vous lancez un exercice, l’app vérifie si vos écouteurs connectés sont compatibles et vous prévient s’ils ne le sont pas.

### Puis-je utiliser Nodly sans AirPods ?
Oui. Les exercices pour la nuque peuvent se faire en temps guidé sans AirPods ; Nodly donne alors le rythme mais ne mesure pas votre mouvement. Les exercices de respiration, la pause pour les yeux et les exercices sous le bureau n’ont jamais besoin d’AirPods.

### Où sont mes données, et comment les effacer ?
Les données de mouvement sont traitées sur votre appareil et ne le quittent jamais. Pour effacer votre historique d’exercices, allez dans Réglages › Effacer l’historique dans l’app. Supprimer l’app efface le reste ; pour supprimer aussi la copie iCloud, allez dans Réglages d’iOS › [votre nom] › iCloud › Gérer le stockage du compte › Nodly. Plus d’informations dans la [Politique de confidentialité](../confidentialite/).

### Nodly est-elle une app médicale ?
Non. Nodly est une app de bien-être, pas un dispositif médical. Si vous avez un problème de nuque, consultez un professionnel de santé avant de commencer. Voir [Santé et sécurité](../sante/).
"""

T = dict(
    lang="fr", lang_label="Langue",
    title="Nodly : de courtes pauses pour la nuque, la posture et tout le corps",
    description="De courts exercices pour la nuque, la respiration, les yeux, les mains, les jambes et du yoga au bureau. Avec vos AirPods, Nodly mesure les mouvements de votre nuque et vous prévient quand votre tête reste baissée. Les données de mouvement restent sur votre appareil.",
    h1="Des pauses en douceur pour vos journées au bureau.",
    lead="De courts exercices pour la nuque, la respiration, les yeux, les mains et les jambes, et du yoga au bureau. Avec vos AirPods, Nodly mesure les mouvements de votre nuque, veille sur votre posture et vous prévient quand votre tête reste baissée trop longtemps.",
    cta="Télécharger dans l’App Store", note="Pour iPhone et iPad · Avec des AirPods compatibles, ou sans",
    nav_links=[("areas", "Exercices"), ("measure", "Fonctionnement"), ("posture", "Suivi de posture"), ("progress", "Progrès")],
    gauge=dict(side_r="Droite", side_l="Gauche", back="Revenez au centre", reached="Objectif atteint"),
    screen_alt="Écran d’exercice de Nodly : une rotation de la tête vers la droite, mesurée autour de 50°",
    chips=["Nuque", "Posture", "Respiration", "Pause des yeux"],
    areas_e="Pas seulement la nuque", areas_h="Six zones, quelques minutes chacune.",
    areas=[("neck", "Nuque", "Rotation, inclinaison latérale, regard vers le bas et vers le haut, rétraction du menton. Les AirPods mesurent l’angle et comptent les répétitions ; sans eux, Nodly donne le rythme en temps guidé."),
           ("breath", "Respiration", "Expiration longue, respiration carrée et respiration équilibrée, pendant 1, 2 ou 3 minutes, guidées par un dessin et une légère vibration."),
           ("eyes", "Yeux", "Une pause de deux minutes loin de l’écran : regardez au loin, clignez lentement, puis reposez-vous les yeux fermés."),
           ("hands", "Mains et poignets", "Étirements et cercles des poignets, ouvrir et fermer le poing, pour les journées passées au clavier et à la souris."),
           ("legs", "Sous le bureau", "Élévations des talons et des orteils, extensions du genou et marche assise, sans quitter votre chaise."),
           ("yoga", "Yoga au bureau", "Chat-vache, flexion latérale et torsion assis, et des mouvements d’épaules pour se détendre entre deux réunions.")],
    areas_note="Seul le suivi de la nuque utilise les AirPods. Tout le reste fonctionne sans.",
    measure_e="Mesuré avec vos AirPods", measure_h="Nodly vous dit quand vous y êtes.",
    measure_p="Les capteurs de mouvement de vos AirPods suivent l’angle de votre tête. Lorsque vous atteignez la zone cible, Nodly vous prévient par un son et une vibration et compte la répétition pour vous. Les objectifs s’adaptent à votre propre amplitude.",
    demo_label="Essayez : tournez la tête", demo_hint="Faites glisser vers la droite jusqu’à la zone verte, puis revenez au centre.",
    demo_reps="Répétitions",
    how=[("Mettez vos AirPods", "Nodly utilise les capteurs de mouvement de vos AirPods. Ni caméra, ni appareil supplémentaire."),
         ("Enregistrez votre point de départ", "Regardez droit devant vous et restez immobile quelques secondes. Nodly prend cette position comme 0°."),
         ("Bougez lentement", "Lorsque vous atteignez la zone cible, Nodly vous prévient par un son et une vibration et compte la répétition pour vous.")],
    posture_e="Suivi de posture", posture_h="Un rappel en douceur quand votre tête s’abaisse.",
    posture=[("desk", "Au bureau", "Suit votre tête pendant que vous travaillez, de 30 minutes à 2 heures, ou en cycles Pomodoro de 25 minutes de travail et 5 minutes de pause."),
             ("workout", "À l’entraînement", "Pendant les exercices debout, il vous prévient en quelques secondes si votre tête s’abaisse. Pour les exercices allongés, il suffit de le mettre en pause."),
             ("lock", "Sur l’écran verrouillé", "Verrouillez votre iPhone et continuez à travailler. Le temps restant s’affiche sur l’écran verrouillé, d’où vous pouvez aussi mettre en pause ou arrêter."),
             ("quick", "Lancez-le à votre façon", "Avec Siri, depuis le centre de contrôle ou avec une automatisation de concentration dans Raccourcis.")],
    siri="« Démarrer le Suivi de posture dans Nodly »",
    toast="Il suffit de relever les yeux.",
    today_alt="Écran Aujourd’hui de Nodly avec le Suivi de posture : Au bureau et À l’entraînement",
    pomodoro_alt="Suivi de posture en mode Pomodoro : cycle 1 sur 4 en cours, tête droite",
    routines_e="Routines", routines_h="Des routines toutes prêtes, ou votre propre ordre.",
    routines_p="Commencez par une routine toute prête, comme Bien démarrer ou Pause écran, ou choisissez des exercices dans la bibliothèque et placez-les dans votre propre ordre. Pour vous, sur l’écran Aujourd’hui, vous propose une routine adaptée à votre journée et à vos heures les plus chargées.",
    routine_name="Courte pause", routine_meta="4 exercices · 6 min",
    routine_steps=[("breath", "Expiration longue"), ("neck", "Rotation gauche et droite"), ("neck", "Rétraction du menton"), ("legs", "Élévations des talons")],
    suggest=["Bien démarrer", "Pause écran", "Pause poignets", "Yoga au bureau", "Fin de journée"],
    progress_e="Progrès", progress_h="De petits pas qui se voient.",
    progress_p="Votre série, votre semaine et la répartition de votre temps entre nuque, respiration, yeux, mains et jambes, en un coup d’œil. Et plus vous pratiquez, plus un petit bureau en 3D se range tout seul.",
    streak="jours de série", week=["L", "M", "M", "J", "V", "S", "D"], areas_title="Cette semaine par zone",
    bars=[("Nuque", 86), ("Respiration", 64), ("Yeux", 42), ("Mains", 30), ("Jambes", 52)],
    details_e="Les détails", details_h="S’intègre à votre journée.",
    details=[("cloud", "Synchronisé avec iCloud", "Votre historique et vos routines se synchronisent entre votre iPhone et votre iPad via votre propre iCloud."),
             ("nopods", "Aussi sans AirPods", "Les exercices pour la nuque peuvent se faire en temps guidé. Les autres exercices n’ont jamais besoin d’AirPods."),
             ("bell", "Des rappels à votre choix", "Un rappel quotidien, des pauses au bureau pendant vos heures chargées et un résumé hebdomadaire, tous facultatifs."),
             ("voice", "Guidé par le son", "Le guidage vocal, les sons et le retour haptique vous accompagnent, pour que vos yeux puissent quitter l’écran."),
             ("a11y", "Pensé pour tous", "Grandes tailles de texte, VoiceOver et Réduire les animations, sur iPhone et iPad."),
             ("globe", "Six langues", "Français, anglais, turc, allemand, espagnol et japonais.")],
    trust_e="Confidentialité et confiance", trust_h="Calme, privée et honnête.",
    trust=[("Reste sur votre appareil", "Les données de mouvement sont traitées sur votre iPhone et les données brutes ne sont jamais enregistrées. Aucun compte nécessaire."),
           ("À votre rythme", "Les mouvements doivent rester lents et confortables. Si quelque chose ne va pas, arrêtez immédiatement. Nodly ne vous pousse jamais."),
           ("Pas un dispositif médical", "Nodly est une app de bien-être ; elle ne diagnostique ni ne traite aucune affection. Si vous avez un problème de nuque, consultez un professionnel de santé avant de commencer.")],
    legal_e="Mentions légales", legal_h="L’essentiel en bref.",
    legal=[("privacy", "Politique de confidentialité", "Aucun compte, et vos données de mouvement ne quittent pas votre appareil. Nous ne recueillons de statistiques d’utilisation anonymes qu’avec votre accord. Ni publicité, ni pistage, ni vente de données."),
           ("terms", "Conditions d’utilisation", "Nodly est proposé par abonnement mensuel ou annuel, avec 7 jours d’essai gratuit pour les utilisateurs éligibles. Vous pouvez résilier à tout moment dans les réglages de votre compte App Store."),
           ("health", "Santé et sécurité", "Bougez lentement et uniquement dans une amplitude confortable. Arrêtez immédiatement en cas de douleur, de vertige ou d’engourdissement.")],
    more="Lire le texte complet",
    end_h="Faites votre première pause dès aujourd’hui.", end_s="Sur l’App Store, pour iPhone et iPad.",
    disclaimer="Nodly est une app de bien-être, pas un dispositif médical.",
    nav={"privacy": "Confidentialité", "terms": "Conditions", "health": "Santé et sécurité", "support": "Assistance"},
    home="Accueil",
    health_title="Santé et sécurité",
)
