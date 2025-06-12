import pytesseract as ocr
import PIL.Image
import io


def extract_text_from_image(img_bytes: bytes) -> str:
    """Extract text from image using OCR."""
    ocrConfig = r'--psm 6 --oem 3'
    image = PIL.Image.open(io.BytesIO(img_bytes))
    try:
        output = ocr.image_to_string(image, config=ocrConfig)
        return output
    finally:
        image.close()
