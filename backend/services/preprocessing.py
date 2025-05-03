import cv2
import numpy as np
from PIL import Image


def preprocess_image(image, crop_box=None) -> np.ndarray:
      if crop_box:
        image = image.crop(crop_box)
    
      # Convertir a escala de grises
      image = image.convert('L')
    
      # Binarizar (umbral adaptativo podría ser mejor en escaneos irregulares)
      image = image.point(lambda x: 0 if x < 180 else 255, '1')
    
      return image