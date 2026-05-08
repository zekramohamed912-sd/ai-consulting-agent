from pdf_extractor import extract_text_from_pdf
from agents import run_all_agents

pdf_path = "DTC Fashion Retail.pdf"

proposal_text = extract_text_from_pdf(pdf_path)

print("Extracted text preview:")

results = run_all_agents(proposal_text)

for agent_name, output in results.items():
    print("\n" + "=" * 60)
    print(agent_name.upper())
    print("=" * 60)
    print(output)