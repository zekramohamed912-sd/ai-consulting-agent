import requests

MODEL_NAME = "phi3"


def call_llm(system_prompt, user_input):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 120
        }
    }

    response = requests.post(url, json=payload, timeout=600)
    response.raise_for_status()

    return response.json()["message"]["content"]


def summary_agent(proposal_text):
    system_prompt = """
    You are a summary agent.
    Summarize the project proposal clearly and briefly.
    Include:
    - Main idea
    - Business need
    - Target users
    - Expected outcome
    """
    return call_llm(system_prompt, proposal_text)


def objectives_agent(proposal_text):
    system_prompt = """
    You are an objectives extraction agent.
    Extract the key objectives from the proposal.

    Include:
    - Business objectives
    - Technical objectives
    - Target users
    - Constraints
    - Expected outputs

    Return the answer in clear bullet points.
    """
    return call_llm(system_prompt, proposal_text)


def roadmap_agent(proposal_text):
    system_prompt = """
    You are a technical roadmap agent.
    Create a realistic implementation roadmap for this AI project.

    Include:
    - Development phases
    - Main tasks in each phase
    - Estimated time for each phase
    - Dependencies between phases

    Make the roadmap realistic for a student AI project.
    """
    return call_llm(system_prompt, proposal_text)


def model_selection_agent(proposal_text):
    system_prompt = """
    You are a model selection agent.
    Recommend suitable AI/ML models or LLM approaches.

    Include:
    - Recommended model type
    - Why it fits the project
    - Whether prompt engineering, RAG, fine-tuning, or traditional ML is suitable
    - Limitations
    """
    return call_llm(system_prompt, proposal_text)


def deployment_agent(proposal_text):
    system_prompt = """
    You are a deployment strategy agent.
    Suggest a realistic deployment strategy for this AI system.

    Include:
    - Backend
    - API layer
    - Database or storage
    - Monitoring
    - Security
    - Scaling considerations
    """
    return call_llm(system_prompt, proposal_text)


def risks_agent(proposal_text):
    system_prompt = """
    You are a risk analysis agent.
    Identify possible risks in this AI project.

    Include:
    - Technical risks
    - Data risks
    - Ethical risks
    - Deployment risks
    - Business risks

    For each risk, suggest a mitigation strategy.
    """
    return call_llm(system_prompt, proposal_text)


def run_all_agents(proposal_text):
    results = {
        "summary": summary_agent(proposal_text),
        "objectives": objectives_agent(proposal_text),
        "technical_roadmap": roadmap_agent(proposal_text),
        "model_selection": model_selection_agent(proposal_text),
        "deployment_strategy": deployment_agent(proposal_text),
        "risks": risks_agent(proposal_text),
    }

    return results