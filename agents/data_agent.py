
from typing import List, Tuple, Dict, Any
from agentic.base import Agent, Message

class DataAgent(Agent):
    name = "DataAgent"
    description = "Prepares and validates input data; calls data tools."

    def can_handle(self, task: str) -> bool:
        keys = ["load", "dataset", "preprocess", "data"]
        return any(k in task.lower() for k in keys)

    def act(self, messages: List[Message], task: str) -> Tuple[str, Dict[str, Any]]:
        note = self.think(messages, task)
        # In a real system, call self.tools like self.tools['load_json'](...)
        result = {"status": "ok", "details": "Data checked and ready."}
        self.remember("last_data_task", task)
        return f"{note}\nDataAgent: data is ready.", result
