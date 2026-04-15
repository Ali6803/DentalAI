import cv2
import numpy as np

class Preprocessor:
    """Röntgen görüntüsü ön işleme modülü"""

    def __init__(self, target_size=(512, 512)):
        self.target_size = target_size

    def resize(self, image: np.ndarray) -> np.ndarray:
        return cv2.resize(image, self.target_size)

    def enhance_contrast(self, image: np.ndarray) -> np.ndarray:
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        return clahe.apply(image)

    def denoise(self, image: np.ndarray) -> np.ndarray:
        return cv2.fastNlMeansDenoising(image, h=10)

    def normalize(self, image: np.ndarray) -> np.ndarray:
        return image.astype(np.float32) / 255.0

    def pipeline(self, image_path: str) -> np.ndarray:
        """Tüm adımları sırayla uygula"""
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = self.resize(img)
        img = self.enhance_contrast(img)
        img = self.denoise(img)
        img = self.normalize(img)
        return img
