import streamlit as st
import speech_recognition as sr

from docx import Document

from model import generate_meeting_insights

# ---------------- FILE HELPERS ----------------
def read_txt(file):
    return file.read().decode("utf-8")


def read_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])


# ---------------- AUDIO HELPER ----------------
def audio_to_text(file):

    recognizer = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)

    return recognizer.recognize_google(audio)


# ---------------- STREAMLIT CONFIG ----------------
st.set_page_config(
    page_title="AI Meeting Assistant",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("📋 AI Meeting Assistant")

st.write(
    "Upload or enter meeting transcripts to extract summaries, "
    "action items, decisions, and topics."
)

# ---------------- INPUT OPTIONS ----------------
option = st.radio(
    "Choose Input Type",
    ["Text", "File Upload", "Voice Input"]
)

transcript = ""

# ---------------- TEXT INPUT ----------------
if option == "Text":

    transcript = st.text_area(
    "Paste Meeting Transcript",
    height=250
)

# ---------------- FILE INPUT ----------------
elif option == "File Upload":

    uploaded_file = st.file_uploader(
        "Upload .txt or .docx file",
        type=["txt", "docx"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".txt"):
            transcript = read_txt(uploaded_file)

        elif uploaded_file.name.endswith(".docx"):
            transcript = read_docx(uploaded_file)

        st.success("File uploaded successfully!")

# ---------------- VOICE INPUT ----------------
elif option == "Voice Input":

    audio_file = st.file_uploader(
        "Upload .wav file",
        type=["wav"]
    )

    if audio_file:

        try:
            transcript = audio_to_text(audio_file)

            st.success("Audio converted to text successfully!")

        except Exception as e:
            st.error(f"Speech recognition failed: {e}")

# ---------------- DISPLAY TRANSCRIPT ----------------
if transcript:

    st.subheader("📄 Transcript")

    st.write(transcript)

    # ---------------- GENERATE BUTTON ----------------
    if st.button("Generate Insights"):

        with st.spinner("Analyzing meeting transcript..."):

            try:

                result = generate_meeting_insights(transcript)

                st.subheader("📤 JSON Output")

                st.json(result)

                # ✅ Clear input box
                st.session_state.transcript_input = ""

            except Exception as e:

                st.error("Failed to process transcript")
                st.exception(e)

                
