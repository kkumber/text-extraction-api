from fastapi import FastAPI, File, UploadFile, HTTPException
import magic
import pymupdf
import docx
import pytesseract as ocr
import PIL

app = FastAPI()


@app.post("/upload-document/")
async def upload_document(file: list[UploadFile] = File(...)):
    extractedText = []
    
    allowed_docs = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain',
        'image/*'
    ]
    
    for uploadedFile in file:
        content = await file.read()
        mime_type = magic.from_buffer(content, mime=True)

        if mime_type not in allowed_docs:
            raise HTTPException(
                status_code=400,
                detail=f"Document type not allowed. Received: {mime_type}"
            )

    
    return {
        "filename": file.filename,
        "document_type": mime_type
    }

def extract_text_from_pdf(file):
    doc = pymupdf.read(file)
    fullText = []

    for page in doc:
        text = page.get_text().encode('utf8')
        text.append(text)
    print('\n'.join(fullText))

def extract_text_from_docx(file):
    doc = docx.Document(file)
    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)
    print('\n'.join(fullText))

def extract_text_from_image(file):
    # Custom config for OCR page segmentation modes and engine mode
    ocrConfig = r'--psm 6 --oem 3'

    output = ocr.image_to_string(PIL.Image.open(file), config=ocrConfig)
    return output

def extract_text_from_video(file):
    #extraction logic

def extract_text_from_pptx(file):
    #extraction logic