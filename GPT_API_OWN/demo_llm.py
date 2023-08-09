from typing import Any, List, Mapping, Optional
import openai
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

class ChatGPTLLM(LLM):

    @property
    def _llm_type(self) -> str:
        return "chat_gpt"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        model: Optional[str] = "gpt-3.5-turbo"

    ) -> str:
        # 定义一个空列表来存储对话消息
        messages = []

        # 将用户消息添加到消息列表中
        messages.append({"role": "user", "content": prompt})

        # 使用OpenAI API进行对话生成
        completion = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )

        # 从API响应中提取助手的回复
        chat_response = completion.choices[0].message["content"]
        # 将助手的回复添加到消息列表中，准备下一轮对话
        messages.append({"role": "assistant", "content": chat_response})

        return chat_response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {}

api_key = "sk-2EfkISU4b1fx8AFYgxW9XSR7b4NpjaJA7eAidM2RgiQ6aQsz"
api_base = "https://api.chatanywhere.cn/v1"

llm = ChatGPTLLM(api_key=api_key, api_base=api_base)

