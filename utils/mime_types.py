from services.pdf_extractor import extract_text_from_pdf
from services.docx_extractor import extract_text_from_docx
from services.pptx_extractor import extract_text_from_pptx
from services.image_ocr import extract_text_from_image

allowed_docs = {
    'application/pdf': extract_text_from_pdf,
    'application/msword': extract_text_from_docx,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': extract_text_from_docx,
    'image/jpeg': extract_text_from_image,
    'image/png': extract_text_from_image,
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': extract_text_from_pptx
}