import pandas as pd
from collections import defaultdict

# --- Input data ---
interviewers = {
    "Albert": 8,
    "Leo":    5,
    "Jean":   6,
    "Josef":  6,
    "Marzia": 9,
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

# --- Build a DataFrame from households dict ---
df_households = pd.DataFrame(
    list(households.items()), columns=["household", "source"]
)

# --- Group households by source value ---
# Each source bucket is a queue of household IDs to assign
source_buckets = (
    df_households.groupby("source")["household"]
    .apply(list)
    .to_dict()
)
# Use list indices as pointers for round-robin drawing
source_pointers = {src: 0 for src in source_buckets}
source_counts = {src: len(lst) for src, lst in source_buckets.items()}
sources_available = sorted(source_buckets.keys())   # [2, 3, 4]

print("Source bucket sizes:", source_counts)
print("Total households:", sum(source_counts.values()))
print("Total interviewer capacity:", sum(interviewers.values()))
print()

# --- Assignment logic ---
# Tracking structures
assignments = []                          # final rows
interviewer_counts  = {i: 0 for i in interviewers}      # total assigned
interviewer_src_counts = {                # per-source counts
    i: {s: 0 for s in sources_available} for i in interviewers
}

# We cycle through interviewers in a round-robin fashion.
# On each turn we pick the source that keeps the interviewer's
# source distribution as balanced as possible, subject to:
#   • the interviewer not being full
#   • that source bucket not being empty

interviewer_list = list(interviewers.keys())

def next_source_for(interviewer):
    """Return the source that best balances this interviewer's current mix,
    among sources that still have unassigned households."""
    cap   = interviewers[interviewer]
    total = interviewer_counts[interviewer]
    if total >= cap:
        return None                  # interviewer is full

    # Ideal fraction of each source = bucket_size / total_households
    total_hh = sum(source_counts.values())
    src_fracs  = {s: source_counts[s] / total_hh for s in sources_available}

    best_src, best_deficit = None, -1
    for src in sources_available:
        if source_pointers[src] >= source_counts[src]:
            continue                 # bucket empty
        # How far below the ideal fraction are we for this source?
        assigned_so_far = interviewer_src_counts[interviewer][src]
        current_frac = assigned_so_far / (total + 1)   # +1 anticipating assignment
        deficit = src_fracs[src] - current_frac
        if deficit > best_deficit:
            best_deficit = deficit
            best_src = src

    return best_src


# Main while loop
any_assigned = True
while any_assigned:
    any_assigned = False
    for interviewer in interviewer_list:
        if interviewer_counts[interviewer] >= interviewers[interviewer]:
            continue                 # this interviewer is already full

        src = next_source_for(interviewer)
        if src is None:
            continue                 # no suitable household left

        # Pull the next household from that source bucket
        ptr = source_pointers[src]
        hh  = source_buckets[src][ptr]
        source_pointers[src] += 1

        # Record the assignment
        assignments.append({
            "interviewer": interviewer,
            "household":   hh,
            "source":      src,
        })
        interviewer_counts[interviewer]      += 1
        interviewer_src_counts[interviewer][src] += 1
        any_assigned = True

# --- Build result DataFrame ---
df_result = pd.DataFrame(assignments, columns=["interviewer", "household", "source"])

# --- Print results ---
print("=" * 55)
print("ASSIGNMENT RESULTS")
print("=" * 55)
print(df_result.to_string(index=False))
print()

print("=" * 55)
print("SUMMARY PER INTERVIEWER")
print("=" * 55)
summary = (
    df_result.groupby(["interviewer", "source"])
    .size()
    .unstack(fill_value=0)
    .rename_axis(None, axis=1)
)
summary.columns = [f"source_{c}" for c in summary.columns]
summary["total"] = summary.sum(axis=1)
summary["capacity"] = pd.Series(interviewers)
print(summary.to_string())
print()

# Unassigned households
assigned_hh   = set(df_result["household"])
all_hh        = set(households.keys())
unassigned_hh = all_hh - assigned_hh
print("=" * 55)
print(f"Assigned households   : {len(assigned_hh)}")
print(f"Unassigned households : {len(unassigned_hh)}")
if unassigned_hh:
    print(f"Unassigned IDs        : {sorted(unassigned_hh)}")
