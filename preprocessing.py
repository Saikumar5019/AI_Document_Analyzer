import re


def clean_text(text):

    # Remove extra spaces
    text = re.sub(r'\\s+', ' ', text)

    # Remove unwanted symbols
    text = re.sub(r'[^a-zA-Z0-9.,:/\\-₹$% ]', '', text)

    # Remove multiple dots
    text = re.sub(r'\\.+', '.', text)

    # Strip spaces
    text = text.strip()

    return text