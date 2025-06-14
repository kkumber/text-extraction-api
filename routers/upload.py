from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List, Dict, Any
import os

import magic


from services.pdf_extractor import extract_text_from_pdf
from services.docx_extractor import extract_text_from_docx
from services.pptx_extractor import extract_text_from_pptx
from services.image_ocr import extract_text_from_image
from utils.mime_types import allowed_docs

router = APIRouter()


@router.post("/upload-document/")
async def upload_document(file: List[UploadFile] = File(...)) -> Dict[str, Any]:
    # Input validation
    if not file:
        raise HTTPException(400, "No files provided")
    
    if len(file) > 10:
        raise HTTPException(400, "Too many files")

    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    
    # Result dictionary
    result = {
        'results': [],
        'total_files': len(file),
        'successful_files': 0,
        'failed_files': 0
    }
    
    current_file = result['results']
    for uploadedFile in file:
        # Check file size before reading
        if uploadedFile.size and uploadedFile.size > MAX_FILE_SIZE:
            current_file.append({
                'filename': uploadedFile.filename,
                'status': 'error',
                'error': f'File too large: {uploadedFile.size:,} bytes (max: {MAX_FILE_SIZE:,})'
            })
            result['failed_files'] += 1 # Add as a failure
            continue

        try:
            content = await uploadedFile.read()
            mime_type = magic.from_buffer(content, mime=True)
            
            # Check if file type is allowed
            if mime_type not in allowed_docs:
                current_file.append({
                    'filename': uploadedFile.filename,
                    'mime_type': mime_type,
                    'status': 'error',
                    'error': f'Document type not allowed: {mime_type}'
                })
                result['failed_files'] += 1 # Add as a failure
                continue
            
            # Process the file
            extractedText = allowed_docs[mime_type](content)
            current_file.append({
                'filename': uploadedFile.filename,
                'mime_type': mime_type,
                'status': 'success',
                'extractedText': extractedText
            })
            result['successful_files'] += 1 # Add as success

        except Exception as e:
            current_file.append({
                'filename': uploadedFile.filename,
                'mime_type': mime_type or 'unknown',
                'status': 'error',
                'error': str(e)
            })
        result['failed_files'] += 1 # Add as a failure
    return result
