"""Site copy in es (one Spanish for Spain and Latin America). Read by scripts/build.py."""

SUPPORT = """# Soporte

¿Tiene una pregunta o algo no funciona? Escríbanos a **{{EMAIL}}**; solemos responder en dos días laborables. Si se trata de su suscripción, incluya el identificador anónimo que aparece en la app en Ajustes › Soporte para que podamos encontrar su registro.

## Suscripción

### Cancelar la suscripción
Abra Ajustes (Configuración) de iOS › [su nombre] › Suscripciones, elija Nodly y toque Cancelar suscripción. También puede llegar desde Ajustes › Gestionar suscripción en la app. Mantiene el acceso hasta el final del periodo en curso.

### Restaurar compras
En un dispositivo nuevo o tras reinstalar la app, inicie sesión con la misma cuenta de Apple y toque Restaurar compras en la pantalla de suscripción de la app.

### Pedir un reembolso
Las compras se hacen a través de Apple, por lo que Apple gestiona los reembolsos. Puede solicitarlo en [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Preguntas frecuentes

### ¿Qué AirPods funcionan con Nodly?
Nodly necesita AirPods con sensores de movimiento: AirPods Pro, AirPods Max y AirPods (3.ª generación) o posteriores. Al empezar un ejercicio, la app comprueba si sus auriculares conectados son compatibles y se lo indica si no lo son.

### ¿Puedo usar Nodly sin AirPods?
Sí. Los ejercicios de cuello pueden hacerse por tiempo sin AirPods; Nodly marca el ritmo pero no mide su movimiento. Los ejercicios de respiración, la pausa para los ojos y los ejercicios bajo el escritorio nunca necesitan AirPods.

### ¿Dónde están mis datos y cómo los borro?
Los datos de movimiento se tratan en su dispositivo y nunca salen de él. Para borrar su historial de ejercicios, vaya a Ajustes › Borrar historial en la app. Al eliminar la app se borra el resto; para borrar también la copia de iCloud, vaya a Ajustes (Configuración) de iOS › [su nombre] › iCloud › Gestionar almacenamiento de la cuenta › Nodly. Más información en la [Política de privacidad](../privacidad/).

### ¿Es Nodly una app médica?
No. Nodly es una app de bienestar, no un producto sanitario. Si tiene alguna afección en el cuello, consulte a un profesional sanitario antes de empezar. Consulte [Salud y seguridad](../salud/).
"""

