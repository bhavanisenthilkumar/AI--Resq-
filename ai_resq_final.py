import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# ==========================================
# AI-ResQ FINAL SOFTWARE - DAY 6
# Disaster Search & Rescue System
# ==========================================

# ---------- DATABASE ----------
conn = sqlite3.connect("ai_resq.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS missions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    survivor TEXT,
    condition TEXT,
    priority TEXT,
    distance INTEGER,
    time TEXT
)
""")

conn.commit()


# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("AI-ResQ | Disaster Search & Rescue System")
root.geometry("1000x700")
root.resizable(False, False)

# ---------- TITLE ----------
title = tk.Label(
    root,
    text="AI-ResQ",
    font=("Arial", 28, "bold")
)
title.pack(pady=(15, 0))

subtitle = tk.Label(
    root,
    text="AI-Powered Disaster Search & Rescue System",
    font=("Arial", 13)
)
subtitle.pack(pady=5)


# ---------- STATUS ----------
status = tk.Label(
    root,
    text="MISSION STATUS: READY",
    font=("Arial", 13, "bold")
)
status.pack(pady=10)


# ---------- DASHBOARD ----------
dashboard = tk.Frame(root)
dashboard.pack(pady=10)


def disaster_simulation():
    status.config(
        text="MISSION STATUS: DISASTER AREA SCANNING"
    )

    messagebox.showinfo(
        "Disaster Simulation",
        "Disaster Area Loaded\n\n"
        "✓ Flood Zone\n"
        "✓ Buildings\n"
        "✓ Danger Areas\n"
        "✓ Survivor Locations"
    )


def drone_scan():
    status.config(
        text="MISSION STATUS: DRONE SCANNING"
    )

    messagebox.showinfo(
        "Drone Scanning",
        "Virtual Drone Activated\n\n"
        "🚁 Drone is scanning the disaster area..."
    )


def survivor_detection():
    status.config(
        text="MISSION STATUS: AI DETECTION ACTIVE"
    )

    messagebox.showinfo(
        "AI Survivor Detection",
        "YOLO AI Detection\n\n"
        "👤 Survivor Detected: 3\n\n"
        "AI analysis completed."
    )


def priority_assessment():
    status.config(
        text="MISSION STATUS: PRIORITY ANALYSIS"
    )

    messagebox.showinfo(
        "Priority Assessment",
        "SURVIVOR PRIORITY\n\n"
        "S1 → HIGH 🔴\n"
        "S2 → MEDIUM 🟠\n"
        "S3 → LOW 🟢\n\n"
        "First Rescue Target: S1"
    )


def rescue_route():
    status.config(
        text="MISSION STATUS: RESCUE ROUTE CALCULATED"
    )

    messagebox.showinfo(
        "Rescue Route",
        "🗺️ Rescue Route Calculated\n\n"
        "Drone → Safe Route → S1\n\n"
        "Target: S1\n"
        "Priority: HIGH\n"
        "Route: READY"
    )


def save_mission():
    cursor.execute("""
    INSERT INTO missions
    (survivor, condition, priority, distance, time)
    VALUES (?, ?, ?, ?, ?)
    """, (
        "S1",
        "Critical",
        "HIGH",
        120,
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    conn.commit()

    status.config(
        text="MISSION STATUS: DATA SAVED"
    )

    messagebox.showinfo(
        "Database",
        "Mission information saved successfully!\n\n"
        "Survivor: S1\n"
        "Condition: Critical\n"
        "Priority: HIGH"
    )


def view_records():
    records = tk.Toplevel(root)
    records.title("AI-ResQ | Mission Records")
    records.geometry("700x450")

    heading = tk.Label(
        records,
        text="MISSION RECORDS",
        font=("Arial", 18, "bold")
    )
    heading.pack(pady=15)

    text = tk.Text(
        records,
        width=75,
        height=20,
        font=("Consolas", 10)
    )
    text.pack(padx=15)

    cursor.execute(
        "SELECT * FROM missions"
    )

    rows = cursor.fetchall()

    if not rows:
        text.insert(
            tk.END,
            "No mission records available."
        )
    else:
        for row in rows:
            text.insert(
                tk.END,
                f"Mission ID : {row[0]}\n"
                f"Survivor   : {row[1]}\n"
                f"Condition  : {row[2]}\n"
                f"Priority   : {row[3]}\n"
                f"Distance   : {row[4]} m\n"
                f"Time       : {row[5]}\n"
                f"{'-' * 50}\n"
            )


# ---------- BUTTON STYLE ----------
button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 28,
    "height": 2
}


# ---------- BUTTONS ----------
tk.Button(
    dashboard,
    text="🗺️ 1. DISASTER SIMULATION",
    command=disaster_simulation,
    **button_style
).grid(row=0, column=0, padx=15, pady=10)

tk.Button(
    dashboard,
    text="🚁 2. DRONE SCANNING",
    command=drone_scan,
    **button_style
).grid(row=0, column=1, padx=15, pady=10)

tk.Button(
    dashboard,
    text="🤖 3. AI SURVIVOR DETECTION",
    command=survivor_detection,
    **button_style
).grid(row=1, column=0, padx=15, pady=10)

tk.Button(
    dashboard,
    text="🎯 4. PRIORITY ASSESSMENT",
    command=priority_assessment,
    **button_style
).grid(row=1, column=1, padx=15, pady=10)

tk.Button(
    dashboard,
    text="🛣️ 5. RESCUE ROUTE",
    command=rescue_route,
    **button_style
).grid(row=2, column=0, padx=15, pady=10)

tk.Button(
    dashboard,
    text="💾 6. SAVE MISSION",
    command=save_mission,
    **button_style
).grid(row=2, column=1, padx=15, pady=10)

tk.Button(
    dashboard,
    text="📊 7. VIEW MISSION RECORDS",
    command=view_records,
    **button_style
).grid(row=3, column=0, columnspan=2, pady=15)


# ---------- FOOTER ----------
footer = tk.Label(
    root,
    text="AI-ResQ | Software Prototype | SIH 2026",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=15)


# ---------- CLOSE ----------
def close_program():
    conn.close()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_program
)

root.mainloop()