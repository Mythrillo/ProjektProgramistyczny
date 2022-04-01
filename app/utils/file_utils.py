import cv2
import numpy as np


def convert_image_file_contents_to_cv2_image(contents: bytes) -> np.ndarray:
    numpy_array = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    return img
