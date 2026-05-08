from pathlib import Path
from data_extraction import extract_text, extract_tables, clean_text


def process_document(pdf_path):
    pdf_file = Path(pdf_path)

    raw_text = extract_text(pdf_path)
    cleaned_lines = clean_text(raw_text)
    tables = extract_tables(pdf_path)

    document_data = {
        "file_name": pdf_file.name,
        "file_path": str(pdf_file),
        "raw_text": raw_text,
        "cleaned_text": cleaned_lines,
        "tables": tables if tables else [],
        "table_count": len(tables) if tables else 0
    }

    return document_data