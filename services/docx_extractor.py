import docx
import io
from typing import List

from services.image_ocr import extract_text_from_image


def extract_text_from_docx(file: bytes) -> List[str]:
    """Extract text from DOCX file including embedded images."""
    doc = docx.Document(io.BytesIO(file))
    fullText = []

    # Get text from paragraphs
    for para in doc.paragraphs:
        if para.text.strip():  # Only add non-empty text
            fullText.append(para.text)

    # Process embedded images
    try:
        for image in doc.part.related_parts.values():
            if hasattr(image, 'content_type') and image.content_type.startswith("image/"):
                ocr_text = extract_text_from_image(image.blob)
                if ocr_text.strip():
                    fullText.append(ocr_text)
    except Exception as e:
        print(f"Error processing images in DOCX: {e}")
            
    return fullText
