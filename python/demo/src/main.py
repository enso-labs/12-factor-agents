import asyncio
from dotenv import load_dotenv

load_dotenv()

# Factor 1: Natural Language to Tool Calls
def tool_call(intent, data):
	if intent == "add":
		return data["a"] + data["b"]
	elif intent == "subtract":
		return data["a"] - data["b"]
	else:
		raise ValueError("Unknown intent")
	
# Factor 2: Own your prompts
PROMPT_TEMPLATE = "You are a calculator. Given an intent and numbers, perform the calculation."

# Factor 3: Own your context window
def get_context(history):
	# Only keep the last 3 interactions for context
	return history[-3:]

# Factor 12: Make your agent a stateless reducer
class StatelessAgent:
	def step(self, state):
		# state: {"intent": ..., "data": ..., "history": [...]}
		context = get_context(state["history"])
		result = tool_call(state["intent"], state["data"])
		state["history"].append({"intent": state["intent"], "data": state["data"], "result": result})
		return state

async def main():
	state = {
		"intent": "add",
		"data": {"a": 5, "b": 3},
		"history": []
	}
	agent = StatelessAgent()
	new_state = agent.step(state)
	print(new_state["history"][-1]) 

if __name__ == "__main__":
	asyncio.run(main())