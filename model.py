import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langfuse.langchain import CallbackHandler

from prompt import prompt
from parser import parser

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- GROQ API KEY ----------------
groq_api_key = os.getenv("GROQ_API_KEY")

# ---------------- LLM ----------------
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

# ---------------- LANGFUSE CALLBACK ----------------
langfuse_handler = CallbackHandler()

# ---------------- CHAIN ----------------
chain = prompt | llm | parser

# ---------------- MAIN FUNCTION ----------------
def generate_meeting_insights(transcript: str):

    # ---------------- INVOKE CHAIN ----------------
    result = chain.invoke(
        {
            "transcript": transcript
        },

        config={
            "callbacks": [langfuse_handler]
        }
    )

    return result