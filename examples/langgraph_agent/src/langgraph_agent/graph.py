from typing import Annotated, Callable

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import BaseTool
from langchain_core.language_models.chat_models import BaseChatModel

class State(TypedDict):
	messages: Annotated[list, add_messages]

def create_workflow(
    llm: BaseChatModel,
    tools: list[BaseTool],
    input_parser: Callable
) -> StateGraph:
	workflow = StateGraph(State)
	llm_with_tools = llm.bind_tools(tools)

	def chatbot(state: State):
		prompt = input_parser(state["messages"])
		return {"messages": [llm_with_tools.invoke(prompt)]}

	workflow.add_node("chatbot", chatbot)

	tool_node = ToolNode(tools=tools)
	workflow.add_node("tools", tool_node)

	workflow.add_conditional_edges(
		"chatbot",
		tools_condition,	
	)
	# Any time a tool is called, we return to the chatbot to decide the next step
	workflow.add_edge("tools", "chatbot")
	workflow.add_edge(START, "chatbot")
	return workflow
