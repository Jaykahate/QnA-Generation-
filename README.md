# Q&A Generator Application

## Description
This application allows users to generate question-and-answer (Q&A) pairs from either uploaded PDF files or manually entered text. It uses a Streamlit-based interface combined with the Groq API to process the text and generate meaningful Q&A pairs across various categories such as analytical, factual, understanding, and theoretical.

---

## Features
- **Upload PDF Files**: Extract text from uploaded PDF documents for Q&A generation.
- **Manual Text Input**: Input text directly if no PDF is available.
- **Text Preprocessing**: Automatically cleans and formats the text for optimal results.
- **Q&A Categories**:
  - Analytical: Questions requiring deeper interpretation.
  - Factual: Questions based on explicit facts in the text.
  - Understanding: Questions testing comprehension.
  - Theoretical: Questions exploring underlying principles or theories.
- **Error Handling**: Provides clear error messages for invalid files or API failures.

---

## Installation
1. Create a Groq Account:
   Visit the Groq website.
   Sign up for an account if you haven't already.
2. Obtain the API Key:
   Once logged into your Groq account, navigate to your dashboard.
   Look for the API or Access Tokens section.
   Generate a new API key from this section.

1. Clone the repository:
   ```bash
   https://github.com/Jaykahate/QnA-Generation-.git
   cd qna-generator
   ```

2. Create and activate a virtual environment:
   - On Windows:
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser and choose an input method:
   - Upload a PDF file to extract text.
   - Enter text manually in the provided text area.
3. Click the "Generate Quiz" button to process the input and view the Q&A pairs.

---

## Requirements

- Python 3.8 or higher
- Internet connection (required for Groq API calls)

### Dependencies
- `groq==0.13.1`
- `PyPDF2==3.0.1`
- `streamlit==1.41.1`
- `requests==2.28.1`
- `re` (Built-in Python module for regex)

---

## Example Workflow

1. **Uploading a PDF**:
   - Extract text automatically from the PDF.
   - Preprocess the text to remove noise and optimize for Q&A generation.
   - Use the Groq API to generate questions and answers in a variety of categories.

2. **Manual Text Input**:
   - Input raw text into the text area.
   - Process the text and generate Q&A pairs in a structured format.

---

## Error Handling

- **Invalid PDF Files**: If the uploaded file cannot be read, a relevant error message is displayed.
- **API Errors**: If the Groq API fails, the application provides an informative error message.

---

## Developer Notes

- Replace the placeholder API key in `app.py` with a valid Groq API key.
- Ensure that uploaded PDF files are not encrypted or corrupted.

---

## Acknowledgments

- **Streamlit**: For the user-friendly interface.
- **Groq API**: For enabling Q&A generation from text using LLMs.

---

## License

This project is licensed under the MIT License.

