from document_processor import process_document
import json

pdf_path = "sample_pdfs/proposal.pdf"

document_data = process_document(pdf_path)

with open("outputs/document_data.json", "w", encoding="utf-8") as f:
    json.dump(document_data, f, indent=2, ensure_ascii=False)

print("✅ Done! document_data.json saved")