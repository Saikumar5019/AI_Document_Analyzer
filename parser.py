import pdfplumber
from docx import Document


def extract_pdf_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_docx_text(file):

    doc = Document(file)

    text = "\n".join([para.text for para in doc.paragraphs])

    return text


def extract_txt_text(file):

    return file.read().decode("utf-8")


def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf_text(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_docx_text(uploaded_file)

    elif file_name.endswith(".txt"):
        return extract_txt_text(uploaded_file)

    else:
        return "Unsupported File Type"