from PyPDF2 import PdfReader
from groq import Groq
from docx import Document


def get_pdf_text(pdfs):
    text = ""
    for pdf in pdfs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text() + "/n"
    return text

def get_docx_text(docx_files):
    for docx_file in docx_files:
        document = Document(docx_file)
        text = ""
        for para in document.paragraphs:
            text += para.text + "\n"
    return text


def query_response(text):
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role" : "system",
                "content" : """You are a resume extractor API that responds in JSON. The provided text is a resume and the JSON schema should include 
                            {
                                "Name" :  The name of the applicant ,
                                "email" : The email of the applicant,
                                "phone_number" : The phone number of the applicant,
                                "skills" : the skills of the applicant in the form of a list containing strings,
                                "education" : education of the applicant
                                "experience" : experience of the applicant
                            } In case no relevant data is found for a key, keep it null."""
            },
            {
                "role" : "user",
                "content" : text
            }
        ],
        model = "llama3-70b-8192"
    )

    return chat_completion.choices[0].message.content
