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