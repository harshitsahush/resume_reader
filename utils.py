from PyPDF2 import PdfReader

def get_pdf_text(pdfs):
    text = ""
    for pdf in pdfs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text() + "/n"
    return text