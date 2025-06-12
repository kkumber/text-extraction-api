from fastapi import FastAPI, File, UploadFile, HTTPException
import magic
import pymupdf
import docx
import pytesseract as ocr
import PIL
import io
import pptx

app = FastAPI()


@app.post("/upload-document/")
async def upload_document(file: list[UploadFile] = File(...)):
    extractedText = []
    
    allowed_docs = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain',
        'image/jpeg',
        'image/png'
    ]
    
    for uploadedFile in file:
        content = await uploadedFile.read()
        mime_type = magic.from_buffer(content, mime=True)

        if mime_type not in allowed_docs:
            raise HTTPException(
                status_code=400,
                detail=f"Document type not allowed. Received: {mime_type}"
            )
            
        if (mime_type == allowed_docs[0]):
            extractedText.append(extract_text_from_pdf(content))

    return {
        "extracted_text": '.'.join(extractedText)
    }

# Extract text in docx file using pymupdf
def extract_text_from_pdf(file):
    doc = pymupdf.open(stream=file, filetype='pdf')
    fullText = []

    for page in doc:
        # Process all images on the page at once
        image_list = page.get_images()
        for img in image_list:
            xref = img[0]
            img_data = doc.extract_image(xref)
            img_bytes = img_data["image"]
            fullText.append(extract_text_from_image(img_bytes))
        fullText.append(page.get_text())
    return '\n'.join(fullText)

# Extract text in docx file using python-docx
def extract_text_from_docx(file):
    doc = docx.Document(io.BytesIO(file))
    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)
        
    for image in doc.part.related_parts.values():
        if image.content_type.startswith("image/"):
            fullText.append(extract_text_from_image(image.blob))
            
    return '\n'.join(fullText)

# Extract text in docx file using pytesseract
def extract_text_from_image(img_bytes):
    # config for ocr engine and psm
    ocrConfig = r'--psm 6 --oem 3'
    image = PIL.Image.open(io.BytesIO(img_bytes))
    output = ocr.image_to_string(image, config=ocrConfig)
    return output

# Extract text in docx file using python-pptx
def extract_text_from_pptx(file):
    ppt = pptx.Presentation(io.BytesIO(file))
    fullText = []
    
    for slide in ppt.slides:
        for shape in slide.shapes:
            if hasattr(shape, 'text'):
                fullText.append(shape.text)
            elif shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE:
                # Get the image binary data
                image = shape.image
                image_bytes = image.blob  # the raw image data
                fullText.append(extract_text_from_image(image_bytes))
            elif shape.has_table:
                for row in shape.table.rows:
                    for cell in row.cells:
                        fullText.append(cell.text)
    
    return '\n'.join(fullText)

# Extract text in docx file using idk yet
def extract_text_from_video(file):
    
    pass