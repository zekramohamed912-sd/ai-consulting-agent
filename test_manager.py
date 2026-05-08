from manager import Manager

proposal_text = """
This proposal aims to improve airline crew scheduling using AI.
The system assigns pilots and crew while respecting constraints like
duty hours, rest periods, and real-time disruptions.
"""

manager = Manager()
tasks = manager.create_tasks(proposal_text)

for task in tasks:
    print("Task:", task["task_name"])
    print("Agent:", task["agent"])
    print("Instruction:", task["instruction"])
    print("-" * 40)
    