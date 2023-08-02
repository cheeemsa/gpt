
import openai
# 设置您的OpenAI API密钥
openai.api_key = "sk-2EfkISU4b1fx8AFYgxW9XSR7b4NpjaJA7eAidM2RgiQ6aQsz"
openai.api_base = "https://api.chatanywhere.cn/v1"

# 定义一个空列表来存储对话消息
messages = []

while True:
    # 用户输入消息
    content = input("User: ")
    # 将用户消息添加到消息列表中
    messages.append({"role": "user", "content": content})

    # 使用OpenAI API进行对话生成
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # 从API响应中提取助手的回复
    chat_response = completion.choices[0].message["content"]
    # 将助手的回复打印出来
    print(f'ChatGPT: {chat_response}')

    # 将助手的回复添加到消息列表中，准备下一轮对话
    messages.append({"role": "assistant", "content": chat_response})