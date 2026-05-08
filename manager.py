class Manager:
    def create_tasks(self, proposal_text: str):
        tasks = [
            {
                "task_name": "proposal_understanding",
                "agent": "proposal_understanding_agent",
                "instruction": "Analyze the business objective, use case, constraints, and main problem.",
                "input": proposal_text
            },
            {
                "task_name": "architecture_design",
                "agent": "architecture_agent",
                "instruction": "Design the overall system architecture, components, and data flow.",
                "input": proposal_text
            },
            {
                "task_name": "model_selection",
                "agent": "model_selection_agent",
                "instruction": "Recommend suitable AI/ML models based on the problem, data, and constraints.",
                "input": proposal_text
            },
            {
                "task_name": "data_requirements",
                "agent": "data_agent",
                "instruction": "Identify required data sources, preprocessing steps, and data challenges.",
                "input": proposal_text
            },
            {
                "task_name": "deployment_strategy",
                "agent": "deployment_agent",
                "instruction": "Suggest deployment options, infrastructure, integration, and monitoring.",
                "input": proposal_text
            },
            {
                "task_name": "implementation_roadmap",
                "agent": "roadmap_agent",
                "instruction": "Break the project into implementation phases and development steps.",
                "input": proposal_text
            },
            {
                "task_name": "timeline_estimation",
                "agent": "timeline_agent",
                "instruction": "Estimate project duration, milestones, and deliverables.",
                "input": proposal_text
            },
            {
                "task_name": "risk_analysis",
                "agent": "risk_agent",
                "instruction": "Identify risks, limitations, assumptions, and possible mitigation strategies.",
                "input": proposal_text
            }
        ]

        return tasks