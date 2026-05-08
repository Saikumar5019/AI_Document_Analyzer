import easyocr
from PIL import Image
import numpy as np

# Load OCR model once
reader = easyocr.Reader(['en'])


def extract_text_from_image(uploaded_file):

    # Open image
    image = Image.open(uploaded_file)

    # Convert to numpy array
    image_np = np.array(image)

    # OCR extraction
    results = reader.readtext(image_np)

    # Extract only text
    extracted_text = ""

    for result in results:
        extracted_text += result[1] + " "

    return extracted_text