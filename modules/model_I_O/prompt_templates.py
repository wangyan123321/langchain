from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate
)

#提示语模型

template = """\
You are a naming consultant for new companies.
What is a good name for a company that makes {product}?
"""
promt = PromptTemplate.from_template(template)
data = promt.format(product="fast food")
print(data)

# 消息模型
template = "You can help me that translate {intput_language} to {output_language}"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
data = system_message_prompt.format(intput_language="English",output_language="Chinese")
print(data)

#
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
data = human_message_prompt.format(text="hello")
print(data)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
data = chat_prompt.format_prompt(intput_language="English", output_language="Chinese", text="hello")
print(data)


