# Chat with CSV using Gemini Pro

This repository contains a Streamlit application that allows users to chat with a CSV file using the Gemini Pro model.

## Requirements

- Python 3.8 or higher
- Streamlit
- Langchain
- Chroma
- Google Generative AI
- Pandas

## Setup

### 1. Clone the repository

```sh
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the dependencies
```sh
pip install -r requirements.txt
```

### 4. Set up your API key
- 1. Create and insert your own API key via Google AI Studio (https://aistudio.google.com/app/apikey).
- 2. Replace the placeholder `ENTER_YOUR_API_KEY` in `utils.py` with your own API key.
```sh
# In utils.py
genai.configure(api_key="YOUR_API_KEY")
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
```

### 5. Running the Application
Run on your folder with repository directory (on Terminal or Bash) by using the following command:
```sh
streamlit run model.py
```

#### Usage
- Upload a CSV file using the sidebar file uploader.
- Enter your message or query in the text input field.
- The application will process the CSV file and provide a response based on the Gemini Pro model.



