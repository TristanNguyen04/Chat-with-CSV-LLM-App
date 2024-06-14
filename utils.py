from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

genai.configure(api_key="ENTER_YOUR_API_KEY") #Create and Insert your own API Key via https://aistudio.google.com/app/apikey
os.environ["GOOGLE_API_KEY"] = "ENTER_YOUR_API_KEY" #Insert the above API key

def get_model_response(file, query):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=200)
    context = "\n\n".join(str(p.page_content) for p in file)

    data = text_splitter.split_text(context)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    searcher = Chroma.from_texts(data, embeddings).as_retriever()
    q = "Which is the highest value?"
    records = searcher.get_relevant_documents(q)
    print(records)

    prompt_template = """
        You have to answer the question from the provided context and make sure that you provide all the details\n
        Context: {context}
        Question: {question}
        
        Answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    response = chain({
        "input_documents": records,
        "question": query
    }, return_only_outputs=True)

    return response['output_text']
