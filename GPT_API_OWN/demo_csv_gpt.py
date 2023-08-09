from langchain.agents import create_csv_agent
from typing import Any, List, Mapping, Optional
import openai
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
openai.api_key = "sk-2EfkISU4b1fx8AFYgxW9XSR7b4NpjaJA7eAidM2RgiQ6aQsz"
openai.api_base = "https://api.chatanywhere.cn/v1"

class ChatGPTLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "chat_gpt"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        model: Optional[str] = "gpt-3.5-turbo",
        temperature: Optional[float] = 0.0
    ) -> str:
        # 定义一个空列表来存储对话消息
        messages = messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

        # 将用户消息添加到消息列表中
        messages.append({"role": "user", "content": prompt})

        # 使用OpenAI API进行对话生成
        completion = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature  # Set the temperature parameter
        )

        # 从API响应中提取助手的回复
        chat_response = completion.choices[0].message["content"]
        # 将助手的回复添加到消息列表中，准备下一轮对话
        messages.append({"role": "assistant", "content": chat_response})

        return chat_response

# Load CSV data using CSVLoader
csv_loader = CSVLoader('D:/Rfile/test.csv')
df = pd.read_csv('D:/Rfile/test.csv')
# Create an instance of the ChatGPTLLM class
chat_gpt_llm = ChatGPTLLM()

# Create the agent with the loaded CSV data and the ChatGPTLLM instance
agent = create_pandas_dataframe_agent(ChatGPTLLM(verbose=True), df, verbose=True)

# Run the agent with a prompt
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'stop']:
        break

    # Generate assistant's response
    assistant_response = agent.run(user_input)

    # Print the assistant's response
    print("Assistant:", assistant_response)




