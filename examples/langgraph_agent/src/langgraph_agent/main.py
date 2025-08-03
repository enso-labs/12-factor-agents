import os
import asyncio
from dotenv import load_dotenv
from graph import create_workflow
from langchain_core.messages import HumanMessage
from tools import get_weather, get_stock_price, human_assistance
from langchain.chat_models import init_chat_model
from langchain.globals import set_llm_cache
from langchain_openai import OpenAIEmbeddings
from langchain_redis.cache import RedisSemanticCache
from langgraph.checkpoint.redis.aio import AsyncRedisSaver
from parse import input_parser
from time import time

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

load_dotenv()
set_llm_cache(
    RedisSemanticCache(
        redis_url=REDIS_URL, 
        embeddings=OpenAIEmbeddings(),
        ttl=30
    )
)

async def main(stream=True):
    query = "I need some expert guidance for building an AI agent. Could you request assistance for me?"
    workflow = create_workflow(
        llm=init_chat_model("openai:gpt-4.1-nano"),
        tools=[get_weather, get_stock_price, human_assistance],
        input_parser=input_parser
    )
    async with AsyncRedisSaver.from_conn_string(REDIS_URL) as checkpointer:
        agent = workflow.compile(checkpointer=checkpointer)
        if stream:
            async for chunk in agent.astream(
                {"messages": [HumanMessage(content=query)]}, 
                config={"configurable": {"thread_id": "1"}},
                stream_mode='values'
            ):
                if "messages" in chunk:
                    chunk["messages"][-1].pretty_print()
        else:
            result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
            print(result)


if __name__ == "__main__":
    start_time = time()
    asyncio.run(main())
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time()
    asyncio.run(main())
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds (cached)")
