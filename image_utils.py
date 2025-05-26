import cv2
import numpy as np
from PIL import Image

def preprocess_image(image: Image.Image):
    img = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return edges, img

def estimate_usable_area(edge_image):
    # Dummy logic: assume 60% area is usable if edges are detected
    edge_density = np.sum(edge_image > 0) / edge_image.size
    usable_ratio = min(max(edge_density * 2, 0.1), 0.8)
    return usable_ratio
