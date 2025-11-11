
from typing import Dict, Any
import json, time, statistics

def safe_json(obj: Any) -> str:
    try:
        return json.dumps(obj, ensure_ascii=False, indent=2)
    except Exception:
        return str(obj)

def load_patient_record(record_path: str) -> Dict[str, Any]:
    "Demo tool: load a JSON-like patient record if exists."
    try:
        with open(record_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"_error": f"Could not open {record_path}"}

def calc_metrics(y_true, y_pred) -> Dict[str, float]:
    "Demo metrics"
    if not y_true or not y_pred or len(y_true) != len(y_pred):
        return {"error": "mismatched lengths"}
    # Dummy accuracy
    acc = sum(1 for a,b in zip(y_true,y_pred) if a==b)/len(y_true)
    return {"accuracy": acc}

