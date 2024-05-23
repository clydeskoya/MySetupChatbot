import fitz 

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    # Remove empty lines
    text_lines = filter(lambda x: x.strip(), text.split('\n'))
    # Join non-empty lines back together
    processed_text = '\n'.join(text_lines)
    return processed_text
