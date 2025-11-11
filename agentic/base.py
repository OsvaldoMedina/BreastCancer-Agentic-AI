
"""
Simple Agentic AI base classes without external deps.
You can plug in LangGraph/LangChain later if desired.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
import abc, json, time

class Message:
    def __init__(self, role: str, content: str, meta: Optional[dict]=None):
        self.role = role
        self.content = content
        self.meta = meta or {}
    def to_dict(self):
        return {"role": self.role, "content": self.content, "meta": self.meta}

class Agent(abc.ABC):
    name: str = "BaseAgent"
    description: str = "Abstract base agent"
    def __init__(self, memory=None, tools: Optional[Dict[str, Any]]=None):
        self.memory = memory
        self.tools = tools or {}

    @abc.abstractmethod
    def can_handle(self, task: str) -> bool:
        ...

    @abc.abstractmethod
    def act(self, messages: List[Message], task: str) -> Tuple[str, Dict[str, Any]]:
        "Return (response, artifacts)"
        ...

    def think(self, messages: List[Message], task: str) -> str:
        "Very lightweight reflection (replace with a proper chain-of-thought in production)"
        context = " | ".join(m.content for m in messages[-3:]) if messages else ""
        return f"[{self.name} Reflection] Considering context: {context[:200]} -> task: {task}"

    def recall(self, key: str) -> Optional[Any]:
        if not self.memory: return None
        return self.memory.get(key)

    def remember(self, key: str, value: Any) -> None:
        if not self.memory: return
        self.memory.set(key, value)

class Memory:
    def __init__(self):
        self._kv = {}
    def get(self, key: str):
        return self._kv.get(key)
    def set(self, key: str, value):
        self._kv[key] = value
    def dump(self):
        return dict(self._kv)

class ToolRegistry(dict):
    def register(self, name: str, fn):
        self[name] = fn

def tool(name):
    def deco(fn):
        fn._tool_name = name
        return fn
    return deco
