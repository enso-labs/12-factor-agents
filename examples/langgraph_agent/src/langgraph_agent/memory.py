import os
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.redis.aio import AsyncRedisSaver

from langchain_openai import OpenAIEmbeddings

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

#####################################
# Redis Memory
#####################################
def redis_memory(ttl=3600):
    return AsyncRedisSaver.from_conn_string(REDIS_URL, ttl={"default": ttl})


def in_memory_memory():
    return InMemorySaver()

########################################################
# Redis Cache (Semantic Cache) .. not used for now
########################################################
def redis_cache(
    name="langgraph_agent",
    prefix: str | None = None,
    ttl=30,
    embeddings=OpenAIEmbeddings()
):
    from langchain_redis.cache import RedisSemanticCache
    return RedisSemanticCache(
        name=f"{name}:{prefix}" if prefix else name,
        redis_url=REDIS_URL, 
        embeddings=embeddings,
        ttl=ttl,
        distance_threshold=0.95 # 1 location for weather can return diff query location result
    )