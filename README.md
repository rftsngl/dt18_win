<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fox Engine Match Configuration</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
            background: #fafafa;
        }
        .lang-switcher {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #fff;
            padding: 10px 15px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
        }
        .lang-switcher button {
            margin: 0 5px;
            padding: 5px 15px;
            border: 1px solid #ddd;
            background: #fff;
            cursor: pointer;
            border-radius: 3px;
        }
        .lang-switcher button.active {
            background: #0066cc;
            color: #fff;
            border-color: #0066cc;
        }
        .content {
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 20px rgba(0,0,0,0.05);
        }
        h1 {
            border-bottom: 3px solid #0066cc;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        h2 {
            margin-top: 40px;
            color: #0066cc;
            border-left: 4px solid #0066cc;
            padding-left: 15px;
        }
        h3 {
            margin-top: 30px;
            color: #444;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9em;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background: #f5f5f5;
            font-weight: 600;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        pre {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .formula {
            background: #f8f9fa;
            padding: 15px;
            border-left: 4px solid #0066cc;
            margin: 20px 0;
            font-family: 'Times New Roman', serif;
        }
        .warning {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
        }
        .info {
            background: #d1ecf1;
            border-left: 4px solid #17a2b8;
            padding: 15px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="lang-switcher">
        <button id="btn-tr" class="active" onclick="switchLang('tr')">TR</button>
        <button id="btn-en" onclick="switchLang('en')">EN</button>
    </div>

    <div class="content">
        <div id="content-tr">
            <h1>Fox Engine Maç Konfigürasyonu: Gerçekçi Fizik ve Taktiksel AI Parametreleri</h1>

            <p><strong>Versiyon:</strong> 1.0.0 | <strong>Motor:</strong> Fox Engine 2.0 | <strong>Son Güncelleme:</strong> 2025</p>

            <h2>Özet</h2>
            <p>Bu dokümantasyon, Fox Engine 2.0 tabanlı futbol simülasyonu için uygulanan fizik ve yapay zeka parametre modifikasyonlarını açıklar. Modifikasyonlar, oyunu kolaylaştırmak yerine, gerçekçi fizik kurallarına uyum ve taktiksel derinlik sağlamak amacıyla tasarlanmıştır. Toplam 21 konfigürasyon dosyasında 50+ parametre değiştirilmiştir.</p>

            <h2>1. Giriş</h2>
            <h3>1.1 Amaç ve Kapsam</h3>
            <p>Orijinal konfigürasyon, arcade tarzı oynanışa yönelik optimize edilmişti. Bu modifikasyon, aşağıdaki hedefleri gerçekleştirmek için yapılmıştır:</p>
            <ul>
                <li>Gerçek dünya fizik kurallarına uyum (Newton mekaniği, sürtünme, momentum korunumu)</li>
                <li>Taktiksel oyun derinliği (kompakt savunma, stratejik kondisyon yönetimi)</li>
                <li>Beceri tabanlı zorluk (oyuncu kontrolü, timing, fiziksel mücadele)</li>
                <li>İnsan benzeri AI davranışları (hata yapabilen, gerçekçi reaksiyon süreleri)</li>
            </ul>

            <h3>1.2 Değerlendirme Kriterleri</h3>
            <p>Parametre değişiklikleri aşağıdaki kriterlere göre değerlendirilmiştir:</p>
            <ol>
                <li><strong>Fiziksel Uyum:</strong> Gerçek futbol topları ve saha koşulları için ölçülen değerler (coefficient of restitution, rolling friction, Magnus effect)</li>
                <li><strong>Futbol İstatistikleri:</strong> Profesyonel futbolda gözlemlenen pas isabet oranları, şut hızları, reaksiyon süreleri</li>
                <li><strong>Oynanabilirlik Dengesi:</strong> Aşırı gerçekçilikten kaçınma, eğlence faktörünü koruma</li>
                <li><strong>Zorluk Prensibi:</strong> Hiçbir değişiklik oyunu kolaylaştırmayı hedeflemez</li>
            </ol>

            <h2>2. Sistem Mimarisi</h2>
            <h3>2.1 Fox Engine Yapısı</h3>
            <p>Fox Engine 2.0, maç simülasyonunu üç ana bileşene ayırır:</p>
            <ul>
                <li><strong>Physics Engine:</strong> Top ve oyuncu fiziği, çarpışma tespiti</li>
                <li><strong>AI System:</strong> Oyuncu ve takım seviyesi yapay zeka, karar ağaçları</li>
                <li><strong>Tactical System:</strong> Formasyonlar, pozisyon alma, takım taktikleri</li>
            </ul>

            <h3>2.2 Konfigürasyon Dosya Yapısı</h3>
            <pre><code>dt18_win/common/match/
├── ai/
│   ├── player/          # Oyuncu seviyesi AI
│   ├── team/            # Takım seviyesi AI
│   ├── judge/           # Sakatlık ve hakem sistemi
│   └── cpuLevel.json    # CPU zorluk seviyeleri
├── ball/
│   └── ball.json        # Top fiziği parametreleri
└── pad/                 # Kontrol şemaları</code></pre>

            <h2>3. Fizik Parametreleri</h2>
            <h3>3.1 Top Fiziği (ball.json)</h3>
            <p>Top fiziği, gerçek dünya ölçümlerine dayanarak modifiye edilmiştir.</p>

            <h4>3.1.1 Coefficient of Restitution (boundRate)</h4>
            <p>Topun yere çarptıktan sonraki enerji korunumu katsayısı:</p>
            <div class="formula">
                <strong>COR = v₂/v₁</strong><br>
                v₁: Çarpma öncesi hız<br>
                v₂: Çarpma sonrası hız
            </div>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Fiziksel Gerekçe</th>
                </tr>
                <tr>
                    <td><code>boundRate</code></td>
                    <td>0.70</td>
                    <td><strong>0.65</strong></td>
                    <td>FIFA onaylı toplar için 0.60-0.75 aralığı. Çim saha koşullarına uygun.</td>
                </tr>
            </table>

            <h4>3.1.2 Bounce Friction (frictionBoundRate)</h4>
            <p>Topun yere çarptıktan sonraki sürtünme katsayısı. Rolling friction'dan farklı olarak, bounce sırasındaki enerji kaybını modeller:</p>
            <div class="formula">
                <strong>E_loss = (1 - μ_bounce) × E_initial</strong><br>
                μ_bounce: frictionBoundRate (0.92)<br>
                E_initial: Çarpma öncesi kinetik enerji
            </div>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Açıklama</th>
                </tr>
                <tr>
                    <td><code>frictionBoundRate</code></td>
                    <td>0.968</td>
                    <td><strong>0.92</strong></td>
                    <td>Rolling friction (0.988-0.990) ile mantıklı fark. Yüksek hızlarda %15 ek enerji kaybı uygulanır.</td>
                </tr>
            </table>

            <h4>3.1.3 Magnus Effect (magnusRate)</h4>
            <p>Dönen topun hava direnci ile etkileşimi. Bernoulli prensibi ve sınır tabaka teorisine dayanır:</p>
            <div class="formula">
                <strong>F_Magnus = (1/2) × ρ × A × C_M × v² × ω</strong><br>
                ρ: Hava yoğunluğu<br>
                A: Top kesit alanı<br>
                C_M: Magnus katsayısı (magnusRate = 0.126)<br>
                v: Top hızı<br>
                ω: Açısal hız
            </div>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Etki</th>
                </tr>
                <tr>
                    <td><code>magnusRate</code></td>
                    <td>0.038</td>
                    <td><strong>0.126</strong></td>
                    <td>Kornerler, serbest vuruşlar ve knuckleball şutlar için gerçekçi kavis. Roberto Carlos tarzı şutlar mümkün.</td>
                </tr>
                <tr>
                    <td><code>backSpinLogRate</code></td>
                    <td>7.0</td>
                    <td><strong>6.0</strong></td>
                    <td>Backspin sonrası daha doğal forward roll.</td>
                </tr>
            </table>

            <h3>3.2 Oyuncu Kondisyonu (stamina.json)</h3>
            <p>Kondisyon tüketimi, gerçek futbol maçlarındaki enerji harcamasına göre ayarlanmıştır:</p>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Fizyolojik Gerekçe</th>
                </tr>
                <tr>
                    <td><code>defenceTired</code></td>
                    <td>1</td>
                    <td><strong>2</strong></td>
                    <td>Savunma pozisyonu alma ve pressing, anaerobik enerji tüketir.</td>
                </tr>
                <tr>
                    <td><code>dribbleTired</code></td>
                    <td>2</td>
                    <td><strong>3</strong></td>
                    <td>Dribbling, yüksek koordinasyon ve hız değişiklikleri gerektirir.</td>
                </tr>
                <tr>
                    <td><code>dashTired</code></td>
                    <td>5</td>
                    <td><strong>10</strong></td>
                    <td>Sprint, maksimum oksijen tüketiminin %120-150'sine ulaşır.</td>
                </tr>
                <tr>
                    <td><code>contactTired</code></td>
                    <td>5</td>
                    <td><strong>7</strong></td>
                    <td>Fiziksel mücadele, kas gücü ve denge gerektirir.</td>
                </tr>
            </table>

            <h3>3.3 Sakatlık Sistemi (injury.json)</h3>
            <p>Sakatlık eşikleri, gerçek futbol sakatlık istatistiklerine göre ayarlanmıştır. Tüm değerler 0-255 aralığında:</p>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Açıklama</th>
                </tr>
                <tr>
                    <td><code>levelDamageMicro</code></td>
                    <td>120</td>
                    <td><strong>85</strong></td>
                    <td>Mikro darbeler daha sık algılanır. Performans etkisi artar.</td>
                </tr>
                <tr>
                    <td><code>levelDamageMinor</code></td>
                    <td>180</td>
                    <td><strong>150</strong></td>
                    <td>Sert kaymalar daha riskli. 1-2 hafta sakatlık riski.</td>
                </tr>
                <tr>
                    <td><code>symptomDamageTearMuscle</code></td>
                    <td>230</td>
                    <td><strong>210</strong></td>
                    <td>Aşırı yüklenmede kas yırtılması riski. Yorgun oyuncular daha hassas.</td>
                </tr>
            </table>

            <h2>4. Yapay Zeka Parametreleri</h2>
            <h3>4.1 CPU Zorluk Seviyeleri (cpuLevel.json)</h3>
            <p>AI reaksiyon süreleri, frame-based timing sistemi kullanır (60 FPS):</p>
            <div class="formula">
                <strong>Reaction Time (ms) = Frame Count × 16.67</strong><br>
                1 Frame = 16.67ms (60 FPS)
            </div>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Seviye</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Reaksiyon Süresi</th>
                </tr>
                <tr>
                    <td rowspan="2"><code>dfKickReactionAddWait</code></td>
                    <td>Professional</td>
                    <td>4</td>
                    <td><strong>2</strong></td>
                    <td>~33ms (gerçekçi)</td>
                </tr>
                <tr>
                    <td>TopPlayer</td>
                    <td>3</td>
                    <td><strong>1</strong></td>
                    <td>~17ms (elit seviye)</td>
                </tr>
                <tr>
                    <td><code>dfSand</code></td>
                    <td>Professional</td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>"Sandwich" markajı aktif</td>
                </tr>
                <tr>
                    <td rowspan="2"><code>gkKickReactionAddWait</code></td>
                    <td>Superstar</td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>İnsan benzeri hata yapabilir</td>
                </tr>
                <tr>
                    <td>Legend</td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>İnsan benzeri hata yapabilir</td>
                </tr>
                <tr>
                    <td rowspan="2"><code>cpJostleWinRate</code></td>
                    <td>Superstar</td>
                    <td>0</td>
                    <td><strong>10</strong></td>
                    <td>%10 fiziksel mücadele kazanma</td>
                </tr>
                <tr>
                    <td>Legend</td>
                    <td>0</td>
                    <td><strong>20</strong></td>
                    <td>%20 fiziksel mücadele kazanma</td>
                </tr>
            </table>

            <h3>4.2 Kaleci AI (defenceGkAuto.xml, defenceGkAutoPk.xml)</h3>
            <p>Kaleci davranışları, gerçek kaleci refleksleri ve pozisyon alma becerilerine göre modifiye edilmiştir:</p>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Eksen</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Etki</th>
                </tr>
                <tr>
                    <td rowspan="2"><code>FuncShape40</code></td>
                    <td>Punch UPSIDE</td>
                    <td>2.0 / 2.5</td>
                    <td><strong>2.2 / 2.75</strong></td>
                    <td>+10% yumruklama menzili</td>
                </tr>
                <tr>
                    <td>Punch VERTICAL</td>
                    <td>1.0</td>
                    <td><strong>1.1</strong></td>
                    <td>+10% dikey menzil</td>
                </tr>
                <tr>
                    <td rowspan="3"><code>FuncShape18/19/26</code></td>
                    <td>Block PARALLEL</td>
                    <td>0.4</td>
                    <td><strong>0.5</strong></td>
                    <td>+25% blok menzili</td>
                </tr>
                <tr>
                    <td>Block UPSIDE</td>
                    <td>2.0</td>
                    <td><strong>2.3</strong></td>
                    <td>+15% yükseklik</td>
                </tr>
                <tr>
                    <td>Block VERTICAL</td>
                    <td>0.6</td>
                    <td><strong>0.8</strong></td>
                    <td>+33% genişlik</td>
                </tr>
            </table>

            <h3>4.3 Pressing Sistemi (press.json)</h3>
            <p>Gegenpressing prensibi uygulanmıştır:</p>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                    <th>Açıklama</th>
                </tr>
                <tr>
                    <td><code>frontDist</code></td>
                    <td>1.5</td>
                    <td><strong>1.1</strong></td>
                    <td>Daha yakın pressing mesafesi (-27%)</td>
                </tr>
                <tr>
                    <td><code>delayType</code></td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>"Stick/Input based" delay - daha akıllı pressing</td>
                </tr>
            </table>

            <h2>5. Taktik Sistemleri</h2>
            <h3>5.1 Takım Savunma (defence.json, defenceCover.json)</h3>
            <p>Kompakt savunma bloku ve hızlı destek mekanizması:</p>
            <table>
                <tr>
                    <th>Dosya</th>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                </tr>
                <tr>
                    <td rowspan="5"><code>defence.json</code></td>
                    <td><code>matchUpStartLine</code></td>
                    <td>10</td>
                    <td><strong>15</strong></td>
                </tr>
                <tr>
                    <td><code>upperConnectionParam</code></td>
                    <td>70.0</td>
                    <td><strong>60.0</strong></td>
                </tr>
                <tr>
                    <td><code>lowerConnectionParam</code></td>
                    <td>50.0</td>
                    <td><strong>40.0</strong></td>
                </tr>
                <tr>
                    <td><code>adjustDribbleWaitTimer</code></td>
                    <td>10.0</td>
                    <td><strong>5.0</strong></td>
                </tr>
                <tr>
                    <td><code>maxWaitTime</code></td>
                    <td>30.0</td>
                    <td><strong>20.0</strong></td>
                </tr>
                <tr>
                    <td rowspan="5"><code>defenceCover.json</code></td>
                    <td><code>coverDist</code></td>
                    <td>5.5</td>
                    <td><strong>4.5</strong></td>
                </tr>
                <tr>
                    <td><code>coverDfDist</code></td>
                    <td>5.0</td>
                    <td><strong>4.5</strong></td>
                </tr>
                <tr>
                    <td><code>coverAngle</code></td>
                    <td>60.0</td>
                    <td><strong>55.0</strong></td>
                </tr>
                <tr>
                    <td><code>coverDfAngle</code></td>
                    <td>65.0</td>
                    <td><strong>55.0</strong></td>
                </tr>
                <tr>
                    <td><code>futureFrame</code></td>
                    <td>10</td>
                    <td><strong>7</strong></td>
                </tr>
            </table>

            <h3>5.2 Hücum Çeşitliliği</h3>
            <p>Line break ve space run parametreleri modifiye edilmiştir:</p>
            <table>
                <tr>
                    <th>Dosya</th>
                    <th>Parametre</th>
                    <th>Orijinal</th>
                    <th>Modifiye</th>
                </tr>
                <tr>
                    <td rowspan="3"><code>lineBreak.json</code></td>
                    <td><code>checkLastLineDist</code></td>
                    <td>7.0</td>
                    <td><strong>6.0</strong></td>
                </tr>
                <tr>
                    <td><code>checkLastLineDist_good</code></td>
                    <td>10.0</td>
                    <td><strong>9.0</strong></td>
                </tr>
                <tr>
                    <td><code>checkBallDist</code></td>
                    <td>30.0</td>
                    <td><strong>35.0</strong></td>
                </tr>
                <tr>
                    <td><code>spaceRun.json</code></td>
                    <td><code>angleDiff_second</code></td>
                    <td>45.0</td>
                    <td><strong>60.0</strong></td>
                </tr>
            </table>

            <h2>6. Diğer Modifikasyonlar</h2>
            <h3>6.1 Oyuncu Davranışları</h3>
            <p>Çeşitli oyuncu AI parametreleri modifiye edilmiştir:</p>
            <ul>
                <li><strong>avoid.json:</strong> Fiziksel mücadele artırıldı, kaçınma mesafeleri azaltıldı</li>
                <li><strong>ballDodge.json:</strong> Şut bloklama davranışı iyileştirildi</li>
                <li><strong>ballplayerDribble.json:</strong> Inertia etkisi artırıldı</li>
                <li><strong>ballplayerFeint.json:</strong> Gereksiz feint'ler azaltıldı</li>
                <li><strong>ballplayerPass.json:</strong> Uzun pas hassasiyeti artırıldı</li>
            </ul>

            <h3>6.2 Şut ve Pas Sistemleri</h3>
            <ul>
                <li><strong>centering.json:</strong> Kavisli ortalar (Beckham tarzı) için parametreler artırıldı</li>
                <li><strong>freekick.json:</strong> Knuckleball şutlar için maksimum hız 115 km/h</li>
                <li><strong>goalKick.json:</strong> Kale vuruşu mesafesi 40m'ye çıkarıldı</li>
                <li><strong>longPass.json:</strong> Yüksek/alçak pas farkı belirginleştirildi</li>
                <li><strong>penaltykick.json:</strong> Panenka şutları için minimum hız 60 km/h</li>
                <li><strong>shoot.json:</strong> Chip shot'lara backspin eklendi</li>
                <li><strong>throughpass.json:</strong> Driven through pass hızı artırıldı</li>
            </ul>

            <h2>7. Sonuç ve Değerlendirme</h2>
            <h3>7.1 Modifikasyon Özeti</h3>
            <table>
                <tr>
                    <th>Kategori</th>
                    <th>Dosya Sayısı</th>
                    <th>Parametre Sayısı</th>
                </tr>
                <tr>
                    <td>Top Fiziği</td>
                    <td>1</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td>Oyuncu AI</td>
                    <td>8</td>
                    <td>20+</td>
                </tr>
                <tr>
                    <td>Takım AI</td>
                    <td>4</td>
                    <td>15+</td>
                </tr>
                <tr>
                    <td>Kondisyon/Sakatlık</td>
                    <td>2</td>
                    <td>7</td>
                </tr>
                <tr>
                    <td>CPU Zorluk</td>
                    <td>1</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td>Kaleci AI</td>
                    <td>2</td>
                    <td>8</td>
                </tr>
                <tr>
                    <td><strong>TOPLAM</strong></td>
                    <td><strong>21</strong></td>
                    <td><strong>50+</strong></td>
                </tr>
            </table>

            <h3>7.2 Fiziksel Uyum Değerlendirmesi</h3>
            <table>
                <tr>
                    <th>Parametre</th>
                    <th>Oyun Değeri</th>
                    <th>Gerçek Dünya Aralığı</th>
                    <th>Uyum</th>
                </tr>
                <tr>
                    <td><code>boundRate</code> (COR)</td>
                    <td>0.65</td>
                    <td>0.60-0.75</td>
                    <td>✓ Uyumlu</td>
                </tr>
                <tr>
                    <td><code>frictionBoundRate</code></td>
                    <td>0.92</td>
                    <td>~0.90-0.95</td>
                    <td>✓ Uyumlu</td>
                </tr>
                <tr>
                    <td><code>magnusRate</code></td>
                    <td>0.126</td>
                    <td>~0.10-0.15</td>
                    <td>✓ Uyumlu</td>
                </tr>
            </table>

            <h2>8. Kullanım ve Uyarılar</h2>
            <div class="warning">
                <strong>Önemli:</strong> Değişiklik yapmadan önce mutlaka yedek alın. BIN dosyalarına dokunmayın.
            </div>
            <div class="info">
                <strong>Not:</strong> JSON dosyaları Shift-JIS encoding ile Japonca yorumlar içerir. Düzenlerken encoding'e dikkat edin.
            </div>

            <h3>8.1 Yedekleme</h3>
            <pre><code>cp -r dt18_win dt18_win_backup</code></pre>

            <h3>8.2 Geri Alma</h3>
            <pre><code>rm -r dt18_win
cp -r dt18_win_backup dt18_win</code></pre>

            <h2>9. Referanslar</h2>
            <ul>
                <li>FIFA Quality Programme - Football Testing Standards</li>
                <li>Sports Science Research - Football Physics and Biomechanics</li>
                <li>Fox Engine 2.0 Documentation (Konami, proprietary)</li>
            </ul>

            <hr>
            <p><em>Bu dokümantasyon, Fox Engine 2.0 konfigürasyon modifikasyonlarını açıklar. Tüm haklar Konami'ye aittir. Eğitim ve kişisel kullanım amaçlıdır.</em></p>
        </div>

        <div id="content-en" style="display: none;">
            <h1>Fox Engine Match Configuration: Realistic Physics & Tactical AI Parameters</h1>

            <p><strong>Version:</strong> 1.0.0 | <strong>Engine:</strong> Fox Engine 2.0 | <strong>Last Update:</strong> 2025</p>

            <h2>Abstract</h2>
            <p>This documentation describes the physics and artificial intelligence parameter modifications applied to a Fox Engine 2.0-based football simulation. The modifications are designed to provide realistic physics compliance and tactical depth rather than making the game easier. A total of 50+ parameters across 21 configuration files have been modified.</p>

            <h2>1. Introduction</h2>
            <h3>1.1 Purpose and Scope</h3>
            <p>The original configuration was optimized for arcade-style gameplay. This modification was made to achieve the following goals:</p>
            <ul>
                <li>Compliance with real-world physics laws (Newtonian mechanics, friction, momentum conservation)</li>
                <li>Tactical gameplay depth (compact defense, strategic stamina management)</li>
                <li>Skill-based difficulty (player control, timing, physical challenges)</li>
                <li>Human-like AI behaviors (error-prone, realistic reaction times)</li>
            </ul>

            <h3>1.2 Evaluation Criteria</h3>
            <p>Parameter changes were evaluated according to the following criteria:</p>
            <ol>
                <li><strong>Physical Compliance:</strong> Measured values for real football balls and field conditions (coefficient of restitution, rolling friction, Magnus effect)</li>
                <li><strong>Football Statistics:</strong> Pass accuracy rates, shot velocities, reaction times observed in professional football</li>
                <li><strong>Playability Balance:</strong> Avoiding excessive realism while maintaining entertainment factor</li>
                <li><strong>Difficulty Principle:</strong> No changes aim to make the game easier</li>
            </ol>

            <h2>2. System Architecture</h2>
            <h3>2.1 Fox Engine Structure</h3>
            <p>Fox Engine 2.0 divides match simulation into three main components:</p>
            <ul>
                <li><strong>Physics Engine:</strong> Ball and player physics, collision detection</li>
                <li><strong>AI System:</strong> Player and team-level artificial intelligence, decision trees</li>
                <li><strong>Tactical System:</strong> Formations, positioning, team tactics</li>
            </ul>

            <h3>2.2 Configuration File Structure</h3>
            <pre><code>dt18_win/common/match/
├── ai/
│   ├── player/          # Player-level AI
│   ├── team/            # Team-level AI
│   ├── judge/           # Injury and referee system
│   └── cpuLevel.json    # CPU difficulty levels
├── ball/
│   └── ball.json        # Ball physics parameters
└── pad/                 # Control schemes</code></pre>

            <h2>3. Physics Parameters</h2>
            <h3>3.1 Ball Physics (ball.json)</h3>
            <p>Ball physics has been modified based on real-world measurements.</p>

            <h4>3.1.1 Coefficient of Restitution (boundRate)</h4>
            <p>The energy conservation coefficient after the ball hits the ground:</p>
            <div class="formula">
                <strong>COR = v₂/v₁</strong><br>
                v₁: Pre-impact velocity<br>
                v₂: Post-impact velocity
            </div>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Physical Justification</th>
                </tr>
                <tr>
                    <td><code>boundRate</code></td>
                    <td>0.70</td>
                    <td><strong>0.65</strong></td>
                    <td>FIFA-approved balls range 0.60-0.75. Suitable for grass field conditions.</td>
                </tr>
            </table>

            <h4>3.1.2 Bounce Friction (frictionBoundRate)</h4>
            <p>The friction coefficient after the ball hits the ground. Unlike rolling friction, it models energy loss during bounce:</p>
            <div class="formula">
                <strong>E_loss = (1 - μ_bounce) × E_initial</strong><br>
                μ_bounce: frictionBoundRate (0.92)<br>
                E_initial: Pre-impact kinetic energy
            </div>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td><code>frictionBoundRate</code></td>
                    <td>0.968</td>
                    <td><strong>0.92</strong></td>
                    <td>Reasonable difference from rolling friction (0.988-0.990). 15% additional energy loss applied at high speeds.</td>
                </tr>
            </table>

            <h4>3.1.3 Magnus Effect (magnusRate)</h4>
            <p>Interaction of spinning ball with air resistance. Based on Bernoulli principle and boundary layer theory:</p>
            <div class="formula">
                <strong>F_Magnus = (1/2) × ρ × A × C_M × v² × ω</strong><br>
                ρ: Air density<br>
                A: Ball cross-sectional area<br>
                C_M: Magnus coefficient (magnusRate = 0.126)<br>
                v: Ball velocity<br>
                ω: Angular velocity
            </div>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Effect</th>
                </tr>
                <tr>
                    <td><code>magnusRate</code></td>
                    <td>0.038</td>
                    <td><strong>0.126</strong></td>
                    <td>Realistic curve for corners, free kicks, and knuckleball shots. Roberto Carlos-style shots possible.</td>
                </tr>
                <tr>
                    <td><code>backSpinLogRate</code></td>
                    <td>7.0</td>
                    <td><strong>6.0</strong></td>
                    <td>More natural forward roll after backspin.</td>
                </tr>
            </table>

            <h3>3.2 Player Stamina (stamina.json)</h3>
            <p>Stamina consumption adjusted according to energy expenditure in real football matches:</p>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Physiological Justification</th>
                </tr>
                <tr>
                    <td><code>defenceTired</code></td>
                    <td>1</td>
                    <td><strong>2</strong></td>
                    <td>Defensive positioning and pressing consume anaerobic energy.</td>
                </tr>
                <tr>
                    <td><code>dribbleTired</code></td>
                    <td>2</td>
                    <td><strong>3</strong></td>
                    <td>Dribbling requires high coordination and speed changes.</td>
                </tr>
                <tr>
                    <td><code>dashTired</code></td>
                    <td>5</td>
                    <td><strong>10</strong></td>
                    <td>Sprinting reaches 120-150% of maximum oxygen consumption.</td>
                </tr>
                <tr>
                    <td><code>contactTired</code></td>
                    <td>5</td>
                    <td><strong>7</strong></td>
                    <td>Physical challenges require muscle strength and balance.</td>
                </tr>
            </table>

            <h3>3.3 Injury System (injury.json)</h3>
            <p>Injury thresholds adjusted according to real football injury statistics. All values range 0-255:</p>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td><code>levelDamageMicro</code></td>
                    <td>120</td>
                    <td><strong>85</strong></td>
                    <td>Micro impacts detected more frequently. Performance impact increases.</td>
                </tr>
                <tr>
                    <td><code>levelDamageMinor</code></td>
                    <td>180</td>
                    <td><strong>150</strong></td>
                    <td>Hard tackles more risky. 1-2 week injury risk.</td>
                </tr>
                <tr>
                    <td><code>symptomDamageTearMuscle</code></td>
                    <td>230</td>
                    <td><strong>210</strong></td>
                    <td>Muscle tear risk during overexertion. Tired players more sensitive.</td>
                </tr>
            </table>

            <h2>4. Artificial Intelligence Parameters</h2>
            <h3>4.1 CPU Difficulty Levels (cpuLevel.json)</h3>
            <p>AI reaction times use frame-based timing system (60 FPS):</p>
            <div class="formula">
                <strong>Reaction Time (ms) = Frame Count × 16.67</strong><br>
                1 Frame = 16.67ms (60 FPS)
            </div>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Level</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Reaction Time</th>
                </tr>
                <tr>
                    <td rowspan="2"><code>dfKickReactionAddWait</code></td>
                    <td>Professional</td>
                    <td>4</td>
                    <td><strong>2</strong></td>
                    <td>~33ms (realistic)</td>
                </tr>
                <tr>
                    <td>TopPlayer</td>
                    <td>3</td>
                    <td><strong>1</strong></td>
                    <td>~17ms (elite level)</td>
                </tr>
                <tr>
                    <td><code>dfSand</code></td>
                    <td>Professional</td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>"Sandwich" marking active</td>
                </tr>
                <tr>
                    <td rowspan="2"><code>gkKickReactionAddWait</code></td>
                    <td>Superstar</td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>Can make human-like errors</td>
                </tr>
                <tr>
                    <td>Legend</td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>Can make human-like errors</td>
                </tr>
                <tr>
                    <td rowspan="2"><code>cpJostleWinRate</code></td>
                    <td>Superstar</td>
                    <td>0</td>
                    <td><strong>10</strong></td>
                    <td>10% physical challenge win rate</td>
                </tr>
                <tr>
                    <td>Legend</td>
                    <td>0</td>
                    <td><strong>20</strong></td>
                    <td>20% physical challenge win rate</td>
                </tr>
            </table>

            <h3>4.2 Goalkeeper AI (defenceGkAuto.xml, defenceGkAutoPk.xml)</h3>
            <p>Goalkeeper behaviors modified according to real goalkeeper reflexes and positioning skills:</p>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Axis</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Effect</th>
                </tr>
                <tr>
                    <td rowspan="2"><code>FuncShape40</code></td>
                    <td>Punch UPSIDE</td>
                    <td>2.0 / 2.5</td>
                    <td><strong>2.2 / 2.75</strong></td>
                    <td>+10% punch range</td>
                </tr>
                <tr>
                    <td>Punch VERTICAL</td>
                    <td>1.0</td>
                    <td><strong>1.1</strong></td>
                    <td>+10% vertical range</td>
                </tr>
                <tr>
                    <td rowspan="3"><code>FuncShape18/19/26</code></td>
                    <td>Block PARALLEL</td>
                    <td>0.4</td>
                    <td><strong>0.5</strong></td>
                    <td>+25% block range</td>
                </tr>
                <tr>
                    <td>Block UPSIDE</td>
                    <td>2.0</td>
                    <td><strong>2.3</strong></td>
                    <td>+15% height</td>
                </tr>
                <tr>
                    <td>Block VERTICAL</td>
                    <td>0.6</td>
                    <td><strong>0.8</strong></td>
                    <td>+33% width</td>
                </tr>
            </table>

            <h3>4.3 Pressing System (press.json)</h3>
            <p>Gegenpressing principle applied:</p>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td><code>frontDist</code></td>
                    <td>1.5</td>
                    <td><strong>1.1</strong></td>
                    <td>Closer pressing distance (-27%)</td>
                </tr>
                <tr>
                    <td><code>delayType</code></td>
                    <td>0</td>
                    <td><strong>1</strong></td>
                    <td>"Stick/Input based" delay - smarter pressing</td>
                </tr>
            </table>

            <h2>5. Tactical Systems</h2>
            <h3>5.1 Team Defense (defence.json, defenceCover.json)</h3>
            <p>Compact defense block and fast support mechanism:</p>
            <table>
                <tr>
                    <th>File</th>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                </tr>
                <tr>
                    <td rowspan="5"><code>defence.json</code></td>
                    <td><code>matchUpStartLine</code></td>
                    <td>10</td>
                    <td><strong>15</strong></td>
                </tr>
                <tr>
                    <td><code>upperConnectionParam</code></td>
                    <td>70.0</td>
                    <td><strong>60.0</strong></td>
                </tr>
                <tr>
                    <td><code>lowerConnectionParam</code></td>
                    <td>50.0</td>
                    <td><strong>40.0</strong></td>
                </tr>
                <tr>
                    <td><code>adjustDribbleWaitTimer</code></td>
                    <td>10.0</td>
                    <td><strong>5.0</strong></td>
                </tr>
                <tr>
                    <td><code>maxWaitTime</code></td>
                    <td>30.0</td>
                    <td><strong>20.0</strong></td>
                </tr>
                <tr>
                    <td rowspan="5"><code>defenceCover.json</code></td>
                    <td><code>coverDist</code></td>
                    <td>5.5</td>
                    <td><strong>4.5</strong></td>
                </tr>
                <tr>
                    <td><code>coverDfDist</code></td>
                    <td>5.0</td>
                    <td><strong>4.5</strong></td>
                </tr>
                <tr>
                    <td><code>coverAngle</code></td>
                    <td>60.0</td>
                    <td><strong>55.0</strong></td>
                </tr>
                <tr>
                    <td><code>coverDfAngle</code></td>
                    <td>65.0</td>
                    <td><strong>55.0</strong></td>
                </tr>
                <tr>
                    <td><code>futureFrame</code></td>
                    <td>10</td>
                    <td><strong>7</strong></td>
                </tr>
            </table>

            <h3>5.2 Offensive Variety</h3>
            <p>Line break and space run parameters modified:</p>
            <table>
                <tr>
                    <th>File</th>
                    <th>Parameter</th>
                    <th>Original</th>
                    <th>Modified</th>
                </tr>
                <tr>
                    <td rowspan="3"><code>lineBreak.json</code></td>
                    <td><code>checkLastLineDist</code></td>
                    <td>7.0</td>
                    <td><strong>6.0</strong></td>
                </tr>
                <tr>
                    <td><code>checkLastLineDist_good</code></td>
                    <td>10.0</td>
                    <td><strong>9.0</strong></td>
                </tr>
                <tr>
                    <td><code>checkBallDist</code></td>
                    <td>30.0</td>
                    <td><strong>35.0</strong></td>
                </tr>
                <tr>
                    <td><code>spaceRun.json</code></td>
                    <td><code>angleDiff_second</code></td>
                    <td>45.0</td>
                    <td><strong>60.0</strong></td>
                </tr>
            </table>

            <h2>6. Other Modifications</h2>
            <h3>6.1 Player Behaviors</h3>
            <p>Various player AI parameters modified:</p>
            <ul>
                <li><strong>avoid.json:</strong> Physical challenges increased, avoidance distances reduced</li>
                <li><strong>ballDodge.json:</strong> Shot blocking behavior improved</li>
                <li><strong>ballplayerDribble.json:</strong> Inertia effect increased</li>
                <li><strong>ballplayerFeint.json:</strong> Unnecessary feints reduced</li>
                <li><strong>ballplayerPass.json:</strong> Long pass accuracy increased</li>
            </ul>

            <h3>6.2 Shot and Pass Systems</h3>
            <ul>
                <li><strong>centering.json:</strong> Parameters increased for curved crosses (Beckham style)</li>
                <li><strong>freekick.json:</strong> Maximum speed 115 km/h for knuckleball shots</li>
                <li><strong>goalKick.json:</strong> Goal kick distance increased to 40m</li>
                <li><strong>longPass.json:</strong> High/low pass difference made more distinct</li>
                <li><strong>penaltykick.json:</strong> Minimum speed 60 km/h for Panenka shots</li>
                <li><strong>shoot.json:</strong> Backspin added to chip shots</li>
                <li><strong>throughpass.json:</strong> Driven through pass speed increased</li>
            </ul>

            <h2>7. Results and Evaluation</h2>
            <h3>7.1 Modification Summary</h3>
            <table>
                <tr>
                    <th>Category</th>
                    <th>File Count</th>
                    <th>Parameter Count</th>
                </tr>
                <tr>
                    <td>Ball Physics</td>
                    <td>1</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td>Player AI</td>
                    <td>8</td>
                    <td>20+</td>
                </tr>
                <tr>
                    <td>Team AI</td>
                    <td>4</td>
                    <td>15+</td>
                </tr>
                <tr>
                    <td>Stamina/Injury</td>
                    <td>2</td>
                    <td>7</td>
                </tr>
                <tr>
                    <td>CPU Difficulty</td>
                    <td>1</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td>Goalkeeper AI</td>
                    <td>2</td>
                    <td>8</td>
                </tr>
                <tr>
                    <td><strong>TOTAL</strong></td>
                    <td><strong>21</strong></td>
                    <td><strong>50+</strong></td>
                </tr>
            </table>

            <h3>7.2 Physical Compliance Assessment</h3>
            <table>
                <tr>
                    <th>Parameter</th>
                    <th>Game Value</th>
                    <th>Real World Range</th>
                    <th>Compliance</th>
                </tr>
                <tr>
                    <td><code>boundRate</code> (COR)</td>
                    <td>0.65</td>
                    <td>0.60-0.75</td>
                    <td>✓ Compliant</td>
                </tr>
                <tr>
                    <td><code>frictionBoundRate</code></td>
                    <td>0.92</td>
                    <td>~0.90-0.95</td>
                    <td>✓ Compliant</td>
                </tr>
                <tr>
                    <td><code>magnusRate</code></td>
                    <td>0.126</td>
                    <td>~0.10-0.15</td>
                    <td>✓ Compliant</td>
                </tr>
            </table>

            <h2>8. Usage and Warnings</h2>
            <div class="warning">
                <strong>Important:</strong> Always backup before making changes. Do not modify BIN files.
            </div>
            <div class="info">
                <strong>Note:</strong> JSON files contain Japanese comments in Shift-JIS encoding. Be careful with encoding when editing.
            </div>

            <h3>8.1 Backup</h3>
            <pre><code>cp -r dt18_win dt18_win_backup</code></pre>

            <h3>8.2 Rollback</h3>
            <pre><code>rm -r dt18_win
cp -r dt18_win_backup dt18_win</code></pre>

            <h2>9. References</h2>
            <ul>
                <li>FIFA Quality Programme - Football Testing Standards</li>
                <li>Sports Science Research - Football Physics and Biomechanics</li>
                <li>Fox Engine 2.0 Documentation (Konami, proprietary)</li>
            </ul>

            <hr>
            <p><em>This documentation describes Fox Engine 2.0 configuration modifications. All rights belong to Konami. For educational and personal use only.</em></p>
        </div>
    </div>

    <script>
        function switchLang(lang) {
            const trContent = document.getElementById('content-tr');
            const enContent = document.getElementById('content-en');
            const btnTr = document.getElementById('btn-tr');
            const btnEn = document.getElementById('btn-en');

            if (lang === 'tr') {
                trContent.style.display = 'block';
                enContent.style.display = 'none';
                btnTr.classList.add('active');
                btnEn.classList.remove('active');
            } else {
                trContent.style.display = 'none';
                enContent.style.display = 'block';
                btnTr.classList.remove('active');
                btnEn.classList.add('active');
            }
        }
    </script>
</body>
</html>
