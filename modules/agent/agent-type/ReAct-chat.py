from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

# 设置语言模型
chat_model = ChatOpenAI(temperature=0)

# 构建工具模型
tools = load_tools(["serpapi", "llm-math"], llm=chat_model)

# 设置代理
agent = initialize_agent(tools, chat_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 执行代理处理
output = agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")

# 打印结果
print("output:"+output)

# I need to find out Leo DiCaprio's girlfriend's name and her age.
# Action: Search
# Action Input: "Leo DiCaprio girlfriend"
# Observation: Leonardo DiCaprio brings rumored model girlfriend Neelam Gill on dinner date with his mom.
# Thought:I need to find out Neelam Gill's age.
# Action: Search
# Action Input: "Neelam Gill age"
# Observation: 28 years
# Thought:I need to calculate her age raised to the 0.43 power.
# Action: Calculator
# Action Input: 28^(0.43)