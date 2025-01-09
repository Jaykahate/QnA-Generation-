import streamlit as st
import PyPDF2
import re
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(
    api_key="use your API key"  # Replace with your actual API key
)

# Streamlit page configuration
st.set_page_config(page_title="Quiz Generator", layout="centered")

# App title
st.title("Quiz Generator from PDF Notes using Groq API")

# File Upload Section
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"], help="Upload a PDF to extract text and generate a quiz.")

# Text Input Section (for manual input instead of uploading PDFs)
text_input = st.text_area("Or manually input text to generate quiz", height=200)

# Function to extract text from the uploaded PDF
def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# Function to preprocess the extracted text
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = re.sub(r'[^\w\s.,!?]', '', text)  # Remove special characters except punctuation
    text = re.sub(r'Page\s\d+|page\s\d+', '', text, flags=re.IGNORECASE)  # Remove "Page X"
    text = re.sub(r'(©|Copyright).*', '', text)  # Remove copyright symbols
    text = re.sub(r'\b(http[s]?://\S+|www\.\S+)\b', '', text)  # Remove URLs
    text = text.lower()  # Convert to lowercase for consistency
    return text

# Function to call Groq API to generate a quiz
def call_groq_api(prompt, model="llama3-70b-8192"):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling Groq API: {e}")
        return None

# Function to create a QnA generation prompt
def generate_quiz_prompt(text):
    prompt = f"""
    From the following text, generate a set of open-ended questions and their corresponding answers.
    The questions should cover the following categories:
    - Analytical: Questions that require analysis and interpretation of the content.
    - Factual: Questions that are directly answered by the content.
    - Understanding: Questions that test comprehension of the text.
    - Theoretical: Questions that delve into underlying principles or theories.

    Text: {text}

    Format your response as:
    1. Question (Category: <Category>):
       <Generated Question>
       Answer:
       <Generated Answer>
    """
    return prompt

# Main logic for handling both PDF upload and manual text input
def generate_quiz_from_text(text):
    # Preprocess the input text
    preprocessed_text = preprocess_text(text)
    st.subheader("Preprocessed Text")
    st.text_area("Cleaned Text", preprocessed_text, height=200)

    # Generate Quiz Button
    if st.button("Generate Quiz"):
        st.info("Generating quiz using Groq API...")

        # Generate quiz using Groq API
        prompt = generate_quiz_prompt(preprocessed_text)
        quiz_text = call_groq_api(prompt)

        if quiz_text:
            st.subheader("Generated Quiz")
            st.text_area("Quiz Output", quiz_text, height=400)
        else:
            st.error("Failed to generate the quiz. Please try again.")

# Logic for handling user input
if uploaded_file is not None:
    # Extract text from the uploaded PDF
    st.subheader("Uploaded PDF Content")
    pdf_text = extract_text_from_pdf(uploaded_file)

    if pdf_text:
        st.text_area("Extracted Text", pdf_text, height=200)
        generate_quiz_from_text(pdf_text)
    else:
        st.warning("No text extracted from the uploaded PDF. Please check the file.")
elif text_input:
    # If the user provides manual input, generate quiz from that text
    generate_quiz_from_text(text_input)
else:
    st.info("Please upload a PDF or manually input text to begin.")

# Footer
st.markdown("---")
st.markdown("Powered by **Streamlit** and Groq API integration.")

