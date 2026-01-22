


import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture("video.mp4")

# List to store ball centers
points = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Green color range (tune if needed)
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        # Largest contour = ball
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 5:
            center = (int(x), int(y))
            points.append(center)

            # Draw ball
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    # Draw trajectory
    for i in range(1, len(points)):
        cv2.line(frame, points[i - 1], points[i], (0, 0, 255), 2)

    cv2.imshow("Green Ball Tracking", frame)
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0 or fps is None:
        fps = 30   # assume normal video FPS

    delay = int(1000 / fps)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
