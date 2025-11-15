# DT18 Fox Engine Configuration

## 📖 Proje Hakkında

Bu repository, Fox Engine 2.0 tabanlı bir futbol oyununun (PES/eFootball serisi) AI, fizik ve taktik konfigürasyon dosyalarını içermektedir.

## 📁 Dizin Yapısı

```
common/match/
├── ai/              # Yapay zeka konfigürasyonları
│   ├── player/      # Oyuncu AI (stamina, defence, offence)
│   ├── team/        # Takım AI (formations, tactics)
│   └── judge/       # Hakem ve yaralanma sistemleri
├── ball/            # Top fiziği parametreleri
├── pad/             # Kontrol şemaları (feint, shoot, defence)
├── constant/        # Sabit değerler (binary)
├── selector/        # Karar ağaçları
├── situation/       # Oyun durumları
└── team_action/     # Takım aksiyonları
```

## 🎯 Dosya Türleri

- **JSON** (33 dosya): Ana konfigürasyon dosyaları - İnsan tarafından okunabilir
- **XML** (16 dosya): Behavior tree'ler ve kontrol şemaları
- **FOX** (167 dosya): Oyuncu pozisyon varlıkları (XML variant)
- **BIN** (199 dosya): Binary/derlenmiş veriler

## ⚠️ Önemli Uyarılar

1. **YEDEKLEME ZORUNLU**: Değişiklik yapmadan önce mutlaka yedek alın
2. **BIN dosyaları**: Proprietary format - düzenlemeyin
3. **FOX dosyaları**: Özel araç gerektirir - dikkatli değiştirin
4. **Encoding**: JSON dosyaları Shift-JIS Japonca yorumlar içerir

## 🔧 Değişiklik Yapma Rehberi

### Düşük Risk (JSON)
- `cpuLevel.json` - AI zorluk seviyeleri
- `stamina.json` - Oyuncu yorgunluk sistemi
- `ball.json` - Top fiziği

### Orta Risk (XML)
- `shoot.xml` - Şut kontrolleri
- `defence.xml` - Savunma kontrolleri
- `patternSelector.xml` - AI karar ağaçları

### Yüksek Risk (FOX)
- `positionKickOff_*.fox` - Formasyon pozisyonları
- `positionCK_*.fox` - Korner pozisyonları

### ÇOK YÜKSEK RİSK (BIN)
- `*.bin` - DOKUNMAYIN!

## 🛠️ Gerekli Araçlar

- **VS Code Eklentileri**:
  - Prettier (JSON formatting)
  - XML Tools (XML editing)
  - GitLens (version control)
  - Hex Editor (BIN inspection only)

## 📊 Önemli Parametreler

### AI Zorluk (cpuLevel.json)
```json
"dfKickReactionAddWait": [12, 8, 4, 3, 0, 0]  // 0=En kolay, 5=En zor
```

### Top Fiziği (ball.json)
```json
"boundRate": 0.70,        // Zıplama oranı
"frictionBoundRate": 0.968 // Sürtünme
```

### Formasyon (basePosition.json)
```json
"lengthOf": 40.0,  // Hücum hattı derinliği
"lengthDf": 25.0   // Savunma hattı derinliği
```

## 🚀 Başlangıç

1. Repository'yi clone edin
2. Değişiklik öncesi branch oluşturun: `git checkout -b feature/my-changes`
3. JSON dosyalarını düzenleyin (XML/FOX için dikkatli olun)
4. Değişiklikleri test edin
5. Commit ve push yapın

## 📝 Lisans

Proprietary - Fox Engine (Konami)

## 🤝 Katkıda Bulunma

Değişiklik yapmadan önce:
1. Issue açın
2. Branch oluşturun
3. Test edin
4. Pull request gönderin

---

**Son Güncelleme**: 16 Kasım 2025  
**Motor**: Fox Engine 2.0  
**Dosya Sayısı**: 415 dosya
