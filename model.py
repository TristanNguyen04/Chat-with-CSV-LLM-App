import streamlit as st
from langchain.document_loaders.csv_loader import CSVLoader
import tempfile
from utils import get_model_response
import pandas as pd

def main():
    st.title("Chat with CSV using Gemini Pro")

    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type = "csv")

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete = False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

            csv_loader = CSVLoader(file_path = tmp_file_path, encoding="utf-8", csv_args={
    'delimiter': ','
})

            data = csv_loader.load()
            user_input = st.text_input("Your message:")
            print(user_input)

            if user_input:
                response = get_model_response(data, user_input)
                st.write(response)

if __name__ == "__main__":
    main()