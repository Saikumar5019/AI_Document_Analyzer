import streamlit as st

from parser import extract_text
from ocr import extract_text_from_image
from preprocessing import clean_text
from ai_engine import classify_document, summarize_document


st.set_page_config(
    page_title="AI Document Analyzer",
    layout="wide"
)

st.title("AI Document Analyzer")

st.write("Upload PDF, DOCX, TXT, PNG, JPG documents")


uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"]
)


if uploaded_file:

    st.success(f"Uploaded File: {uploaded_file.name}")

    file_name = uploaded_file.name.lower()

    with st.spinner("Processing document..."):

        # OCR pipeline
        if file_name.endswith((".png", ".jpg", ".jpeg")):

            raw_text = extract_text_from_image(uploaded_file)
            extracted_text = clean_text(raw_text)

        # Parser pipeline
        else:

            raw_text = extract_text(uploaded_file)
            extracted_text = clean_text(raw_text)

        # AI classification
        document_type = classify_document(extracted_text)

        # AI summarization
        summary = summarize_document(extracted_text)

    # Results
    st.subheader("Document Type")
    st.success(document_type)

    st.subheader("Document Summary")
    st.write(summary)

    st.subheader("Extracted Text")
    st.text_area(
        "Document Content",
        extracted_text,
        height=400
    )

    word_count = len(extracted_text.split())

    st.info(f"Total Words Extracted: {word_count}")