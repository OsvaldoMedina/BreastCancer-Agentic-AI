
from typing import List, Tuple, Dict, Any
from agentic.base import Agent, Message

class ReportAgent(Agent):
    name = "ReportAgent"
    description = "Generates clinician-friendly summaries and reports."

    def can_handle(self, task: str) -> bool:
        keys = ["report", "summary", "informe", "pdf", "doc"]
        return any(k in task.lower() for k in keys)

    def act(self, messages: List[Message], task: str) -> Tuple[str, Dict[str, Any]]:
        note = self.think(messages, task)
        # Build a synthetic report from memory:
        pred = self.recall("last_prediction") or {}
        text = f"BreastDX Report\nPrediction: {pred.get('prediction','n/a')}\nConfidence: {pred.get('confidence','n/a')}"
        artifacts = {"report_text": text}
        self.remember("last_report", text)
        return f"{note}\nReportAgent: report generated.", artifacts
