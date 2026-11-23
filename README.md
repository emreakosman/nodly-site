# Nodly web sitesi

Nodly'nin tanıtım sayfası ve yasal metinleri. Statik HTML; derleme aracı, çerez ya da izleme yok.

## Sayfalar

| Adres | İçerik |
|---|---|
| `/` | İngilizce landing |
| `/tr/`, `/de/`, `/es/`, `/fr/`, `/ja/` | Diğer dillerde landing |
| `/privacy/` · `/tr/gizlilik/` | Gizlilik Politikası |
| `/terms/` · `/tr/kosullar/` | Kullanım Koşulları |
| `/health/` · `/tr/saglik/` | Sağlık ve güvenlik |
| `/support/` · `/tr/destek/` | Destek (App Store Connect'teki Support URL) |

Sağ üstteki dil menüsü aynı sayfanın diğer dillerdeki karşılığını açar. Diğer dillerin yasal sayfa adresleri `scripts/build.py` içindeki `ROUTES`'tadır. İspanyolca tek sürümdür; uygulamadaki iki İspanyolca da `/es/`'e gider.

## Değiştirmek

Sayfalar `scripts/build.py` ile üretilir; `index.html` dosyalarını elle düzenlemeyin.

- Landing ve destek metinleri: her dil için `content/site/<dil>.py` (`T` ve `SUPPORT`).
- Yasal metinler: TR ve EN için `content/legal/*.md` (Nodly/legal klasöründeki dosyaların kopyası); DE, ES, FR, JA için çevirileri `content/legal/<dil>/`. Asıl metin değişince çevirileri de güncelleyin.
- Yeni dil: `LANGS` ve `ROUTES`'a ekleyin, `content/site/<dil>.py` ve `content/legal/<dil>/` dosyalarını yazın, uygulamadan o dilde ekran görüntülerini `assets/img/` altına koyun.
- App Store bağlantısı: `scripts/build.py` içindeki `APP_STORE_URL`.
- Görünüm: `assets/style.css`.

Değişiklikten sonra:

```bash
python3 scripts/build.py
```

Yerelde bakmak için:

```bash
python3 -m http.server 8765
```

Ardından tarayıcıda `http://localhost:8765/tr/` adresini açın.

## GitHub Pages ile yayınlamak

1. GitHub'da yeni bir depo açın (ör. `nodly-site`).
2. Bu klasörü o depoya gönderin.
3. Depoda **Settings › Pages** bölümünde **Source: Deploy from a branch**, dal `main`, klasör `/ (root)` seçin.
4. Birkaç dakika sonra site `https://<kullanıcı-adı>.github.io/nodly-site/` adresinde açılır.
5. Kendi alan adınız için: **Settings › Pages › Custom domain** alanına alan adını yazın ve alan adı sağlayıcınızda GitHub'ın gösterdiği DNS kaydını ekleyin.

Bağlantıların hepsi göreli olduğu için site hem alt yolda hem de kendi alan adında çalışır.

## Yayından önce

- `content/legal/*.md` içindeki `{{EMAIL}}`, `{{ADRES}}`/`{{ADDRESS}}`, `{{DOMAIN}}`, `{{YURURLUK_TARIHI}}`/`{{EFFECTIVE_DATE}}`, `{{BEKLEME_LISTESI_SAGLAYICISI}}`/`{{WAITLIST_PROVIDER}}` ve `{{KONUM}}`/`{{LOCATION}}` yer tutucularını doldurun.
- Yasal metinler taslaktır; yayından önce bir avukata kontrol ettirilmesi önerilir (bkz. Nodly/legal/README.md).
- Destek sayfasındaki `{{EMAIL}}` da doldurulmalı. Sayfa, uygulamada henüz yapılmamış abonelik ekranındaki "Satın Alımları Geri Yükle" ve Ayarlar › Aboneliği Yönet adımlarını anlatıyor; abonelik ekranı yapılınca bu adlar kontrol edilmeli.
