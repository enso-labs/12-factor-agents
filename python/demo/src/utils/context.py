from src.models.context import Event, Thread
import yaml


def event_to_prompt(event: Event) -> str:
    data = event.data if isinstance(event.data, str) \
           else yaml.dump(event.data.__dict__, sort_keys=False).strip()

    return f"<{event.type}>\n{data}\n</{event.type}>"


def thread_to_prompt(thread: Thread) -> str:
  return '\n\n'.join(event_to_prompt(event) for event in thread.events)