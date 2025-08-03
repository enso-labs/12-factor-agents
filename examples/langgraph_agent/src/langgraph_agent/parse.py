from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, AIMessage
import json

def input_parser(
    messages: list[BaseMessage],
    llm_response_prefix: str = "\n\n ai_response:"
) -> str:
    xml_lines = ["<thread>"]
    for message in messages:
        if isinstance(message, HumanMessage):
            xml_lines.append(
                f'  <event id="{message.id}" type="{message.type}">{message.content}</event>'
            )
        elif isinstance(message, ToolMessage):
            xml_lines.append(
                f'  <event id="{message.tool_call_id}" type="tool_output" name="{message.name}" status="{message.status}">{message.content}</event>'
            )
        elif isinstance(message, AIMessage):
            if getattr(message, "tool_calls", None):
                for tool_call in message.tool_calls:
                    xml_lines.append(
                        f'  <event id="{tool_call["id"]}" type="tool_input" name="{tool_call["name"]}">{json.dumps(tool_call["args"])}</event>'
                    )
            else:
                xml_lines.append(
                    f'  <event id="{message.id}" type="{message.type}">{message.content}</event>'
                )
    xml_lines.append("</thread>")
    return "\n".join(xml_lines) + llm_response_prefix