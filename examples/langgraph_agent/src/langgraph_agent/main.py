import asyncio
from time import time
from dotenv import load_dotenv
from nanoid import generate
from langchain.chat_models import init_chat_model
from langgraph.types import Command
load_dotenv()


from graph import create_workflow
from tools import get_weather, get_stock_price, human_assistance
from memory import redis_memory
from parse import input_parser

async def main(
    query: str,
    human_response=None, 
    thread_id: str = f"thread_{generate()}",
    stream=True,
):
    workflow = create_workflow(
        llm=init_chat_model("openai:gpt-4.1-nano"),
        tools=[get_weather, get_stock_price, human_assistance],
        input_parser=input_parser
    )
    async with redis_memory() as checkpointer:
        await checkpointer.asetup()
        agent = workflow.compile(checkpointer=checkpointer)
        if stream:
            payload = {"messages": [('user', query)]}
            if human_response:
                payload = Command(resume={"data": human_response})
            async for chunk in agent.astream(
                payload, 
                config={"configurable": {"thread_id": thread_id}},
                stream_mode='values'
            ):
                if "messages" in chunk:
                    chunk["messages"][-1].pretty_print()
        else:
            result = await agent.ainvoke({"messages": [('user', query)]})
            print(result)


if __name__ == "__main__":
    human_response = (
        "We, the experts are here to help! We'd recommend you check out LangGraph to build your agent."
        " It's much more reliable and extensible than simple autonomous agents."
    )
    start_time = time()
    # thread_id = "thread_RovbKioJ-7PfKQkoCLYGd"
    # print(f"thread_id: {thread_id}")
    asyncio.run(main(
        # thread_id=thread_id,
        query="TSLA stock price?",
        # human_response=human_response
    ))
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
    
    # start_time = time()
    # asyncio.run(main(human_response=human_response, thread_id="2"))
    # end_time = time()
    # print(f"Time taken: {end_time - start_time} seconds (cached)")