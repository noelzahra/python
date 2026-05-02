"""
Assign households to interviewers such that:
  1. Each interviewer's total does not exceed their max count.
  2. Each interviewer receives an approximately equal proportion of
     source values (2, 3, 4) matching the global distribution.
"""

import itertools
import pandas as pd
from collections import defaultdict

# ── Data ──────────────────────────────────────────────────────────────────────
interviewers = {
    "Albert": 20, "Leo": 10, "Jean": 12,
    "Josef": 12, "Marzia": 15, "Michelle": 8
}

households = {
    1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2,
    13:3, 14:3, 15:3, 16:3, 17:3, 18:3, 19:3, 20:3, 21:3, 22:3, 24:3,
    25:3, 26:3, 27:3, 28:3, 29:3, 30:3, 31:4, 32:4, 33:4, 35:4, 36:4,
    37:4, 38:4, 39:4, 40:4, 41:4, 42:2, 43:2, 44:2, 45:2, 46:2, 47:2,
    48:2, 49:2, 50:2, 51:2, 52:2, 53:3, 54:3, 55:3, 56:3, 57:3, 58:3,
    59:3, 60:3, 61:3, 62:3, 63:3, 64:3, 65:3, 66:3, 68:3, 69:3, 70:3,
    71:4, 72:4, 73:4, 75:4, 76:4, 77:4, 78:4, 79:4, 80:4, 67:4
}

# ── Source buckets ────────────────────────────────────────────────────────────
source_buckets = defaultdict(list)
for hh, src in households.items():
    source_buckets[src].append(hh)

source_values = sorted(source_buckets.keys())   # [2, 3, 4]
total_hh      = len(households)
source_ratio  = {s: len(source_buckets[s]) / total_hh for s in source_values}

print("Global source distribution:")
for s in source_values:
    n = len(source_buckets[s])
    print(f"  Source {s}: {n:>3} hh  ({source_ratio[s]*100:.1f} %)")

# ── Per-interviewer source quotas ─────────────────────────────────────────────
def compute_quotas(max_count):
    raw    = {s: source_ratio[s] * max_count for s in source_values}
    quotas = {s: int(raw[s]) for s in source_values}
    remainder = max_count - sum(quotas.values())
    fracs = sorted(source_values, key=lambda s: -(raw[s] - quotas[s]))
    for i in range(remainder):
        quotas[fracs[i % len(fracs)]] += 1
    return quotas

interviewer_quotas = {name: compute_quotas(mx) for name, mx in interviewers.items()}

print("\nPer-interviewer source quotas:")
hdr = f"{'Interviewer':<12} {'Max':>4}  " + "  ".join(f"Src{s}" for s in source_values)
print(hdr)
print("-" * len(hdr))

for name, mx in interviewers.items():
    q = interviewer_quotas[name]
    cols = "  ".join(f"{q[s]:>4}" for s in source_values)
    print(f"{name:<12} {mx:>4}   {cols}")

# ── Source queues ─────────────────────────────────────────────────────────────
src_queues = {s: list(source_buckets[s]) for s in source_values}

# ── Assignment state ──────────────────────────────────────────────────────────
remaining_quota = {name: dict(interviewer_quotas[name]) for name in interviewers}
remaining_total = dict(interviewers)
assignments = []

# ── Main loop ─────────────────────────────────────────────────────────────────
interviewer_cycle = itertools.cycle(list(interviewers.keys()))
max_iterations    = total_hh * len(interviewers) * 2

for _ in range(max_iterations):
    if all(len(q) == 0 for q in src_queues.values()):
        break
    if all(remaining_total[n] == 0 for n in interviewers):
        break

    name = next(interviewer_cycle)
    if remaining_total[name] == 0:
        continue

    # Prefer source with largest remaining quota that still has households
    available = [(remaining_quota[name][s], s)
                 for s in source_values
                 if remaining_quota[name][s] > 0 and len(src_queues[s]) > 0]

    if not available:
        # quota met for all sources; fill remainder with whatever is left
        available = [(1, s) for s in source_values if len(src_queues[s]) > 0]

    if not available:
        continue

    _, chosen_src = max(available)
    hh_id = src_queues[chosen_src].pop(0)

    assignments.append({"household": hh_id, "source": chosen_src, "interviewer": name})
    remaining_total[name] -= 1
    if remaining_quota[name][chosen_src] > 0:
        remaining_quota[name][chosen_src] -= 1

# ── Build DataFrame ───────────────────────────────────────────────────────────
df = pd.DataFrame(assignments).sort_values("household").reset_index(drop=True)

print(f"\nTotal assigned: {len(df)} / {total_hh}")
print("\n── Assignment DataFrame ──")
print(df.to_string(index=False))

# ── Summary ───────────────────────────────────────────────────────────────────
print("\n── Per-interviewer actual distribution ──")
print(hdr)
print("-" * len(hdr))

for name, mx in interviewers.items():
    sub  = df[df["interviewer"] == name]
    cols = "  ".join(f"{int((sub['source']==s).sum()):>4}" for s in source_values)
    print(f"{name:<12} {len(sub):>4}   {cols}   (max {mx})")

# ── Save ──────────────────────────────────────────────────────────────────────
output_path = r"NHHs-interviewers.xlsx"
df.to_excel(output_path, engine="openpyxl", index=False)
print(f"\nSaved → {output_path}")
