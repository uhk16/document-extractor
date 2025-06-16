FROM python:3.11-slim

# Install system dependencies including Tesseract with ALL language packs
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-all \
    libtesseract-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python packages with DOCX support
RUN pip install Flask Werkzeug pytesseract Pillow pdf2image PyPDF2 python-docx

# Copy the app
COPY app.py .

# Create upload directory
RUN mkdir -p uploads

# Verify Tesseract installation and available languages
RUN tesseract --list-langs

EXPOSE 8000

CMD ["python", "app.py"]