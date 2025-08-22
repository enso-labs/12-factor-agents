import random

from langchain_core.tools import tool
from langgraph.types import interrupt

@tool(description="Get the weather in a given city")
def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny and 80 degrees"

@tool(description="Get the stock price of a given symbol")
def get_stock_price(symbol: str) -> str:
    return f"The stock price of {symbol} is {random.randint(100, 1000)}"

@tool(description="Request assistance from a human")
def human_assistance(query: str) -> str:
    human_response = interrupt({"query": query})
    return human_response["data"]