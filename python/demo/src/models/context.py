from typing import List, Literal
from dataclasses import dataclass
import yaml

class UserInput:
	query: str

class DoneForNow:
	reason: str

@dataclass
class Event:
	# could just use string, or could be explicit - up to you
	type: Literal["user_input", "done_for_now"]
	data: UserInput | DoneForNow
	
	def to_prompt(self) -> str:
		data = self.data if isinstance(self.data, str) \
			else yaml.dump(self.data.__dict__, sort_keys=False).strip()

		return f"<{self.type}>\n{data}\n</{self.type}>"

@dataclass
class Thread:
	events: List[Event]

	def serialize(self) -> str:
		return '\n\n'.join(event.to_prompt() for event in self.events)