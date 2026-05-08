import ollama


def classify_document(text):
    """
    Classify document type
    """

    prompt = f"""
You are an AI document classifier.

Analyze the document and classify it into EXACTLY ONE category.

Categories:
- Invoice
- Resume
- Bank Statement
- Legal Document
- Medical Report
- Other

Rules:
- Return ONLY category name
- No explanation
- No extra text

Document:
{text[:3000]}
"""

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"].strip()

    except Exception as e:
        return f"Classification Error: {str(e)}"


def summarize_document(text):
    """
    Summarize document content
    """

    prompt = f"""
You are an AI document summarizer.

Summarize this document in 4–6 clear bullet points.

Rules:
- concise summary
- meaningful points
- no unnecessary text

Document:
{text[:4000]}
"""

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"].strip()

    except Exception as e:
        return f"Summarization Error: {str(e)}"



        
#-----------------------------------------------------
#              WITH USING GEMINAI API KEY 
#-----------------------------------------------------

# import os
# from dotenv import load_dotenv
# from google import genai

# # Load environment variables
# load_dotenv()

# # Create Gemini client
# client = genai.Client(
#     api_key=os.getenv("GOOGLE_API_KEY")
# )


# def classify_document(text):
#     """
#     Classify uploaded document into a document category
#     """

#     prompt = f"""
#     You are an AI document classifier.

#     Analyze the given document text carefully.

#     Classify the document into EXACTLY one of these categories:

#     - Invoice
#     - Resume
#     - Bank Statement
#     - Legal Document
#     - Medical Report
#     - Other

#     Rules:
#     - Return ONLY the category name
#     - Do not explain anything
#     - No extra text
#     - No bullet points

#     Document Text:
#     {text[:4000]}
#     """

#     try:
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=prompt
#         )

#         return response.text.strip()

#     except Exception as e:
#         return f"Classification Error: {str(e)}"

    