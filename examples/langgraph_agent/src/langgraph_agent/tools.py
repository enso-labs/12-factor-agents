import random

from langchain_core.tools import tool


@tool(description="Get the weather in a given city")
def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny and 80 degrees"

@tool(description="Get the stock price of a given symbol")
def get_stock_price(symbol: str) -> str:
    return f"The stock price of {symbol} is {random.randint(100, 1000)}"