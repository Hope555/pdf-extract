import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np


def preprocess_image(image):
    """
    Improve image quality before OCR
    """

    # Convert PIL image to OpenCV format
    img = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise removal
    denoised = cv2.fastNlMeansDenoising(gray)

    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2
    )

    return thresh


def extract_text_ocr(pdf_path, dpi=300):
    """
    Extract text from scanned PDF using OCR
    """

    images = convert_from_path(pdf_path, dpi=dpi)

    full_text = []

    for img in images:

        processed_img = preprocess_image(img)

        text = pytesseract.image_to_string(processed_img)

        full_text.append(text)

    return "\n".join(full_text)