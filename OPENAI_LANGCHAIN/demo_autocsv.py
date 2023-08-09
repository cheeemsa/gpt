import os
import openai
import pandas as pd
from langchain import OpenAI
from langchain.llms import openai
from langchain.agents import create_pandas_dataframe_agent
os.environ["OPENAI_API_KEY"] = "sk-kcfJcDXKztSEuMxaSqVjvuniMFIlz8HSr2xApuxivkNINiEc" #这个key为测试key，不可商用
os.environ["OPENAI_API_BASE"] = "https://key.langchain.com.cn/v1"
os.environ["OPENAI_API_PREFIX"] = "https://key.langchain.com.cn"
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0)
df = pd.read_csv('file:path')
agent = create_pandas_dataframe_agent(llm, df, verbose=True)
while True:
    user_input = input("User: ")
    if user_input.lower() in ['exit', 'quit', 'stop']:
        break
    assistant_response = agent.run(user_input)
    print("Assistant:", assistant_response)