import asyncio
from dotenv import load_dotenv
from src.models.context import Thread, Event
from src.utils.agent import agent_loop

load_dotenv()


async def main():
    thread = Thread([
        Event(type="user_input", data="Please add 5 and 3")
    ])
    result_thread = await agent_loop(thread)
    print(result_thread.serialize())

if __name__ == "__main__":
    asyncio.run(main())