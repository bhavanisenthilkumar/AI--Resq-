import tkinter as tk
import math

# =========================
# AI-RESQ DAY 2
# Drone Area Scanning
# =========================

root = tk.Tk()
root.title("AI-ResQ - Day 2 Drone Scanning")
root.geometry("950x700")
root.resizable(False, False)

# ---------- TITLE ----------
title = tk.Label(
    root,
    text="AI-ResQ | Intelligent Drone Scanning System",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# ---------- MAIN CANVAS ----------
canvas = tk.Canvas(
    root,
    width=850,
    height=450,
    bg="lightgray"
)
canvas.pack()

# Disaster Area
canvas.create_rectangle(
    40, 40, 810, 410,
    fill="white",
    outline="black",
    width=2
)

# ---------- DANGER ZONES ----------
danger_zones = [
    (70, 70, 230, 140),
    (300, 300, 500, 380),
    (620, 80, 770, 160)
]

for zone in danger_zones:
    canvas.create_rectangle(
        *zone,
        fill="skyblue",
        outline="blue"
    )

# ---------- BUILDINGS ----------
buildings = [
    (140, 180, 220, 250),
    (350, 120, 430, 200),
    (540, 220, 630, 300),
    (680, 300, 760, 380)
]

for x1, y1, x2, y2 in buildings:
    canvas.create_rectangle(
        x1, y1, x2, y2,
        fill="gray",
        outline="black"
    )

    canvas.create_text(
        (x1 + x2) / 2,
        (y1 + y2) / 2,
        text="BUILDING",
        font=("Arial", 8, "bold")
    )

# ---------- SURVIVORS ----------
survivors = {
    "S1": (280, 180),
    "S2": (450, 250),
    "S3": (580, 350)
}

survivor_objects = {}
detected = set()

for name, (x, y) in survivors.items():

    obj = canvas.create_oval(
        x - 10,
        y - 10,
        x + 10,
        y + 10,
        fill="red",
        outline="black"
    )

    canvas.create_text(
        x,
        y - 20,
        text=name,
        font=("Arial", 10, "bold")
    )

    survivor_objects[name] = obj


# ---------- DRONE ----------
drone_x = 80
drone_y = 60

drone = canvas.create_oval(
    drone_x - 15,
    drone_y - 15,
    drone_x + 15,
    drone_y + 15,
    fill="black"
)

drone_label = canvas.create_text(
    drone_x,
    drone_y,
    text="D",
    fill="white",
    font=("Arial", 10, "bold")
)


# ---------- STATUS ----------
status = tk.Label(
    root,
    text="Mission Status: READY",
    font=("Arial", 13, "bold")
)
status.pack(pady=5)


progress = tk.Label(
    root,
    text="Scanning Progress: 0%",
    font=("Arial", 11)
)
progress.pack()


# ---------- SURVIVOR STATUS ----------
survivor_status = tk.Label(
    root,
    text="S1: NOT DETECTED | S2: NOT DETECTED | S3: NOT DETECTED",
    font=("Arial", 11, "bold")
)
survivor_status.pack(pady=5)


# ---------- SCANNING VARIABLES ----------
running = False
scan_x = 80
scan_y = 60
direction = 1
scan_steps = 0
total_steps = 140


# ---------- UPDATE SURVIVOR STATUS ----------
def update_survivor_status():

    text = ""

    for name in survivors:

        if name in detected:
            text += f"{name}: DETECTED ✅   "
        else:
            text += f"{name}: NOT DETECTED ⏳   "

    survivor_status.config(text=text)


# ---------- CHECK SURVIVORS ----------
def detect_survivors():

    for name, (sx, sy) in survivors.items():

        distance = math.sqrt(
            (scan_x - sx) ** 2 +
            (scan_y - sy) ** 2
        )

        if distance < 80:

            if name not in detected:

                detected.add(name)

                canvas.itemconfig(
                    survivor_objects[name],
                    fill="green"
                )

    update_survivor_status()


# ---------- DRONE MOVEMENT ----------
def move_drone():

    global scan_x
    global scan_y
    global direction
    global scan_steps
    global running

    if not running:
        return

    # Horizontal scanning
    scan_x += 5 * direction

    # Change row when edge reached
    if scan_x >= 780:

        scan_x = 780
        direction = -1
        scan_y += 40
        scan_steps += 1

    elif scan_x <= 80:

        scan_x = 80
        direction = 1
        scan_y += 40
        scan_steps += 1

    # Reset after full scan
    if scan_y >= 390:

        scan_y = 60
        scan_x = 80
        direction = 1
        scan_steps = 0

        status.config(
            text="Mission Status: AREA SCAN COMPLETED"
        )

        progress.config(
            text="Scanning Progress: 100%"
        )

        running = False
        return

    # Move drone
    canvas.coords(
        drone,
        scan_x - 15,
        scan_y - 15,
        scan_x + 15,
        scan_y + 15
    )

    canvas.coords(
        drone_label,
        scan_x,
        scan_y
    )

    # Detect survivors
    detect_survivors()

    # Calculate progress
    percentage = min(
        int((scan_y - 60) / 330 * 100),
        100
    )

    progress.config(
        text=f"Scanning Progress: {percentage}%"
    )

    status.config(
        text=f"Mission Status: DRONE SCANNING | Detected: {len(detected)}/3"
    )

    root.after(50, move_drone)


# ---------- START MISSION ----------
def start_mission():

    global running
    global scan_x
    global scan_y
    global direction
    global detected

    if running:
        return

    running = True

    scan_x = 80
    scan_y = 60
    direction = 1
    detected.clear()

    # Reset survivor colours
    for obj in survivor_objects.values():
        canvas.itemconfig(obj, fill="red")

    update_survivor_status()

    status.config(
        text="Mission Status: DRONE TAKEOFF..."
    )

    move_drone()



# ---------- BUTTON ----------
start_button = tk.Button(
    root,
    text="🚁 START MISSION",
    font=("Arial", 13, "bold"),
    command=start_mission
)

start_button.pack(pady=8)


# ---------- FOOTER ----------
footer = tk.Label(
    root,
    text="AI-ResQ | Software-Based Disaster Search & Rescue Simulation",
    font=("Arial", 9)
)

footer.pack(pady=5)


root.mainloop()