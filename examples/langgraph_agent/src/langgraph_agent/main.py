import asyncio
from dotenv import load_dotenv
from graph import create_workflow
from langchain_core.messages import HumanMessage
from tools import get_weather, get_stock_price, human_assistance
from langchain.chat_models import init_chat_model
from langchain.globals import set_llm_cache
from langchain_openai import OpenAIEmbeddings
from langchain_redis.cache import RedisSemanticCache
from parse import input_parser
from time import time

load_dotenv()
set_llm_cache(
    RedisSemanticCache(
        redis_url="redis://localhost:6379", 
        embeddings=OpenAIEmbeddings(),
        ttl=30
    )
)

def main(stream=True):
    # query = "TSLA stock price?"
    query = "I need some expert guidance for building an AI agent. Could you request assistance for me?"
    workflow = create_workflow(
        llm=init_chat_model("openai:gpt-4.1-nano"),
        tools=[get_weather, get_stock_price, human_assistance],
        input_parser=input_parser
    )
    agent = workflow.compile()
    for event in agent.stream({"messages": [HumanMessage(content=query)]}, stream_mode='values'):
        if "messages" in event:
            event["messages"][-1].pretty_print()
    # if stream:
    #     async for chunk in agent.astream({"messages": [HumanMessage(content=query)]}):
    #         print(chunk)
    # else:
    #     result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
    #     print(result)


if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time()
    main()
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds (cached)")
