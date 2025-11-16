# PES 2017 Gerçekçilik Modu - Oyuncu Deneyimi Rehberi

**Mod Hedefi:** Arcade futbol oyunu → Gerçekçi futbol simülasyonu  
**Hedef Oyuncu:** "PES çok kolay/arcade" diyenler için

---

## 🎮 OYUNDA SANA NASIL ETKİ EDER?

### ⚽ **1. TOP KONTROLÜ - Artık Top "Yapışmıyor"**

#### ❌ **Eski PES (Orijinal):**
- Top ayağına yapışıyor gibi
- Sektirmeler çok yüksek (0.70 bounce rate)
- Top hiç durmuyor, sürekli kayıyor
- Uzun paslar süper kolay, top çok hafif

#### ✅ **Yeni PES (Gerçekçilik Modu):**
```
Top Fiziği:
├─ Sıçrama: %11 daha az (0.62) → Top ağır hissediliyor
├─ Sürtünme: %2 artış → Top çabuk yavaşlıyor
└─ Durma Hızı: +26% → Top çabuk "durmuş" sayılıyor
```

**OYUNDA NE DEĞİŞTİ:**
- ✅ **İlk Dokunuş Önemli:** Top geldiğinde R2 ile kontrol etmezsen uzağa gidiyor
- ✅ **Uzun Pas Zor:** Top havada daha çabuk yavaşlıyor, mesafe hesabı lazım
- ✅ **Sektirmeler Gerçekçi:** Yer pasları daha kontrollü, arcade sektirme yok
- ✅ **Şut Sonrası:** Kaleciden seken toplar çok uzağa gitmez
- ⚠️ **DİKKAT:** Hızlı pas oyununda tempo düşebilir (daha gerçekçi)

**ÖRNEK SENARYO:**
> Eski: Uzun pas → Top 40 metre süzülerek gidiyor → Oyuncu rahat kontrol ediyor  
> Yeni: Uzun pas → Top 30 metrede yavaşlıyor → Rakip öne çıkıp kesiyor (gerçekçi!)

---

### 🤖 **2. YAPAY ZEKA - AI Artık "Süper İnsan" Değil**

#### ❌ **Eski PES (Orijinal):**
- CPU 0 frame'de tepki veriyor (robot gibi)
- Şut atmadan önce kaleci zaten hazır
- Her pas mükemmel, hiç hata yok
- Düşük seviyede bile AI çok iyi

#### ✅ **Yeni PES (Gerçekçilik Modu):**
```
AI Tepki Süreleri:
├─ Şut Tepkisi: 5→8 frame (+60%) → Sen şut çekerken AI geç tepki veriyor
├─ Pas Tepkisi: 5→8 frame (+60%) → AI paslarda düşünüyor
├─ Kaleci: 5→8 frame (+60%) → Kaleci geç çıkıyor
└─ Dribbling Savunması: 5→10 frame (2x yavaş!) → Dribblingin etkili
```

**OYUNDA NE DEĞİŞTİ:**
- ✅ **Daha Çok Gol Atıyorsun:** Kaleciler geç tepki veriyor, yakın şutlar gol oluyor
- ✅ **Dribbling İşe Yarıyor:** Defender 10 frame geç tepki veriyor → Feint'ler çalışıyor
- ✅ **1v1 Kolay:** Kaleci 8 frame geç çıkıyor → Lob şut/yan şut açık
- ✅ **AI Pas Hataları:** CPU artık bazen yanlış pas yapıyor (insan gibi)
- ⚠️ **DİKKAT:** Düşük seviyelerde oyun ÇOK kolay olabilir

**ÖRNEK SENARYO:**
> Eski: Ceza sahası önü şut → Kaleci zaten hazır → Kurtarıyor  
> Yeni: Ceza sahası önü şut → Kaleci 8 frame (0.13 saniye) geç tepki → **GOL!**

---

### 💪 **3. KONDISYON - 60. Dakika Sonrası Oyun Değişiyor**

#### ❌ **Eski PES (Orijinal):**
- Metabolism 10 → Çok hızlı toparlanma
- Sprint spam yapabiliyorsun
- 90. dakikada bile oyuncular fresh

#### ✅ **Yeni PES (Gerçekçilik Modu):**
```
Yorulma Faktörleri:
├─ Sprint Yorgunluğu: 1→2 (2x hızlı yorulma)
├─ Dribbling: 2→3 (+50%)
├─ Fiziksel Temas: 5→7 (+40%)
├─ Dash Stamina: 5→7 (+40%)
└─ Toparlanma: 10→7 (-30% YAVAS!) ⚠️
```

