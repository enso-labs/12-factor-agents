import os
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.redis.aio import AsyncRedisSaver
from langchain_redis.cache import RedisSemanticCache
from langchain_openai import OpenAIEmbeddings

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

#####################################
# Redis Memory
#####################################
def redis_memory():
    return AsyncRedisSaver.from_conn_string(REDIS_URL)


def in_memory_memory():
    return InMemorySaver()

#####################################
# Redis Cache
#####################################
def redis_cache(
    name="langgraph_agent",
    prefix: str | None = None,
    ttl=30,
    embeddings=OpenAIEmbeddings()
):
    return RedisSemanticCache(
        name=name,
        prefix=prefix,
        redis_url=REDIS_URL, 
        embeddings=embeddings,
        ttl=ttl,
    )