
"""
Entry point to run the Agentic AI workflow for the BreastCancer project.

Usage:
    python run_agentic.py "Diagnose patient 123 and create a report"
"""
import sys, json
from agentic.orchestrator import Orchestrator

def main():
    goal = sys.argv[1] if len(sys.argv) > 1 else "Run diagnosis and report"
    orch = Orchestrator()
    result = orch.run(goal)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
