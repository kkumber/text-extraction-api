# text-extraction-api

This is a lightweight microservice for extracting text from files using specific python libraries served via FastAPI.

## Features

- Extract text from PDF, DOCX, PPTX, IMAGE FORMAT
- REST API for integration
- Lightweight and fast

## Installation

Clone the repository:

```bash
git clone https://github.com/kkumber/text-extraction-api.git
cd text-extraction-microservice
```

Make sure you already have Python 3.8+ installed in your system. If you don't have python installed you can check the official page for instructions.

<a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>

Create a virtual environment:

```bash
python -m venv .venv
```

<i>Note: If python doesn’t work, try 'py' (Windows) or 'python3' (Linux/macOS).</i>

Activate virtual environment:
On Windows:

```bash
.venv/Scripts/activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

<i>Note: It's recommended to use a virtual environment to install all dependencies to avoid conflicts with your other projects</i>

Install all dependencies:

```bash
pip install -r requirements.txt
```

## Usage

You can simply serve locally via uvicorn

```bash
uvicorn main:app --reload --port=9000
```

API will be available at:
Swagger UI → http://localhost:9000/docs

### Example Request

```bash
curl -X POST "http://localhost:9000/extract" \
  -F "file=@sample.pdf"
```

## License

This project is licensed under the MIT License – see the LICENSE file for details.

## Acknowledgements

This project is made possible thanks to the following open-source libraries and tools:

- [PyMuPDF](https://pymupdf.readthedocs.io/) – PDF text and image extraction
- [python-docx](https://python-docx.readthedocs.io/) – Reading text from Microsoft Word documents
- [python-pptx](https://python-pptx.readthedocs.io/) – PowerPoint text extraction
- [Pillow](https://pillow.readthedocs.io/) – Image processing support
- [pytesseract](https://pypi.org/project/pytesseract/) – OCR (Optical Character Recognition) for extracting text from images
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – The OCR engine powering `pytesseract`

Special thanks to the open-source community for maintaining these tools and enabling fast, reliable text extraction services.
