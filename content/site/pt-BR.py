"""Site copy in pt-BR. Read by scripts/build.py."""

SUPPORT = """# Suporte

Tem alguma dúvida ou algo não está funcionando? Escreva para **{{EMAIL}}** e responderemos o quanto antes, normalmente em até dois dias úteis. Se for sobre a sua assinatura, inclua o ID anônimo exibido no app em Ajustes › Suporte, para encontrarmos o registro certo.

## Assinatura

### Cancelar a assinatura
Abra Ajustes do iOS › [seu nome] › Assinaturas, escolha o Nodly e toque em Cancelar Assinatura. Você também pode chegar lá pelo app, em Ajustes › Gerenciar Assinatura. O acesso continua até o fim do período atual.

### Restaurar compras
Em um novo dispositivo ou depois de reinstalar o app, entre com a mesma Conta Apple e toque em Restaurar Compras na tela de assinatura do app.

### Pedir reembolso
As compras são feitas pela Apple, então os reembolsos são tratados pela Apple. Faça o pedido em [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Perguntas frequentes

### Quais AirPods funcionam com o Nodly?
O Nodly precisa de AirPods com sensores de movimento: AirPods Pro, AirPods Max e AirPods (3ª geração) ou posteriores. Quando você inicia um exercício, o app verifica se os fones conectados são compatíveis e avisa se não forem.

### Posso usar o Nodly sem AirPods?
Sim. Os exercícios para o pescoço podem seguir um temporizador sem AirPods; nesse caso, o Nodly guia o ritmo, mas não mede seus movimentos. Os exercícios de respiração, a pausa para os olhos e os exercícios sob a mesa nunca precisam de AirPods.

### Onde ficam meus dados e como apagá-los?
Os dados de movimento são processados no seu dispositivo e nunca saem dele. Para apagar seu histórico de exercícios, vá a Ajustes › Apagar histórico de sessões no app. Apagar o app remove o restante; para apagar também a cópia no iCloud, vá a Ajustes do iOS › [seu nome] › iCloud › Gerenciar Armazenamento da Conta › Nodly. Saiba mais na [Política de Privacidade](../privacidade/).

### O Nodly é um app médico?
Não. O Nodly é um app de bem-estar, não um dispositivo médico. Se você tem algum problema no pescoço, consulte um profissional de saúde antes de começar. Veja [Saúde e segurança](../saude/).
"""

