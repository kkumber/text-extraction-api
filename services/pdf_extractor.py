import pymupdf
from typing import List
from services.image_ocr import extract_text_from_image


def extract_text_from_pdf(file: bytes) -> List[str]:
    """Extract text from PDF file including embedded images."""
    doc = pymupdf.open(stream=file, filetype='pdf')
    try:
        fullText = []
        for page in doc:
            # Get text from page
            page_text = page.get_text()
            if page_text.strip():  # Only add non-empty text
                fullText.append(page_text)

            # Process images on the page
            image_list = page.get_images()
            for img in image_list:
                try:
                    xref = img[0]
                    img_data = doc.extract_image(xref)
                    img_bytes = img_data["image"]
                    ocr_text = extract_text_from_image(img_bytes)
                    if ocr_text.strip():  # Only add non-empty OCR text
                        fullText.append(ocr_text)
                except Exception as e:
                    # Log error but continue processing
                    print(f"Error processing image in PDF: {e}")
                    continue
        
        return fullText
    finally:
        doc.close()
