import sys
import os

# Ensure the parent directory of 'scripts' is in the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Print sys.path to debug
print("Python Path:", sys.path)

from app.services.text_extraction import extract_text_from_pdf

manual_dir = "data/manuals"
processed_dir = "data/processed"

if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

for manual in os.listdir(manual_dir):
    if manual.endswith(".pdf"):
        pdf_path = os.path.join(manual_dir, manual)
        text = extract_text_from_pdf(pdf_path)
        text_filename = manual.replace(".pdf", ".txt")
        text_path = os.path.join(processed_dir, text_filename)
        with open(text_path, "w") as f:
            f.write(text)