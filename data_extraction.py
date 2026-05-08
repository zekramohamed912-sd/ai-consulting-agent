from pypdf import PdfReader
import pdfplumber

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()
        if page_text:
            text += f"\n--- Page {page_number} ---\n"
            text += page_text

    return text

    import pdfplumber

def extract_tables(pdf_path):
    tables_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table in tables:
                tables_data.append({
                    "page": page_number,
                    "table": table
                })

def clean_text(text):
    lines = text.split("\n")
    cleaned = []

    for line in lines:
        line = line.strip()

        # remove page markers
        if line.startswith("--- Page"):
            continue

        if line:
            cleaned.append(line)

    return cleaned


def structure_text(cleaned_lines):
    structured = {
        "title": "",
        "sections": []
    }

    current_section = None

    for line in cleaned_lines:
        # Ignore page markers like --- Page 1 ---
        if line.startswith("--- Page") and line.endswith("---"):
            continue

        # Set title from the first real line
        if not structured["title"] and len(line) > 5:
            structured["title"] = line
            continue

        # Detect headings
        if line.isupper() or line.lower().startswith(("introduction", "conclusion", "overview")):
            current_section = {
                "heading": line,
                "content": []
            }
            structured["sections"].append(current_section)
        else:
            if current_section:
                current_section["content"].append(line)

    return structured