from langchain import LLMMathChain,  SerpAPIWrapper
from langchain.agents import initialize_agent,Tool
from langchain.agents import AgentType
from typing import Any, List, Mapping, Optional
import openai
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.utilities import PythonREPL
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
        temperature: Optional[float] = 0  # Add temperature with a default value of 0.0
    ) -> str:
        # 定义一个空列表来存储对话消息
        messages = []

        # 将用户消息添加到消息列表中
        messages.append({"role": "user", "content": prompt})

        # 使用OpenAI API进行对话生成
        completion = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0 # Set the temperature parameter
        )

        # 从API响应中提取助手的回复
        chat_response = completion.choices[0].message["content"]
        # 将助手的回复添加到消息列表中，准备下一轮对话
        messages.append({"role": "assistant", "content": chat_response})

        return chat_response
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {}
search = SerpAPIWrapper(serpapi_api_key = "b2bc793ca31e17a04c0116250af75dfff70f50dc0d38dae967586a23d80a5259")
llm = ChatGPTLLM()
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

api_key = "sk-2EfkISU4b1fx8AFYgxW9XSR7b4NpjaJA7eAidM2RgiQ6aQsz"
api_base = "https://api.chatanywhere.cn/v1"
serpapi_api_key = "b2bc793ca31e17a04c0116250af75dfff70f50dc0d38dae967586a23d80a5259"
llm = ChatGPTLLM(api_key=api_key, api_base=api_base)
tools  = [
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    ),

    # You can create the tool to pass to an agent
     Tool(
    name="python_repl",
    description="A Python shell. Use this to calculate. ",
    func=PythonREPL.run
)



]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
user_input = "今天几号?"
result = agent.run(user_input)

# 打印助手的最终回复
print(result)
