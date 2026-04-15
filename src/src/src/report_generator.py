from datetime import datetime

class ReportGenerator:
    """Otomatik diş analiz raporu üretici"""

    ANOMALY_LABELS = {
        'caries':     'Çürük',
        'bone_loss':  'Kemik Kaybı',
        'root_canal': 'Kanal Tedavisi İhtiyacı',
    }

    def generate(self, detections: list, image_path: str) -> str:
        now = datetime.now().strftime("%d.%m.%Y %H:%M")

        lines = [
            "=" * 50,
            "       DENTAL AI — ANALİZ RAPORU",
            "=" * 50,
            f"Tarih       : {now}",
            f"Görüntü     : {image_path}",
            f"Tespit Sayısı: {len(detections)}",
            "-" * 50,
        ]

        if not detections:
            lines.append("✅ Anormal bölge tespit edilmedi.")
        else:
            for i, det in enumerate(detections, 1):
                label = self.ANOMALY_LABELS.get(det['type'], det['type'])
                conf = det['confidence']
                lines.append(f"{i}. {label} — Güven: {conf:.0%}")

        lines += [
            "-" * 50,
            "⚠️  Bu rapor yapay zeka destekli ön analizdir.",
            "    Kesin tanı için uzman hekim değerlendirmesi gereklidir.",
            "=" * 50,
        ]

        return "\n".join(lines)

    def save(self, report_text: str, output_path: str = "rapor.txt"):
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_text)
        print(f"Rapor kaydedildi: {output_path}")
