#响应代理，对输入进行分析，根据设置的语言模型进行处理，选择默认的工具进行执行

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

# 设置语言模型
llm = OpenAI(temperature=0)

# 构建工具模型
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 设置代理
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 执行代理处理
output = agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

# 打印结果
print("output:"+output)

# I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.
# Action: Search
# Action Input: "Leo DiCaprio girlfriend"
# Observation: Leonardo DiCaprio brings rumored model girlfriend Neelam Gill on dinner date with his mom.
# Thought: I need to find out Neelam Gill's age.
# Action: Search
# Action Input: "Neelam Gill age"
# Observation: 28 years
# Thought: I now need to calculate 28 raised to the 0.43 power.
# Action: Calculator
# Action Input: 28^0.43
# Observation: Answer: 4.1906168361987195
# Thought: I now know the final answer.
# Final Answer: Neelam Gill, Leo DiCaprio's girlfriend, is 28 years old and her age raised to the 0.43 power is 4.1906168361987195.
