import httpx
from src.config import config

class LLMService:
    """
    Service for interacting with the OpenAI Chat Completion API.
    """

    def __init__(self):
        self.api_key = config.LLM_API_KEY
        self.model = config.LLM_MODEL
        self.base_url = config.LLM_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def chat(
        self, 
        context: str, 
        system_prompt: str = "You are a helpful assistant.", 
        timeout: float = 30.0
    ):
        """
        Sends a chat completion request to the OpenAI API.

        Args:
            messages (list): List of message dicts, e.g. [{"role": "user", "content": "Say hello"}]
            timeout (float): Request timeout in seconds.

        Returns:
            dict: The response JSON from the API.
        """
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": context}
            ]
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                headers=self.headers,
                json=data,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()


llm_service = LLMService()