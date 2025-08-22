from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()

from langgraph_agent.graph import create_workflow
from langgraph_agent.tools import get_weather, get_stock_price, human_assistance
from langgraph_agent.parse import input_parser

workflow = create_workflow(
	llm=init_chat_model("openai:gpt-5-nano"),
	tools=[get_weather, get_stock_price, human_assistance],
	input_parser=input_parser
)
agent = workflow.compile()

with open("graph.png", "wb") as f:
    f.write(agent.get_graph().draw_mermaid_png())

## Run `langgraph dev` to start the server