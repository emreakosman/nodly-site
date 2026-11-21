# Nodly web sitesi

Nodly'nin tanıtım sayfası ve yasal metinleri. Statik HTML; derleme aracı, çerez ya da izleme yok.

## Sayfalar

| Adres | İçerik |
|---|---|
| `/` | İngilizce landing |
| `/tr/` | Türkçe landing |
| `/privacy/` · `/tr/gizlilik/` | Gizlilik Politikası |
| `/terms/` · `/tr/kosullar/` | Kullanım Koşulları |
| `/health/` · `/tr/saglik/` | Sağlık ve güvenlik |

Her sayfanın sağ üstündeki buton, aynı sayfanın diğer dildeki karşılığını açar.

## Değiştirmek

Sayfalar `scripts/build.py` ile üretilir; `index.html` dosyalarını elle düzenlemeyin.

- Landing metinleri: `scripts/build.py` içindeki `T` sözlüğü.
- Yasal metinler: `content/legal/*.md` (Nodly/legal klasöründeki dosyaların kopyası). Asıl dosya değişince buraya yeniden kopyalayın.
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
- App Store, ayrıca zorunlu bir destek sayfası (`/support`) ister; henüz yok.