T = dict(
    lang="es", lang_label="Idioma",
    title="Nodly: pausas breves para el cuello, la postura y todo el cuerpo",
    description="Ejercicios breves para el cuello, la respiración, los ojos, las manos, las piernas y yoga de escritorio. Con sus AirPods, Nodly mide los movimientos de su cuello y le avisa cuando mantiene la cabeza baja. Los datos de movimiento se quedan en su dispositivo.",
    h1="Pausas suaves para sus días frente al escritorio.",
    lead="Ejercicios breves para el cuello, la respiración, los ojos, las manos y las piernas, y yoga de escritorio. Con sus AirPods, Nodly mide los movimientos de su cuello, cuida su postura y le avisa cuando mantiene la cabeza baja demasiado tiempo.",
    cta="Descargar en el App Store", note="Para iPhone y iPad · Con AirPods compatibles o sin ellos",
    nav_links=[("areas", "Ejercicios"), ("measure", "Cómo funciona"), ("posture", "Control de postura"), ("progress", "Progreso")],
    gauge=dict(side_r="Derecha", side_l="Izquierda", back="Vuelva al centro", reached="Objetivo alcanzado"),
    screen_alt="Pantalla de ejercicio de Nodly: un giro de cabeza a la derecha medido en torno a 50°",
    chips=["Cuello", "Postura", "Respiración", "Pausa para los ojos"],
    areas_e="No solo el cuello", areas_h="Seis zonas, unos minutos cada una.",
    areas=[("neck", "Cuello", "Giro de cabeza, inclinación lateral, mirar hacia abajo y hacia arriba, retracción de barbilla. Los AirPods miden el ángulo y cuentan las repeticiones; sin ellos, Nodly marca el ritmo por tiempo."),
           ("breath", "Respiración", "Espiración larga, respiración cuadrada y respiración equilibrada durante 1, 2 o 3 minutos, guiadas por un dibujo y una vibración suave."),
           ("eyes", "Ojos", "Una pausa de dos minutos lejos de la pantalla: mire a lo lejos, parpadee despacio y descanse con los ojos cerrados."),
           ("hands", "Manos y muñecas", "Estiramientos y círculos de muñeca, y abrir y cerrar el puño, para los días de teclado y ratón."),
           ("legs", "Bajo el escritorio", "Elevación de talones y de puntas, extensión de rodilla y marcha sentado, sin levantarse de la silla."),
           ("yoga", "Yoga de escritorio", "Gato-vaca, flexión lateral y torsión sentado, y ejercicios de hombros para soltarse entre reuniones.")],
    areas_note="Solo la medición del cuello usa AirPods. Todo lo demás funciona sin ellos.",
    measure_e="Medido con sus AirPods", measure_h="Nodly le dice cuándo ha llegado.",
    measure_p="Los sensores de movimiento de sus AirPods siguen el ángulo de su cabeza. Cuando llega al rango objetivo, Nodly le avisa con un sonido y una vibración y cuenta la repetición por usted. Los objetivos se adaptan a su propio rango de movimiento.",
    demo_label="Pruébelo: gire la cabeza", demo_hint="Arrastre hacia la derecha hasta la zona verde y luego vuelva al centro.",
    demo_reps="Repeticiones",
    how=[("Póngase los AirPods", "Nodly usa los sensores de movimiento de sus AirPods. Sin cámara ni dispositivos adicionales."),
         ("Guarde su punto de partida", "Mire al frente y quédese quieto unos segundos. Nodly toma esta postura como 0°."),
         ("Muévase despacio", "Cuando llega al rango objetivo, Nodly le avisa con un sonido y una vibración y cuenta la repetición por usted.")],
    posture_e="Control de postura", posture_h="Un aviso amable cuando baja la cabeza.",
    posture=[("desk", "En el escritorio", "Sigue su cabeza mientras trabaja, de 30 minutos a 2 horas, o en rondas Pomodoro de 25 minutos de trabajo y 5 de descanso."),
             ("workout", "Al entrenar", "En los ejercicios de pie, le avisa en segundos si baja la cabeza. Para los ejercicios tumbado, basta con ponerlo en pausa."),
             ("lock", "En la pantalla de bloqueo", "Bloquee el iPhone y siga trabajando. El tiempo restante aparece en la pantalla de bloqueo, y desde ahí puede pausarlo o finalizarlo."),
             ("quick", "Inícielo como prefiera", "Con Siri, desde el centro de control o con una automatización de concentración en Atajos.")],
    siri="“Iniciar Control de postura en Nodly”",
    toast="Basta con volver a levantar la vista.",
    today_alt="Pantalla Hoy de Nodly con el Control de postura: En el escritorio y Al entrenar",
    pomodoro_alt="Control de postura en modo Pomodoro: ronda 1 de 4 en curso, con la cabeza erguida",
    routines_e="Rutinas", routines_h="Rutinas listas o su propio orden.",
    routines_p="Empiece con una rutina lista, como Buen comienzo o Pausa de pantalla, o elija ejercicios de la biblioteca y póngalos en su propio orden. Para usted, en la pantalla Hoy, le sugiere una rutina que encaja con su día y sus horas de más trabajo.",
    routine_name="Pausa corta", routine_meta="4 ejercicios · 6 min",
    routine_steps=[("breath", "Espiración larga"), ("neck", "Giro de cabeza"), ("neck", "Retracción de barbilla"), ("legs", "Elevación de talones")],
    suggest=["Buen comienzo", "Pausa de pantalla", "Pausa de muñecas", "Yoga de escritorio", "Fin de la jornada"],
    progress_e="Progreso", progress_h="Pequeños pasos que se notan.",
    progress_p="Su racha, su semana y cómo reparte su tiempo entre cuello, respiración, ojos, manos y piernas, de un vistazo. Y a medida que practica, un pequeño escritorio en 3D se va ordenando solo.",
    streak="días de racha", week=["L", "M", "X", "J", "V", "S", "D"], areas_title="Esta semana por zona",
    bars=[("Cuello", 86), ("Respiración", 64), ("Ojos", 42), ("Manos", 30), ("Piernas", 52)],
    details_e="Los detalles", details_h="Se adapta a su día.",
    details=[("cloud", "Sincronizado con iCloud", "Su historial y sus rutinas se sincronizan entre su iPhone y su iPad a través de su propio iCloud."),
             ("nopods", "También sin AirPods", "Los ejercicios de cuello pueden hacerse por tiempo. Los demás ejercicios nunca necesitan AirPods."),
             ("bell", "Recordatorios a su elección", "Un recordatorio diario, pausas de escritorio en sus horas de más trabajo y un resumen semanal, todos opcionales."),
             ("voice", "Guiado por sonido", "La guía por voz, los sonidos y la vibración le acompañan para que sus ojos puedan descansar de la pantalla."),
             ("a11y", "Pensado para todos", "Tamaños de texto grandes, VoiceOver y Reducir movimiento, en iPhone y iPad."),
             ("globe", "12 idiomas", "Español, inglés, turco, alemán, francés, italiano, portugués, neerlandés, ruso, japonés, coreano y chino (simplificado y tradicional).")],
    trust_e="Privacidad y confianza", trust_h="Tranquila, privada y honesta.",
    trust=[("Se queda en su dispositivo", "Los datos de movimiento se tratan en su iPhone y nunca se guardan datos brutos. No necesita cuenta."),
           ("A su ritmo", "Los movimientos deben ser lentos y cómodos. Si algo no le sienta bien, pare de inmediato. Nodly nunca le fuerza."),
           ("No es un producto sanitario", "Nodly es una app de bienestar; no diagnostica ni trata ninguna enfermedad. Si tiene alguna afección en el cuello, consulte a un profesional sanitario antes de empezar.")],
    legal_e="Información legal", legal_h="Lo esencial, en breve.",
    legal=[("privacy", "Política de privacidad", "Sin cuenta, y sus datos de movimiento no salen de su dispositivo. Solo recogemos estadísticas de uso anónimas si nos da permiso. Sin anuncios, sin seguimiento y sin venta de datos."),
           ("terms", "Condiciones de uso", "Nodly se ofrece con suscripción mensual o anual, y los usuarios que reúnan los requisitos tienen 7 días de prueba gratis. Puede cancelar cuando quiera en los ajustes de su cuenta del App Store."),
           ("health", "Salud y seguridad", "Muévase despacio y solo dentro de un rango cómodo. Pare de inmediato si siente dolor, mareo o entumecimiento.")],
    more="Leer el texto completo",
    end_h="Tómese hoy su primera pausa.", end_s="En el App Store, para iPhone y iPad.",
    disclaimer="Nodly es una app de bienestar, no un producto sanitario.",
    nav={"privacy": "Privacidad", "terms": "Condiciones", "health": "Salud y seguridad", "support": "Soporte"},
    home="Inicio",
    health_title="Salud y seguridad",
)
