import asyncio
import json
from graph import create_workflow
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage, ToolMessage
from tools import get_weather, get_stock_price
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

def input_parser(messages: list[BaseMessage], llm_response_prefix: str = "\n\n ai_response:"):
    xml_content = "<thread>\n"
    for i, message in enumerate(messages):
        if isinstance(message, AIMessage):
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    xml_content += f'  <event id="{tool_call["id"]}" role="tool_input" tool_name="{tool_call["name"]}">{json.dumps(tool_call["args"])}</event>\n'
            else:
                xml_content += f'  <event id="{message.id}" role="{message.type}">{message.content}</event>\n'
        if isinstance(message, ToolMessage):
            xml_content += f'  <event id="{message.tool_call_id}" role="tool_output" tool_name="{message.name}" status="{message.status}">{message.content}</event>\n'
        else:
            xml_content += f'  <event id="{message.id}" role="{message.type}">{message.content}</event>\n'
    xml_content += "</thread>"
    return xml_content + llm_response_prefix

async def main():
    query = "What is the weather in Tokyo?"
    workflow = create_workflow(
        llm=init_chat_model("openai:gpt-4.1-nano"),
        tools=[get_weather, get_stock_price],
        input_parser=input_parser
    )
    agent = workflow.compile()
    async for chunk in agent.astream({"messages": [HumanMessage(content=query)]}):
        print(chunk)


if __name__ == "__main__":
    asyncio.run(main())
