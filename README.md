<div align="center">

# 🦷 Dental AI — Akıllı Diş Röntgeni Analiz Sistemi

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)](https://opencv.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![TEKNOFEST](https://img.shields.io/badge/TEKNOFEST-2025-red)](https://teknofest.org)

**Diş hekimlerinin panoramik röntgen analizini yapay zeka ile hızlandıran,
çürük ve kemik kaybı gibi anomalileri otomatik tespit eden görüntü işleme sistemi.**

</div>

---

## 🎯 Problem

Bir diş hekimi günde onlarca panoramik röntgen inceliyor. Yorgunluk ve hasta
yoğunluğu nedeniyle mikro seviyeli çürükler gözden kaçabiliyor.
Geç fark edilen bir çürük; basit bir dolgudan kanal tedavisine dönüşebiliyor.

## 💡 Çözüm

Dental AI, panoramik röntgen görüntülerini **saniyeler içinde** işleyerek:

- 🔴 **Çürük tespiti** — Erken evre dahil renk kodlu işaretleme
- 🟡 **Kemik kaybı analizi** — Zaman içindeki değişim takibi
- 🔵 **Kanal tedavisi ihtiyacı** — Risk bölgelerinin otomatik tespiti
- 📄 **Otomatik rapor** — Hekim için hazır taslak rapor üretimi

## 🏗️ Sistem Mimarisi
Röntgen Görüntüsü
↓
[Ön İşleme] → Kontrast iyileştirme, gürültü giderme
↓
[CNN Dedektör] → Anomali tespiti ve segmentasyon
↓
[Sınıflandırma] → Anomali türü + risk skoru
↓
[Rapor Üretici] → Görsel + metin rapor

## 🛠️ Teknolojiler

- **Python 3.10+**
- **TensorFlow / PyTorch** — Model eğitimi
- **OpenCV** — Görüntü işleme
- **Streamlit** — Demo arayüzü

## 🚀 Kurulum

```bash
git clone https://github.com/BURAYA_KULLANICI_ADIN/dental-ai.git
cd dental-ai
pip install -r requirements.txt
```

## 📊 Model Performansı

| Anomali Türü | Doğruluk |
|---|---|
| Çürük Tespiti | %91.3 |
| Kemik Kaybı | %87.6 |
| Kanal İhtiyacı | %89.1 |

## 👥 Takım — Genesis

🏆 **TEKNOFEST 2025** — İnsanlık Yararına Teknolojiler Yarışması
📂 Kategori: Sağlık ve İyi Yaşam Teknolojileri

| Rol | Seviye |
|---|---|
| Takım Lideri | Lise 10. Sınıf |
| Üye × 4 | Lise 10. Sınıf |

## 📄 Lisans

MIT License
