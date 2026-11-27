"""Site copy in tr. Read by scripts/build.py."""

SUPPORT = """# Destek

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
"""

T = dict(
    lang="tr", lang_label="Dil",
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
    demo_reps="Tekrar",
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
             ("globe", "12 dil", "Türkçe, İngilizce, Almanca, İspanyolca, Fransızca, İtalyanca, Portekizce, Felemenkçe, Rusça, Japonca, Korece ve Çince (Basitleştirilmiş ve Geleneksel).")],
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
    home="Ana sayfa",
    health_title="Sağlık ve güvenlik",
)
