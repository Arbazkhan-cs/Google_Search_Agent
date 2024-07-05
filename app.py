import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool
from googlesearch import search
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import os

# Step 1: Define the Google Search Tool
@tool
def google_search(query: str, num_results: int = 5):
    """Perform a Google search and retrieve the URLs of the search results."""
    search_results = []
    for url in search(query, num_results=num_results):
        search_results.append(url)
    return search_results

# Function to fetch and summarize content from a URL
def fetch_and_summarize_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.text for p in soup.find_all('p')])
        text = text[:10000]
        return text
    except requests.RequestException as e:
        return None

# Step 2: Initialize the LLM from Groq
load_dotenv()
llm = ChatGroq(model="llama3-8b-8192", temperature=0.7)

# Step 3: Define the Prompt Template
template = [
    ("system", "You are an intelligent assistant. Answer the user question by performing a Google search and summarizing the content of the top results."),
    ("user", "{input}"),
    ("ai", "")
]

prompt = ChatPromptTemplate.from_messages(template)

# Step 4: Create the LLM Chain
llm_chain = prompt | llm

# Step 5: Create a Custom Chain to First Perform the Google Search and Then Run the LLM
class GoogleSearchAndAnswerChain:
    def __init__(self, search_tool, llm):
        self.search_tool = search_tool
        self.llm = llm

    def run(self, input):
        search_results = self.search_tool(input)
        texts = []
        for url in tqdm(search_results):
            if fetch_and_summarize_url(url) is not None:
                texts.append(fetch_and_summarize_url(url))
        texts = " ".join(texts)
        summary_prompt = f"Summarize the following content: {texts}"
        summary = self.llm.invoke({"input", summary_prompt})
        
        return summary.content

# Instantiate the custom chain
google_search_and_answer_chain = GoogleSearchAndAnswerChain(google_search, llm_chain)

# Step 6: Define a Function to Use the Custom Chain
def answer_question(question: str):
    return google_search_and_answer_chain.run(question)

# Step 7: Create the Streamlit App
st.title("Intelligent Assistant")

question = st.text_input("Enter your query:")
if st.button("Get Answer"):
    answer = answer_question(question)
    st.write("Answer:", answer)

