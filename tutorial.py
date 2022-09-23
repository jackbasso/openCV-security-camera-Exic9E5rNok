from turtle import width
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # face detection
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")  # face detection

while True:
  # read by frame
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3) # drawing an image over frame

    cv2.imshow("Jack's Camera", frame) # Video frame name and what it´s going to show

    if cv2.waitKey(1) == ord('q'):
        break;

# release cpu resources
cap.release()
cv2.destroyAllWindows()
