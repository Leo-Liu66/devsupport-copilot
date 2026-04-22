"""Baseline runner — calls analyze_ticket() directly, no HTTP layer.

Outputs backend/scripts/baseline_metrics.json:
{
  "total": 31,
  "completed": <int>,
  "category_accuracy": <float 0..1>,
  "p1_recall": <float 0..1>,
  "mean_workflow_ms": <float>,
  "mean_per_node_ms": {"classify": ..., "retrieve": ..., "draft": ..., "route": ...},
  "edge_case_count": <int>,
  "edge_case_ids": [...],
  "per_ticket": [ {"id":..., "expected":..., "got":..., "duration_ms":...}, ... ]
}
"""
import asyncio
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.models.ticket import TicketInput
from app.services.workflow import analyze_ticket

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "seed_tickets.json"
OUT_PATH = Path(__file__).resolve().parent / "baseline_metrics.json"


async def run() -> None:
    with open(DATA_PATH) as f:
        seed_tickets = json.load(f)

    per_ticket = []
    node_totals: dict[str, list[float]] = {"classify": [], "retrieve": [], "draft": [], "route": []}
    category_correct = 0
    p1_total = 0
    p1_correct = 0
    edge_case_ids = []
    completed = 0

    for raw in seed_tickets:
        tid = raw["id"]
        expected_category = raw["expected_category"]
        expected_action = raw.get("expected_action")

        ticket = TicketInput(
            subject=raw["subject"],
            body=raw["body"],
            user_email=raw.get("user_email"),
        )

        start = time.perf_counter()
        error = None
        result = None
        try:
            result = await analyze_ticket(ticket)
            completed += 1
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"

        elapsed_ms = (time.perf_counter() - start) * 1000

        got_category = result.classification.category if result else None
        got_action = result.action if result else None
        got_severity = result.classification.severity if result else None

        cat_match = got_category == expected_category
        if cat_match:
            category_correct += 1

        if expected_action != got_action:
            edge_case_ids.append(tid)

        if got_severity == "P1 - Critical" or raw.get("expected_severity") == "P1 - Critical":
            p1_total += 1
            if got_severity == "P1 - Critical":
                p1_correct += 1

        if result:
            for step in result.workflow_trace:
                if step.node in node_totals and step.duration_ms is not None:
                    node_totals[step.node].append(float(step.duration_ms))

        status = "✓" if cat_match else "✗"
        print(
            f"  {status} {tid}  expected={expected_category!r:<30} got={got_category!r:<30}"
            + (f"  ERROR: {error}" if error else f"  {elapsed_ms:.0f}ms")
        )

        per_ticket.append({
            "id": tid,
            "expected_category": expected_category,
            "got_category": got_category,
            "expected_action": expected_action,
            "got_action": got_action,
            "duration_ms": round(elapsed_ms, 1),
            "error": error,
        })

    total = len(seed_tickets)
    category_accuracy = category_correct / total if total else 0.0
    p1_recall = p1_correct / p1_total if p1_total else 1.0

    all_durations = [t["duration_ms"] for t in per_ticket if t["error"] is None]
    mean_workflow_ms = sum(all_durations) / len(all_durations) if all_durations else 0.0

    mean_per_node_ms = {
        node: round(sum(vals) / len(vals), 1) if vals else 0.0
        for node, vals in node_totals.items()
    }

    metrics = {
        "total": total,
        "completed": completed,
        "category_accuracy": round(category_accuracy, 4),
        "p1_recall": round(p1_recall, 4),
        "mean_workflow_ms": round(mean_workflow_ms, 1),
        "mean_per_node_ms": mean_per_node_ms,
        "edge_case_count": len(edge_case_ids),
        "edge_case_ids": edge_case_ids,
        "per_ticket": per_ticket,
    }

    with open(OUT_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

    print()
    print("=" * 60)
    print(f"Total:              {total}")
    print(f"Completed:          {completed}")
    print(f"Category accuracy:  {category_accuracy:.1%}  ({category_correct}/{total})")
    print(f"P1 recall:          {p1_recall:.1%}  ({p1_correct}/{p1_total})")
    print(f"Mean workflow ms:   {mean_workflow_ms:.0f}ms")
    print(f"Mean per node:      {mean_per_node_ms}")
    print(f"Edge cases:         {len(edge_case_ids)}  {edge_case_ids}")
    print(f"Metrics saved to:   {OUT_PATH}")


if __name__ == "__main__":
    asyncio.run(run())
