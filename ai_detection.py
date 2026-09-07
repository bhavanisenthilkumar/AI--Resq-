from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open camera
cap = cv2.VideoCapture(0)

print("================================")
print("AI-ResQ SURVIVOR DETECTION")
print("================================")
print("AI Camera Started")
print("Press Q to stop")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera could not be opened")
        break

    # Detect only PERSON (class 0)
    results = model(
        frame,
        classes=[0],
        conf=0.50,
        verbose=False
    )

    # Count detected people
    person_count = len(results[0].boxes)

    # Draw AI bounding boxes
    frame = results[0].plot()

    # Display survivor information
    if person_count > 0:

        cv2.putText(
            frame,
            f"SURVIVOR DETECTED: {person_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "STATUS: RESCUE REQUIRED",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

    else:

        cv2.putText(
            frame,
            "NO SURVIVOR DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 255),
            2
        )

    # Show result
    cv2.imshow(
        "AI-ResQ | Survivor Detection",
        frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()