import tkinter as tk
import math

# Main Window
root = tk.Tk()
root.title("AI-ResQ - Disaster Rescue Simulation")
root.geometry("900x600")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="AI-ResQ | Disaster Search & Rescue Simulation",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Simulation Canvas
canvas = tk.Canvas(
    root,
    width=850,
    height=430,
    bg="lightgray"
)
canvas.pack()

# Disaster Zone
canvas.create_rectangle(
    50, 50, 800, 400,
    fill="white",
    outline="black",
    width=2
)

# Danger / Water Zones
canvas.create_rectangle(80, 80, 250, 150, fill="skyblue")
canvas.create_rectangle(300, 300, 500, 370, fill="skyblue")
canvas.create_rectangle(600, 100, 760, 180, fill="skyblue")

# Buildings
buildings = [
    (150, 180, 230, 250),
    (350, 120, 430, 200),
    (550, 230, 640, 310),
    (680, 300, 750, 370)
]

for x1, y1, x2, y2 in buildings:
    canvas.create_rectangle(
        x1, y1, x2, y2,
        fill="gray",
        outline="black"
    )
    canvas.create_text(
        (x1 + x2) // 2,
        (y1 + y2) // 2,
        text="BUILDING",
        font=("Arial", 8, "bold")
    )

# Survivors
survivors = {
    "S1": (300, 200),
    "S2": (450, 280),
    "S3": (570, 440)
}

survivor_objects = {}

for name, (x, y) in survivors.items():
    obj = canvas.create_oval(
        x - 10, y - 10,
        x + 10, y + 10,
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

# Virtual Drone
drone_x = 100
drone_y = 250

drone = canvas.create_oval(
    drone_x - 15,
    drone_y - 15,
    drone_x + 15,
    drone_y + 15,
    fill="black"
)

canvas.create_text(
    drone_x,
    drone_y,
    text="D",
    fill="white",
    font=("Arial", 10, "bold")
)

# Status
status = tk.Label(
    root,
    text="Mission Status: READY",
    font=("Arial", 13, "bold")
)
status.pack(pady=5)

# Detection variables
detected = set()
mission_running = False


def start_mission():
    global mission_running

    if not mission_running:
        mission_running = True
        status.config(text="Mission Status: DRONE SCANNING...")
        move_drone()


def move_drone():
    global drone_x, mission_running

    if not mission_running:
        return

    # Move drone
    drone_x += 5

    if drone_x > 750:
        drone_x = 100

    canvas.coords(
        drone,
        drone_x - 15,
        drone_y - 15,
        drone_x + 15,
        drone_y + 15
    )

    # Check survivor detection
    for name, (sx, sy) in survivors.items():

        distance = math.sqrt(
            (drone_x - sx) ** 2 +
            (drone_y - sy) ** 2
        )

        if distance < 100:
            if name not in detected:
                detected.add(name)

                canvas.itemconfig(
                    survivor_objects[name],
                    fill="green"
                )

    status.config(
        text=f"Mission Status: SCANNING | Survivors Detected: {len(detected)}/3"
    )

    root.after(50, move_drone)


# Start Button
button = tk.Button(
    root,
    text="START MISSION",
    font=("Arial", 12, "bold"),
    command=start_mission
)

button.pack(pady=5)

root.mainloop()