from langchain_core.prompts import PromptTemplate
from parser import parser

prompt = PromptTemplate(
    template="""
You are an AI meeting assistant.

Extract action items from the meeting transcript.

Return ONLY valid JSON.

DO NOT:
- add markdown
- add explanations
- add text before JSON
- add text after JSON

Expected JSON format:

{{
  "actions": [
    {{
      "task": "string",
      "owner": "string or not_available",
      "deadline": "string or not_available",
      "priority": "High | Medium | Low"
    }}
  ]
}}

Priority Rules:
- High → urgent / blocker / near deadline
- Medium → regular task
- Low → optional / minor task

If owner missing:
owner = "not_available"

If deadline missing:
deadline = "not_available"

{format_instructions}

Transcript:
{transcript}
""",

    input_variables=["transcript"],

    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)