**OYUNDA NE DEĞİŞTİ:**
- ✅ **60+ Dakika Kritik:** Oyuncular yorgun, süper sub önemli
- ✅ **Sprint Dikkatli Kullan:** R1 spam yapınca oyuncu 70. dakikada bitik
- ✅ **Fiziksel Oyun Riskli:** Defender'ın sürekli itişince yoruluyor
- ✅ **Taktik Değişiklik Önemli:** Counter attack → Ball possession gerekebilir
- ⚠️ **DİKKAT:** Yavaş oyuncular 60+ dakikada daha da yavaş

**ÖRNEK SENARYO:**
> Eski: 90. dakika → Ronaldo hala sprint atıyor  
> Yeni: 90. dakika → Ronaldo yorgun (sarı kondisyon) → Yedekten fresh oyuncu lazım

---

### 🚑 **4. SAKATLIKLАР - Fiziksel Oyunun Bedeli Var**

#### ❌ **Eski PES (Orijinal):**
- Sakatlık eşikleri yüksek (120-240)
- Fiziksel oyun riskiz

#### ✅ **Yeni PES (Gerçekçilik Modu):**
```
Sakatlık Eşikleri: (%4-17 daha kolay sakatlanma)
├─ Hafif: 120→100 (-17%)
├─ Küçük: 180→150 (-17%)
├─ Orta: 220→200 (-9%)
└─ Ciddi: 240→230 (-4%)
```

**OYUNDA NE DEĞİŞTİ:**
- ✅ **Sliding Tackle Riskli:** Çok kullanınca oyuncun sakatlanabilir
- ✅ **Fiziksel Oyuncular Risk Altında:** Power striker'lar 70+ dakikada dikkat
- ✅ **Yedek Kullanımı:** 3 değişikliği kullanman önemli
- ⚠️ **DİKKAT:** Master League'de sakatlık riski arttı

**ÖRNEK SENARYO:**
> Eski: Sliding tackle spam → Sakatlık yok  
> Yeni: Sliding tackle spam → 75. dakika → Defender ayak bileği sakatlığı → Oyundan çıkıyor

---

### 🎯 **5. DRIBBLING & FEİNT - Artık Çok Etkili**

#### ❌ **Eski PES (Orijinal):**
- AI 5 frame'de tepki veriyor
- Feint yapınca defender hemen dönüyor

#### ✅ **Yeni PES (Gerçekçilik Modu):**
```
Dribbling Değişiklikleri:
├─ AI Tepki: 5→10 frame (2x yavaş!)
├─ ballplayerFeint.json: +3,771 bytes (büyük değişiklik)
└─ ballplayerDribble.json: +1,695 bytes
```

**OYUNDA NE DEĞİŞTİ:**
- ✅ **Feint Çalışıyor:** Roulette/Marseille turn yaptığında defender 10 frame geç tepki → Geçiyorsun!
- ✅ **Skill Move Oyuncular Değerli:** Neymar/Hazard gibi oyuncular çok etkili
- ✅ **1v1 Kolay:** Close control dribbling ile defender'ı geçebiliyorsun
- ⚠️ **DİKKAT:** Yavaş dribbler'lar (70-75 dribbling) hala zor

**ÖRNEK SENARYO:**
> Eski: Roulette → Defender 5 frame'de dönüyor → Topu kesiyor  
> Yeni: Roulette → Defender 10 frame geç → **Geçtin!** → 1v1 kaleci

---

### 🛡️ **6. SAVUNMA - AI Daha Pasif**

#### ❌ **Eski PES (Orijinal):**
- AI her yerde press yapıyor
- Defender 12 frame'de topa geliyor

#### ✅ **Yeni PES (Gerçekçilik Modu):**
```
Savunma AI:
├─ Kick Reaction: 12→18 frame (Seviye 1'de 50% yavaş)
├─ Press: Orta seviyelerde daha az agresif
└─ Sandwiching: 3. seviyede aktif (daha gerçekçi)
```

**OYUNDA NE DEĞİŞTİ:**
- ✅ **Daha Çok Alan:** AI sana daha çok alan veriyor, build-up kolay
- ✅ **Ceza Sahası Rahat:** Ceza sahasında daha az basınç
- ⚠️ **DİKKAT:** Düşük seviyeler ÇOK kolay olabilir

---

## 📊 OYUN STİLİNE ETKİSİ

### **Eski Oyun Stili (Orijinal PES):**
```
Tiki-Taka → Hızlı Paslaşma → Counter Attack → Şut
• Sprint spam çalışıyor
• Uzun pas oyunu dominant
• Kondisyon önemsiz
• Dribbling zor
```

