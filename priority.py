import tkinter as tk

# =========================
# AI-RESQ DAY 4
# Survivor Priority System
# =========================

root = tk.Tk()
root.title("AI-ResQ - Survivor Priority Assessment")
root.geometry("850x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="AI-ResQ | Survivor Priority Assessment",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

info = tk.Label(
    root,
    text="AI analyzes survivor condition and assigns rescue priority",
    font=("Arial", 11)
)
info.pack(pady=5)

# Survivor data
survivors = [
    {
        "id": "S1",
        "condition": "Critical",
        "distance": 120,
        "priority": "HIGH"
    },
    {
        "id": "S2",
        "condition": "Injured",
        "distance": 250,
        "priority": "MEDIUM"
    },
    {
        "id": "S3",
        "condition": "Safe",
        "distance": 400,
        "priority": "LOW"
    }
]

# Priority scores
priority_score = {
    "Critical": 3,
    "Injured": 2,
    "Safe": 1
}


def calculate_priority(survivor):
    condition_score = priority_score[survivor["condition"]]

    # Higher condition score = higher priority
    # Shorter distance gets a small advantage
    distance_score = max(0, 500 - survivor["distance"]) / 500

    total_score = condition_score + distance_score

    return total_score


def show_priority():
    # Calculate scores
    for survivor in survivors:
        survivor["score"] = calculate_priority(survivor)

    # Sort highest priority first
    sorted_survivors = sorted(
        survivors,
        key=lambda x: x["score"],
        reverse=True
    )

    # Clear previous results
    result.delete("1.0", tk.END)

    result.insert(
        tk.END,
        "RESCUE PRIORITY ORDER\n"
        "========================\n\n"
    )

    for position, survivor in enumerate(
        sorted_survivors,
        start=1
    ):

        result.insert(
            tk.END,
            f"{position}. {survivor['id']}\n"
        )

        result.insert(
            tk.END,
            f"   Condition : {survivor['condition']}\n"
        )

        result.insert(
            tk.END,
            f"   Distance  : {survivor['distance']} m\n"
        )

        result.insert(
            tk.END,
            f"   Priority  : {survivor['priority']}\n"
        )

        result.insert(
            tk.END,
            f"   AI Score  : {survivor['score']:.2f}\n\n"
        )

    result.insert(
        tk.END,
        "🚨 FIRST RESCUE TARGET: "
        + sorted_survivors[0]["id"]
    )


# Result box
result = tk.Text(
    root,
    width=65,
    height=18,
    font=("Consolas", 11)
)
result.pack(pady=15)

# Button
button = tk.Button(
    root,
    text="🎯 ANALYZE PRIORITY",
    font=("Arial", 13, "bold"),
    command=show_priority
)
button.pack(pady=10)

root.mainloop()