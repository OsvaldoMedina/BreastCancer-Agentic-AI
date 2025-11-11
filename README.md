
# Upgrade: Agent IA → Agentic AI (BreastCancer)


This upgrade introduces an **agentic architecture** with:
- **Planner/Orchestrator** (`agentic/orchestrator.py`) that decomposes a goal into steps and routes each step to the best agent.
- **Specialized Agents** (`agents/`): `DataAgent`, `DiagnosisAgent`, `ReportAgent` with minimal reflection and shared memory.
- **Shared Memory** (`agentic/base.py: Memory`) to pass context (e.g., predictions) across agents.
- **Tool Registry** (`tools/`) to plug domain tools (loading records, metrics, etc.).
- **Config** (`configs/agentic_config.yaml`) to declare agents and tools.

## How to run
```bash
# inside the project root
python run_agentic.py "Diagnose patient X and create a report"
```

## Where to plug your model
- Edit `agents/diagnosis_agent.py` in the `act` method and call your real model pipeline.
- Use `tools/` to register domain-specific utilities (I/O, metrics, preprocessing).
- If you later add LangChain/LangGraph, replace the simple base classes with their runtimes.

## Notes
- No external dependencies are required for this skeleton; it runs with the Python standard library.
- You can progressively enhance: add a TaskGraph, retries with confidence thresholds, and a vector DB memory.
