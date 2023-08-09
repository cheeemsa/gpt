from langchain import PromptTemplate
no_input_prompt=PromptTemplate(input_variables=[],template='Tell me a joke')
no_input_prompt.format()