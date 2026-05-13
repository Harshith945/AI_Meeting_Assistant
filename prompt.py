from langchain_core.prompts import PromptTemplate
from parser import parser

prompt = PromptTemplate(
    template="""
You are an expert AI meeting assistant.

Analyze the meeting transcript and extract structured information.

Return ONLY valid JSON.

JSON Schema:
{{
    "summary": "5-7 line concise summary",
    
    "action_items": [
        {{
            "task": "task description",
            "owner": "person responsible or null",
            "deadline": "deadline or null",
            "priority": "high | medium | low"
        }}
    ],

    "decisions": [
        "decision 1",
        "decision 2"
    ],

    "topics": [
        "topic 1",
        "topic 2"
    ]
}}

Rules:
- Do not return markdown
- Do not add explanations
- Do not invent information
- Infer priority:
    high = urgent/blocker/near deadline
    medium = normal task
    low = optional/minor task
- Output MUST be valid JSON

{format_instructions}

Transcript:
{transcript}
""",

    input_variables=["transcript"],

    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)