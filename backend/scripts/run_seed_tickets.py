"""E2E validation script — hits the running server via HTTP.

Usage:
    uvicorn app.main:app --port 8000 &
    python scripts/run_seed_tickets.py

Exit code 0  if accuracy >= 80% AND zero 500s.
Exit code 1  otherwise.
"""
import json
import sys
import time
from pathlib import Path

import httpx

BASE_URL = "http://localhost:8000"
DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "seed_tickets.json"


def main() -> None:
    with open(DATA_PATH) as f:
        seed_tickets = json.load(f)

    correct = 0
    errors_500 = 0
    total = len(seed_tickets)

    print(f"Running {total} seed tickets against {BASE_URL}/tickets/analyze\n")

    for raw in seed_tickets:
        tid = raw["id"]
        expected = raw["expected_category"]

        t0 = time.perf_counter()
        try:
            resp = httpx.post(
                f"{BASE_URL}/tickets/analyze",
                json={
                    "subject": raw["subject"],
                    "body": raw["body"],
                    "user_email": raw.get("user_email"),
                },
                timeout=120.0,
            )
        except httpx.ConnectError:
            print(f"  ✗ {tid}  CONNECTION REFUSED — is the server running at {BASE_URL}?")
            sys.exit(2)

        elapsed_ms = (time.perf_counter() - t0) * 1000

        if resp.status_code == 500:
            errors_500 += 1
            print(f"  ✗ {tid}  HTTP 500  {elapsed_ms:.0f}ms  {resp.json().get('detail','')}")
            continue

        if resp.status_code != 200:
            print(f"  ✗ {tid}  HTTP {resp.status_code}  {elapsed_ms:.0f}ms")
            continue

        data = resp.json()
        got = data.get("classification", {}).get("category", "")
        match = got == expected
        if match:
            correct += 1

        symbol = "✓" if match else "✗"
        print(
            f"  {symbol} {tid}  {elapsed_ms:.0f}ms  "
            f"expected={expected!r:<30} got={got!r}"
        )

    accuracy = correct / total if total else 0.0
    print(f"\n{'='*60}")
    print(f"Total:      {total}")
    print(f"Accuracy:   {accuracy:.1%}  ({correct}/{total})")
    print(f"500 errors: {errors_500}")

    if accuracy >= 0.80 and errors_500 == 0:
        print("✅ PASS — Week 1 acceptance criteria met")
        sys.exit(0)
    else:
        reasons = []
        if accuracy < 0.80:
            reasons.append(f"accuracy {accuracy:.1%} < 80%")
        if errors_500 > 0:
            reasons.append(f"{errors_500} HTTP 500 error(s)")
        print(f"❌ FAIL — {', '.join(reasons)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
