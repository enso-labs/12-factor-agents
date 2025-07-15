from src.services.llm_service import llm_service

# Factor 1: Natural Language to Tool Calls
def tool_call(intent, data):
    if intent == "add":
        return data["a"] + data["b"]
    elif intent == "subtract":
        return data["a"] - data["b"]
    else:
        raise ValueError("Unknown intent")
    
async def handle_next_step(next_step, thread):
    """
    Handles the next calculator step and appends the result as a tool_response event to the thread.

    Args:
        next_step: An object with attributes 'intent', 'a', and 'b'.
        thread: A Thread object with an 'events' list.

    Returns:
        The updated thread.
    """
    intent = next_step.intent
    a = next_step.a
    b = next_step.b

    if intent == "add":
        result = a + b
    elif intent == "subtract":
        result = a - b
    elif intent == "multiply":
        result = a * b
    elif intent == "divide":
        result = a / b
    else:
        raise ValueError(f"Unknown intent: {intent}")

    print("tool_response", result)
    thread.events.append({
        "type": "tool_response",
        "data": result
    })
    return thread

async def agent_loop(thread):
    while True:
        next_step = await llm_service.chat(thread.serialize())
        print("nextStep", next_step)

        thread.events.append({
            "type": "tool_call",
            "data": next_step
        })

        if next_step.intent in ["done_for_now", "request_more_information"]:
            # response to human, return the thread
            return thread
        elif next_step.intent in ["add", "subtract", "multiply", "divide"]:
            thread = await handle_next_step(next_step, thread)