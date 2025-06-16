from services.pdf_extractor import extract_text_from_pdf
from services.docx_extractor import extract_text_from_docx
from services.pptx_extractor import extract_text_from_pptx
from services.image_ocr import extract_text_from_image

allowed_docs = {
    'application/pdf': extract_text_from_pdf,
    # 'application/msword': extract_text_from_docx,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': extract_text_from_docx, 
    # 'application/vnd.ms-powerpoint': extract_text_from_pptx,
    'application/vnd.openxmlformats-officedocument.presentationml.presentation': extract_text_from_pptx,  
    'image/jpeg': extract_text_from_image,
    'image/png': extract_text_from_image,
    'image/webp': extract_text_from_image,
    'image/bmp': extract_text_from_image,
}