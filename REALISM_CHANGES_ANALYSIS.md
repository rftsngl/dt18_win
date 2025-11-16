# PES 2017 Gerçekçilik Modu - Değişiklik Analizi

**Tarih:** 16 Kasım 2025  
**Mod Hedefi:** Tam Gerçekçilik (Realistic Simulation)  
**Değiştirilen Dosya Sayısı:** 12 JSON dosyası

---

## 📊 Genel Değişiklikler Özeti

### 🎮 **1. CPU Zorluk Seviyesi** (`cpuLevel.json`)

#### Savunma Tepki Süreleri (Daha Zor)
- **Kick Reaction Delay** (Topa tepki):
  - Orijinal: `[12, 8, 4, 3, 0, 0]` frame
  - Yeni: `[18, 12, 8, 5, 3, 2]` frame
  - **Etki:** Düşük seviyelerde AI daha yavaş tepki veriyor (12→18), üst seviyelerde her seviye aktif (0→2-5)

- **Dribble Reaction Delay** (Dribblingin karşı tepki):
  - Orijinal: `[5, 5, 3, 3, 0, 0]` frame
  - Yeni: `[10, 8, 6, 4, 3, 2]` frame
  - **Etki:** Tüm seviyelerde dribbling daha etkili (2-5 kat daha yavaş tepki)

#### Savunma Taktikleri
- **Sandwiching** (İkili kapama):
  - Orijinal: `[0, 0, 0, 1, 1, 1]`
  - Yeni: `[0, 0, 1, 1, 1, 1]`
  - **Etki:** Orta zorlukta bile aktif (3. seviye), gerçekçi savunma

#### Hücum Oyuncu Tepkileri (Daha Yavaş)
- **Shoot Timing Delay**:
  - Orijinal: `[5, 3, 3, 1, 0, 0]` frame
  - Yeni: `[8, 6, 4, 3, 2, 1]` frame
  - **Etki:** AI'ın şut zamanlaması daha insani (%60 daha yavaş)

- **Pass Timing Delay**:
  - Orijinal: `[5, 3, 3, 1, 0, 0]` frame
  - Yeni: `[8, 6, 4, 3, 2, 1]` frame
  - **Etki:** Pas kararları daha yavaş, gerçek oyuncular gibi

#### Kaleci Tepkileri
- **GK Kick Reaction Delay**:
  - Orijinal: `[5, 3, 3, 2, 0, 0]` frame
  - Yeni: `[8, 6, 4, 3, 2, 1]` frame
  - **Etki:** Kaleciler daha geç müdahale ediyor, daha çok gol!

---

### ⚽ **2. Top Fiziği** (`ball.json`)

#### Gerçekçi Top Davranışı
- **Bound Rate** (Sıçrama oranı):
  - Orijinal: `0.70`
  - Yeni: `0.62`
  - **Etki:** %11 daha az sıçrama → top daha ağır hissediliyor

- **Friction Bound Rate** (Sürtünme sıçraması):
  - Orijinal: `0.968`
  - Yeni: `0.950`
  - **Etki:** Top yerde daha çabuk yavaşlıyor (gerçek futbol topu davranışı)

- **Friction Roll Rate Max/Min** (Yuvarlanma sürtünmesi):
  - Orijinal: `Max: 0.990, Min: 0.988`
  - Yeni: `Max: 0.982, Min: 0.980`
  - **Etki:** Top zemin üzerinde daha hızlı duruyor

- **Stop Speed** (Durma hızı):
  - Orijinal: `0.175`
  - Yeni: `0.22`
  - **Etki:** Top daha erken "durmuş" sayılıyor (oyun akışı daha dinamik)

- **Drag Speed Max** (Maksimum hava direnci):
  - Orijinal: `105.0`
  - Yeni: `90.0`
  - **Etki:** Yüksek hızlarda hava direnci daha erken devreye giriyor

**SONUÇ:** Top daha gerçekçi fizik kurallarına uyuyor, arcade hissi azaltıldı.

---

### 💪 **3. Oyuncu Kondisyonu** (`stamina.json`)

#### Yorulma Faktörleri (Daha Hızlı Yorulma)
- **Defence Tired** (Savunma yorgunluğu):
  - Orijinal: `1`
  - Yeni: `2`
  - **Etki:** %100 artış, savunma yapınca 2 kat hızlı yorulma

- **Dribble Tired** (Dribbling yorgunluğu):
  - Orijinal: `2`
  - Yeni: `3`
  - **Etki:** %50 artış, dribbling daha riskli

- **Speed Tired** (Hız yorgunluğu):
  - Orijinal: `1`
  - Yeni: `2`
  - **Etki:** %100 artış, sprint kullanımı cezalandırılıyor

- **Contact Tired** (Fiziksel temas yorgunluğu):
  - Orijinal: `5`
  - Yeni: `7`
  - **Etki:** %40 artış, fiziksel oyun daha yıpratıcı

- **Jostle Tired** (İtişme yorgunluğu):
  - Orijinal: `2`
  - Yeni: `3`
  - **Etki:** %50 artış

- **Metabolism** (Temel metabolizma - toparlanma):
  - Orijinal: `10`
  - Yeni: `7`
  - **Etki:** %30 daha yavaş toparlanma → oyun sonuna doğru yorgunluk belirgin

- **Dash Tired** (Dash stamina):
  - Orijinal: `5`
  - Yeni: `7`
  - **Etki:** %40 artış, dash kullanımı pahalı

**SONUÇ:** Kondisyon yönetimi kritik hale geldi, gerçekçi futbol simülasyonu.