T = dict(
    lang="pt-BR", lang_label="Idioma",
    title="Nodly: pausas curtas para o pescoço, a postura e o resto do corpo",
    description="Exercícios curtos para pescoço, respiração, olhos, mãos, pernas e ioga na cadeira. Com seus AirPods, o Nodly mede os movimentos do pescoço e avisa quando sua cabeça fica baixa. Os dados de movimento ficam no seu dispositivo.",
    h1="Pausas leves para seus dias de trabalho.",
    lead="Exercícios curtos para pescoço, respiração, olhos, mãos e pernas, além de ioga na cadeira. Com seus AirPods, o Nodly mede os movimentos do pescoço, acompanha sua postura e avisa quando sua cabeça fica baixa por muito tempo.",
    cta="Baixar na App Store", note="Para iPhone e iPad · Com AirPods compatíveis ou sem eles",
    nav_links=[("areas", "Exercícios"), ("measure", "Como funciona"), ("posture", "Monitor de Postura"), ("progress", "Progresso")],
    gauge=dict(side_r="Direita", side_l="Esquerda", back="Volte ao centro", reached="Meta alcançada"),
    screen_alt="Tela de exercício do Nodly: um giro para a direita medido em 51°, repetição 1 de 5",
    chips=["Pescoço", "Postura", "Respiração", "Pausa para os olhos"],
    areas_e="Não é só o pescoço", areas_h="Seis áreas, poucos minutos cada.",
    areas=[("neck", "Pescoço", "Giros, inclinações laterais, olhar para baixo e para cima, retração do queixo. Os AirPods medem o ângulo e contam as repetições; sem eles, o Nodly guia o ritmo com um temporizador."),
           ("breath", "Respiração", "Expiração longa, respiração quadrada e respiração equilibrada, por 1, 2 ou 3 minutos, no ritmo de uma animação e de uma vibração leve."),
           ("eyes", "Olhos", "Uma pausa de dois minutos longe da tela: olhe para longe, pisque devagar e descanse de olhos fechados."),
           ("hands", "Mãos e punhos", "Alongamentos e círculos com os punhos e exercícios de abrir e fechar as mãos, para dias de teclado e mouse."),
           ("legs", "Sob a mesa", "Elevação de calcanhares, elevação da ponta dos pés, extensão de joelho e marcha sentada, sem sair da cadeira."),
           ("yoga", "Ioga na cadeira", "Gato-vaca, alongamento lateral e torção sentados, além de movimentos para soltar os ombros entre reuniões.")],
    areas_note="Só o rastreamento do pescoço usa AirPods. Todo o resto funciona sem eles.",
    measure_e="Medido com seus AirPods", measure_h="O Nodly avisa quando você chega lá.",
    measure_p="Os sensores de movimento dos fones acompanham o ângulo da sua cabeça. Quando você alcança a faixa-alvo, o Nodly avisa com um som e uma vibração e conta a repetição por você. As metas se ajustam à sua própria amplitude de movimento.",
    demo_label="Experimente: gire a cabeça", demo_hint="Arraste para a direita até chegar à faixa verde e depois volte ao centro.",
    demo_reps="Repetições",
    how=[("Coloque os AirPods", "O Nodly usa os sensores de movimento dos seus fones. Sem câmera e sem outro aparelho."),
         ("Registre seu ponto de partida", "Olhe bem para a frente e mantenha a cabeça parada por alguns segundos. O Nodly considera essa posição como 0°."),
         ("Mova-se devagar", "Quando você alcança a faixa-alvo, o Nodly avisa com um som e uma vibração e conta a repetição por você.")],
    posture_e="Monitor de Postura", posture_h="Um aviso discreto quando sua cabeça baixa.",
    posture=[("desk", "Na mesa", "Acompanha sua cabeça enquanto você trabalha, de 30 minutos a 2 horas, ou em ciclos Pomodoro de 25 minutos de trabalho e 5 de intervalo."),
             ("workout", "No treino", "Se sua cabeça baixar em exercícios feitos em pé, o Nodly avisa em segundos. Para exercícios feitos deitado, basta pausá-lo."),
             ("lock", "Na Tela Bloqueada", "Bloqueie o celular e continue trabalhando. O tempo restante aparece na Tela Bloqueada, e você pode pausar ou encerrar por ali."),
             ("quick", "Inicie do seu jeito", "Com a Siri, pela Central de Controle ou com uma automação de Foco no app Atalhos.")],
    siri="“Iniciar Monitor de Postura no Nodly”",
    toast="Basta voltar a olhar para a frente.",
    today_alt="Tela Hoje do Nodly com o Monitor de Postura: Na mesa e No treino",
    pomodoro_alt="Monitor de Postura em modo Pomodoro: faltam 24:58 no ciclo 1 de 4, sua cabeça está erguida",
    routines_e="Rotinas", routines_h="Rotinas prontas ou na sua ordem.",
    routines_p="Comece com uma rotina pronta, como Começo do Dia ou Pausa da Tela, ou escolha movimentos da biblioteca e coloque-os na ordem que quiser. Na tela Hoje, Para você sugere uma rotina que combina com o seu dia e o seu horário mais corrido.",
    routine_name="Pausa Curta", routine_meta="4 exercícios · 6 min",
    routine_steps=[("breath", "Expiração longa"), ("neck", "Giro para os Lados"), ("neck", "Retração do queixo"), ("legs", "Elevação de calcanhares")],
    suggest=["Começo do Dia", "Pausa da Tela", "Pausa para os Punhos", "Ioga na Cadeira", "Fim do Dia"],
    progress_e="Progresso", progress_h="Pequenos passos que você vê somarem.",
    progress_p="Sua sequência, sua semana e como seu tempo se divide entre pescoço, respiração, olhos, mãos e pernas, tudo num relance. E, conforme você se exercita, uma pequena mesa em 3D vai se arrumando.",
    streak="dias de sequência", week=["S", "T", "Q", "Q", "S", "S", "D"], areas_title="Esta semana por área",
    bars=[("Pescoço", 86), ("Respiração", 64), ("Olhos", 42), ("Mãos", 30), ("Pernas", 52)],
    details_e="Os detalhes", details_h="Cabe no seu dia.",
    details=[("cloud", "Sincronizado pelo iCloud", "Seu histórico e suas rotinas são sincronizados entre seu iPhone e seu iPad pelo seu próprio iCloud."),
             ("nopods", "Também sem AirPods", "Os exercícios para o pescoço podem seguir um temporizador. Os outros exercícios nunca precisam de AirPods."),
             ("bell", "Lembretes que você escolhe", "Um lembrete diário, pausas na mesa durante seu horário mais corrido e um resumo semanal, todos opcionais."),
             ("voice", "Guiado por som", "Instruções faladas, sons e vibrações guiam você, para que seus olhos possam ficar longe da tela."),
             ("a11y", "Feito para todos", "Texto Dinâmico, VoiceOver e Reduzir Movimento, no iPhone e no iPad."),
             ("globe", "12 idiomas", "Português, inglês, turco, alemão, espanhol, francês, italiano, holandês, russo, japonês, coreano e chinês (simplificado e tradicional).")],
    trust_e="Privacidade e confiança", trust_h="Calmo, privado e honesto.",
    trust=[("Fica no seu dispositivo", "Os dados de movimento são processados no seu celular, e o movimento bruto nunca é armazenado. Não é preciso criar conta."),
           ("No seu ritmo", "Os movimentos devem ser lentos e confortáveis. Se algo não parecer bem, pare imediatamente. O Nodly nunca pressiona você."),
           ("Não é um dispositivo médico", "O Nodly é um app de bem-estar; não diagnostica nem trata nenhuma condição. Se você tem algum problema no pescoço, consulte um profissional de saúde antes de começar.")],
    legal_e="Informações legais", legal_h="A versão resumida.",
    legal=[("privacy", "Política de Privacidade", "Sem conta, e seus dados de movimento ficam no seu dispositivo. Só coletamos estatísticas de uso anônimas se você permitir. Sem anúncios, sem rastreamento, sem venda de dados."),
           ("terms", "Termos de Uso", "O Nodly é oferecido como assinatura mensal ou anual, e usuários elegíveis têm 7 dias de teste grátis. Você pode cancelar quando quiser nos ajustes da sua conta da App Store."),
           ("health", "Saúde e segurança", "Mova-se devagar e só dentro de uma amplitude confortável. Pare imediatamente se sentir dor, tontura ou dormência.")],
    more="Ler o texto completo",
    end_h="Faça sua primeira pausa hoje.", end_s="Na App Store, para iPhone e iPad.",
    disclaimer="O Nodly é um app de bem-estar, não um dispositivo médico.",
    nav={"privacy": "Privacidade", "terms": "Termos", "health": "Saúde e segurança", "support": "Suporte"},
    home="Início",
    health_title="Saúde e segurança",
)
