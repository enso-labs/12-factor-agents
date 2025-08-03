from graph import create_workflow
from langchain_core.messages import HumanMessage, BaseMessage
from tools import get_weather, get_stock_price
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

def input_parser(messages: list[BaseMessage]):
    xml_content = "<thread>\n"
    for i, message in enumerate(messages):
        xml_content += f'  <event id="{message.id}" role="{message.type}">{message.content}</event>\n'
    xml_content += "</thread>"
    return xml_content

def main():
    query = "What is the weather in Tokyo?"
    workflow = create_workflow(
        llm=init_chat_model("openai:gpt-4.1-nano"),
        tools=[get_weather, get_stock_price],
        input_parser=input_parser
    )
    agent = workflow.compile()
    for chunk in agent.stream({"messages": [HumanMessage(content=query)]}):
        print(chunk)


if __name__ == "__main__":
    main()
