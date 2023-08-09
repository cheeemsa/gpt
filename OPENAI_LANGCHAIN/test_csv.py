import os

from langchain.chains import ConversationalRetrievalChain
from langchain import OpenAI
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

#在此更改环境变量，这三者均需要更改
#对于ts/js的语言的更改机制类似，请小伙伴自行尝试
os.environ["OPENAI_API_KEY"] = "sk-kcfJcDXKztSEuMxaSqVjvuniMFIlz8HSr2xApuxivkNINiEc" #当前key为内测key，内测结束后会失效，在群里会针对性的发放新key
os.environ["OPENAI_API_BASE"] = "https://key.langchain.com.cn/v1"
os.environ["OPENAI_API_PREFIX"] = "https://key.langchain.com.cn"
##注意上面的环境变量初始化要早于openai的引入👇🏻👇🏻👇🏻👇🏻👇🏻
from langchain.llms import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

from langchain.agents import create_csv_agent
from typing import Any, List, Mapping, Optional
import openai
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd


# Load CSV data using CSVLoader
csv_loader = CSVLoader('D:/Rfile/test.csv')
df = pd.read_csv('D:/Rfile/test.csv')
# Create an instance of the ChatGPTLLM class


# Create the agent with the loaded CSV data and the ChatGPTLLM instance
agent = create_pandas_dataframe_agent(llm, df, verbose=True)

# Run the agent with a prompt
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'stop']:
        break

    # Generate assistant's response
    assistant_response = agent.run(user_input)

    # Print the assistant's response
    print("Assistant:", assistant_response)