### **Yeni Oyun Stili (Gerçekçilik Modu):**
```
Build-Up → Dribbling → Şut Alanı Bulma → Gol
• Sprint dikkatli kullanılmalı (kondisyon)
• Kısa pas + dribbling kombinasyonu
• 60+ dakika rotasyon/taktik değişikliği
• Feint/skill move çalışıyor
• Kaleciye karşı daha çok gol
```

---

## 🎮 ZORLUK SEVİYESİ ETKİSİ

| Seviye | Orijinal PES | Gerçekçilik Modu |
|--------|--------------|------------------|
| **1 (Beginner)** | Çok Kolay | ÇOK ÇOK KOLAY (AI tepki 18 frame!) |
| **2 (Amateur)** | Kolay | Kolay (AI tepki 12 frame) |
| **3 (Regular)** | Orta | Orta-Kolay (AI tepki 8 frame) |
| **4 (Professional)** | Zor | Orta (AI tepki 5 frame) |
| **5 (Top Player)** | Çok Zor | Orta-Zor (AI tepki 3 frame) |
| **6 (Superstar)** | Ultra Zor | Zor (AI tepki 2 frame) |

**ÖNERİ:** Normalde 4. seviyede oynuyorsan → 5-6. seviyeye çık (çünkü AI yavaşladı)

---

## ⚠️ DİKKAT EDİLMESİ GEREKENLER

### ❌ **Potansiyel Sorunlar:**
1. **Düşük Seviyeler ÇOK Kolay:** 1-2. seviye oynamana gerek yok
2. **Kondisyon Erken Biter:** 60+ dakika dikkatli oyna
3. **Uzun Pas Zor:** Top fiziği değişti, timing lazım
4. **Oyun Temposu Yavaş:** Arcade hız kayboldu (gerçekçilik için fedakarlık)

### ✅ **Avantajlar:**
1. **Daha Çok Gol:** Kaleciler zayıf, 1v1'ler kolay
2. **Dribbling Eğlenceli:** Skill move'lar çalışıyor
3. **Taktik Önemli:** Rotasyon/takım yönetimi kritik
4. **Gerçekçi Futbol:** Fizik yasaları + insan hataları

---

## 🎯 HANGİ OYUNCULARA UYGUN?

### ✅ **Sana Uygun:**
- ❤️ "PES çok kolay" diyenler
- ❤️ Gerçekçilik seven oyuncular
- ❤️ Takım yönetimi seven oyuncular (kondisyon/rotasyon)
- ❤️ Dribbling seven oyuncular
- ❤️ Taktiksel futbol seven oyuncular

### ❌ **Sana Uygun Değil:**
- 💔 Arcade hız isteyenler
- 💔 "Kolay mod" sevenlerse (1-3. seviye oynamaya alışkınsan)
- 💔 Sprint spam yapmayı sevenler
- 💔 "Hızlı maç bitsin" diyenler

---

## 📝 ÖZET: OYUNDA NASIL HİSSEDERSİN?

### **İLK 10 DAKİKA:**
> "Top biraz ağır hissediliyor... Kaleci şutu tutamadı? Vay be!"

### **30. DAKİKA:**
> "Dribbling çok iyi çalışıyor! Feint yaptım defender dondu kaldı 😄"

### **60. DAKİKA:**
> "Oyuncular yorulmaya başladı, hızım düştü... Değişiklik yapmalıyım"

### **75. DAKİKA:**
> "Defender sliding tackle yaptı ama sakatlandı, oyundan çıktı! Gerçekçi!"

### **90. DAKİKA:**
> "Yorgun takım ama fresh yedekler fark yarattı. Gerçek futbol gibi!"

---

## 🏆 SONUÇ

Bu mod **PES 2017'yi farklı bir oyuna dönüştürüyor:**

**Eski PES:**
- Arcade futbol oyunu
- Hızlı tempolu
- AI mükemmel robot
- Kondisyon önemsiz
- Sprint spam

**Yeni PES (Gerçekçilik Modu):**
- Futbol simülasyonu
- Gerçekçi tempo
- AI insan gibi hata yapıyor
- Kondisyon yönetimi kritik
- Taktiksel derinlik

### **Tek Cümle:**
> "Artık futbol oynamak yerine **futbol yönetiyorsun** - kondisyon, rotasyon, taktik, sakatlık... Gerçek futbol gibi!"

---

**Not:** İlk 2-3 maç alışma süresi gerekebilir. Top fiziği ve AI farklı olduğu için alışman lazım. Sonra gerçekçiliği seveceksin! 🎮⚽