---

### 🚑 **4. Sakatlık Sistemi** (`injury.json`)

#### Sakatlık Eşikleri (Daha Dayanıklı Oyuncular)
- **Micro Injury** (Hafif sakatlık):
  - Orijinal: `120/255`
  - Yeni: `100/255`
  - **Etki:** %17 daha kolay hafif sakatlık

- **Minor Injury** (Küçük sakatlık):
  - Orijinal: `180/255`
  - Yeni: `150/255`
  - **Etki:** %17 düşük eşik

- **Middle Injury** (Orta sakatlık):
  - Orijinal: `220/255`
  - Yeni: `200/255`
  - **Etki:** %9 düşük eşik

- **Serious Injury** (Ciddi sakatlık):
  - Orijinal: `240/255`
  - Yeni: `230/255`
  - **Etki:** %4 düşük eşik

**SONUÇ:** Oyuncular daha gerçekçi şekilde sakatlanıyor (ama aşırı değil). Fiziksel oyunun bedeli var.

---

### 🎯 **5. Hücum AI Dosyaları** (4 Dosya Değiştirildi)

#### Dosya Boyut Değişiklikleri
1. **ballplayerDribble.json**: +1,695 bytes (yeni parametreler/ayarlar)
2. **ballplayerFeint.json**: +3,771 bytes (büyük değişiklikler)
3. **ballplayerPass.json**: +1,082 bytes
4. **ballplayerShoot.json**: +1,199 bytes

**TOPLAM:** +7,747 bytes ekstra veri → AI davranışları daha detaylı kontrol ediliyor

#### Muhtemel Değişiklikler (Satır sayısı sabit):
- Dribbling hız/mesafe parametreleri
- Feint (çalım) başarı oranları ve zamanlamaları
- Pas karar algoritmaları (risk/ödül dengesi)
- Şut açısı/mesafe hesaplamaları

---

### 🛡️ **6. Savunma AI Dosyaları** (3 Dosya Değiştirildi)

1. **defence.json** - Temel savunma mantığı
2. **defenceCover.json** - Destek savunma
3. **defenceMark.json** - Adam markajı

*(Detaylı analiz yapılamadı - boyut/satır karşılaştırması yapılabilir)*

---

### 📈 **7. Taktik Dosyası**

- **passSupport.json** - Pas desteği AI'sı değiştirildi

---

## 🎮 Oynanış Üzerindeki Etkiler

### ✅ **Pozitif Değişiklikler:**
1. **Daha Gerçekçi Top:** Fizik yasalarına uygun, ağırlık hissi var
2. **Kondisyon Yönetimi:** Rotasyon ve taktik değişiklikler önemli
3. **Sakatlık Riski:** Fiziksel oyun bedeli var (ama abartısız)
4. **AI Hataları:** CPU "mükemmel robot" gibi oynamıyor
5. **Kaleci Hataları:** Daha çok gol, daha heyecanlı maçlar
6. **Gerçekçi Zorluk:** Her seviye aktif (arcade 0 değerleri kaldırıldı)

### ⚠️ **Potansiyel Sorunlar:**
1. **Kolay Mod Çok Zor:** İlk seviyede bile AI yavaşlatıldı
2. **Uzun Paslar:** Top fiziği değişince uzun pas mekaniği etkilenebilir
3. **Kondisyon Erken Biter:** 60. dakikadan sonra oyuncular yorgun
4. **CPU Savunması Zayıf:** Reaction delay artışı çok fazla olabilir

---

## 📁 Değiştirilen Dosyalar Listesi

```
dt18_win/common/match/
├── ai/
│   ├── cpuLevel.json ⭐⭐⭐ (Büyük değişiklikler)
│   ├── judge/
│   │   └── injury.json ⭐⭐ (Orta değişiklikler)
│   ├── player/
│   │   ├── stamina.json ⭐⭐⭐ (Büyük değişiklikler)
│   │   └── offence/
│   │       ├── ballplayerDribble.json ⭐⭐
│   │       ├── ballplayerFeint.json ⭐⭐⭐
│   │       ├── ballplayerPass.json ⭐⭐
│   │       └── ballplayerShoot.json ⭐⭐
│   └── team/
│       ├── defence/
│       │   ├── defence.json ⭐
│       │   ├── defenceCover.json ⭐
│       │   └── defenceMark.json ⭐
│       └── offence/
│           └── passSupport.json ⭐
└── ball/
    └── ball.json ⭐⭐⭐ (Büyük değişiklikler)
```

---

## 🎯 Sonuç

Bu mod **"Arcade → Simulation"** dönüşümü yapıyor:

### Felsefe:
- ❌ Arcade mükemmellik (CPU 0 frame reaction, mükemmel pas/şut)
- ✅ İnsan benzeri hatalar (yavaş tepki, fizik yasaları, yorgunluk)

### Hedef Kitle:
- Gerçekçilik isteyen oyuncular
- Kondisyon yönetimi seven oyuncular
- Fiziksel oyun bedeli görmek isteyenler
- "CPU çok kolay" diyenler için zorlu mod

### Risk:
- Oyun çok zor olabilir (özellikle düşük seviyelerde)
- Alışma süresi gerekebilir
- Bazı oyuncular "yavaş/sıkıcı" bulabilir

---

**Not:** Bu değişiklikler "Tam Gerçekçilik" hedefi doğrultusunda yapılmış. EDITABLE_FEATURES.md'deki "Realistic Simulation" senaryosu ile uyumlu.
