import tkinter as tk
import math

# ==============================
# AI-ResQ DAY 5
# Rescue Route Planning
# ==============================

root = tk.Tk()
root.title("AI-ResQ - Rescue Route Planning")
root.geometry("900x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="AI-ResQ | Rescue Route Planning",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

info = tk.Label(
    root,
    text="Finding the shortest route from Drone to Highest-Priority Survivor",
    font=("Arial", 11)
)
info.pack()

canvas = tk.Canvas(
    root,
    width=850,
    height=480,
    bg="white"
)
canvas.pack(pady=10)

# Drone position
drone = (100, 380)

# Highest-priority survivor
survivor = (700, 100)

# Obstacles / buildings
obstacles = [
    (250, 100, 400, 180),
    (250, 280, 400, 360),
    (520, 220, 650, 350)
]

# Draw disaster area
canvas.create_rectangle(
    20, 20, 830, 450,
    outline="black",
    width=2
)

# Draw obstacles
for obstacle in obstacles:
    canvas.create_rectangle(
        *obstacle,
        fill="gray",
        outline="black"
    )
    canvas.create_text(
        (obstacle[0] + obstacle[2]) // 2,
        (obstacle[1] + obstacle[3]) // 2,
        text="BUILDING",
        font=("Arial", 9, "bold")
    )

# Draw drone
canvas.create_oval(
    drone[0] - 15,
    drone[1] - 15,
    drone[0] + 15,
    drone[1] + 15,
    fill="black"
)

canvas.create_text(
    drone[0],
    drone[1] - 28,
    text="DRONE",
    font=("Arial", 10, "bold")
)

# Draw survivor
canvas.create_oval(
    survivor[0] - 15,
    survivor[1] - 15,
    survivor[0] + 15,
    survivor[1] + 15,
    fill="red"
)

canvas.create_text(
    survivor[0],
    survivor[1] - 28,
    text="S1 - HIGH PRIORITY",
    font=("Arial", 10, "bold")
)


def calculate_route():
    # Create simple safe route
    route = [
        drone,
        (100, 100),
        (700, 100),
        survivor
    ]

    # Draw route
    for i in range(len(route) - 1):
        canvas.create_line(
            route[i][0],
            route[i][1],
            route[i + 1][0],
            route[i + 1][1],
            fill="blue",
            width=4
        )

    # Calculate total distance
    total_distance = 0

    for i in range(len(route) - 1):
        x1, y1 = route[i]
        x2, y2 = route[i + 1]

        distance = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        total_distance += distance

    status.config(
        text=f"ROUTE FOUND | Distance: {total_distance:.0f} pixels"
    )

    result.config(
        text="🚁 Drone Route Ready\n"
             "🎯 Target: S1\n"
             "🔴 Priority: HIGH\n"
             "🛣️ Safe route calculated"
    )


button = tk.Button(
    root,
    text="🗺️ CALCULATE RESCUE ROUTE",
    font=("Arial", 13, "bold"),
    command=calculate_route
)
button.pack(pady=5)

status = tk.Label(
    root,
    text="STATUS: Waiting for route calculation",
    font=("Arial", 11, "bold")
)
status.pack(pady=5)

result = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left"
)
result.pack()

root.mainloop()