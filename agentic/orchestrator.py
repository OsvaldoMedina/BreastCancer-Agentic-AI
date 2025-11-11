
from typing import List, Dict, Any
from agentic.base import Message, Memory
from agents.data_agent import DataAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.report_agent import ReportAgent

class Orchestrator:
    def __init__(self, tools: Dict[str, Any] | None = None):
        self.memory = Memory()
        self.agents = [
            DataAgent(memory=self.memory, tools=tools or {}),
            DiagnosisAgent(memory=self.memory, tools=tools or {}),
            ReportAgent(memory=self.memory, tools=tools or {}),
        ]
        self.messages: List[Message] = []

    def plan(self, goal: str) -> List[str]:
        "Very simple planner -> break the goal into steps"
        g = goal.lower()
        steps = []
        if any(w in g for w in ["data","dataset","preprocess","load"]):
            steps.append("Prepare data")
        steps.append("Run diagnosis")
        steps.append("Create report")
        return steps

    def route(self, step: str):
        "Route step to the most capable agent"
        for agent in self.agents:
            if agent.can_handle(step):
                return agent
        # fallback to first
        return self.agents[0]

    def reflect_and_retry(self, response: str, artifacts: Dict[str, Any]):
        "Minimal reflection hook"
        # You can implement checks here (e.g., is confidence too low?) and trigger retries.
        return response, artifacts

    def run(self, goal: str) -> Dict[str, Any]:
        plan = self.plan(goal)
        results = {"goal": goal, "steps": plan, "artifacts": {}}
        for step in plan:
            agent = self.route(step)
            msg = Message(role="system", content=f"STEP: {step}")
            self.messages.append(msg)
            resp, art = agent.act(self.messages, step)
            self.messages.append(Message(role="agent", content=resp, meta={"agent": agent.name}))
            resp, art = self.reflect_and_retry(resp, art)
            results["artifacts"][step] = art
        results["memory"] = self.memory.dump()
        return results
