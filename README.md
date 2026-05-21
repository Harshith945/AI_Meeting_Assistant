https://aimeetingassistant-jeaardvus64blz8mfsfkpc.streamlit.ap

# 📋 AI Meeting Assistant

An AI-powered multimodal meeting intelligence system built using **LangChain**, **Groq LLMs**, **Langfuse**, and **Streamlit** that automatically converts meeting conversations into structured insights including summaries, action items, decisions, and discussion topics.

---

# 🚀 Project Overview

This project helps users analyze meeting transcripts from multiple input formats such as:

- Typed meeting notes
- Uploaded text/docx files
- Voice recordings

The application uses Large Language Models (LLMs) with prompt engineering and structured JSON parsing to generate meaningful meeting insights in real time.

---

# ✨ Features

- 🧠 AI-generated meeting summaries
- 📌 Action item extraction
- 🎯 Decision tracking
- 📂 Topic identification
- ⚡ Priority classification (High / Medium / Low)
- 📄 TXT & DOCX file support
- 🎤 Voice-to-text transcription
- 🔍 Langfuse tracing and observability
- ⚙️ LangChain LCEL pipeline
- 🌐 Interactive Streamlit interface

---

# 🧠 Technologies Used

| Technology | Usage |
|---|---|
| Python | Backend logic |
| Streamlit | Web UI |
| LangChain | LLM orchestration |
| Groq | LLM inference |
| Langfuse | Prompt tracing & monitoring |
| JsonOutputParser | Structured JSON extraction |
| SpeechRecognition | Audio transcription |
| python-docx | DOCX parsing |

---

# 🏗️ System Architecture

```text
User Input
   ↓
Streamlit Interface
   ↓
PromptTemplate
   ↓
LangChain Pipeline
   ↓
Groq LLM
   ↓
JsonOutputParser
   ↓
Structured Meeting Insights
   ↓
Langfuse Monitoring Dashboard

```
---

# 🔍 Langfuse Integration

This project integrates **Langfuse** for LLM observability and monitoring.

Langfuse helps track and debug the complete AI pipeline including:

- Prompt tracing
- LLM response monitoring
- Execution latency tracking
- Structured output inspection
- LangChain pipeline observability
- AI debugging and evaluation

---

## 🚀 Why Langfuse?

In production-grade GenAI applications, monitoring prompts and model outputs is essential.

Langfuse provides visibility into:

```text
User Input
   ↓
Prompt
   ↓
LLM Response
   ↓
Parsed JSON Output
