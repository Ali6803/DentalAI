import cv2
import numpy as np

class DentalDetector:
    """
    Dental AI - Panoramik Röntgen Anomali Dedektörü
    Genesis Team | TEKNOFEST 2025
    """

    ANOMALY_COLORS = {
        'caries':     (0, 0, 255),   # Kırmızı - Çürük
        'bone_loss':  (0, 255, 255), # Sarı    - Kemik kaybı
        'root_canal': (255, 0, 0),   # Mavi    - Kanal ihtiyacı
    }

    def __init__(self, model_path=None):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        print("[Dental AI] Model yükleniyor...")
        return None

    def preprocess(self, image_path: str) -> np.ndarray:
        """Görüntüyü modele hazırla"""
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(f"Görüntü bulunamadı: {image_path}")

        # Kontrast iyileştirme
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        img = clahe.apply(img)

        # Gürültü giderme
        img = cv2.GaussianBlur(img, (3, 3), 0)

        return img

    def analyze(self, image_path: str) -> dict:
        """Ana analiz fonksiyonu"""
        processed = self.preprocess(image_path)

        result = {
            'image_path': image_path,
            'processed_image': processed,
            'detections': [],
            'risk_score': 0.0,
            'report_text': 'Analiz tamamlandı.'
        }
        return result

    def annotate(self, image: np.ndarray, detections: list) -> np.ndarray:
        """Anomalileri görüntüye işaretle"""
        annotated = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        for det in detections:
            x, y, w, h = det['bbox']
            label = det['type']
            conf = det['confidence']
            color = self.ANOMALY_COLORS.get(label, (255, 255, 255))

            cv2.rectangle(annotated, (x, y), (x+w, y+h), color, 2)
            cv2.putText(
                annotated,
                f"{label} ({conf:.0%})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 1
            )

        return annotated
