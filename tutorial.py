from turtle import width
import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # face detection
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")  # face detection

detection = False
# record only when face is detected
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

# need the frame size to be record
frame_size = (int(cap.get(3)), int(cap.get(4)))
# four character code for my video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)
while True:
  # read by frame
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

    # record if there are faces or bodies
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stop Recording!")
            else:
                timer_started = True
                detection_stopped_time = time.time() # we could use datetime but time is better in this time

    if detection:
        out.write(frame)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3) # drawing an image over frame
    #for (x, y, width, height) in bodies:
    #    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3) # drawing an image over frame

    cv2.imshow("Jack's Camera", frame) # Video frame name and what it´s going to show

    if cv2.waitKey(1) == ord('q'):
        break;


out.release()
# release cpu resources
cap.release()
cv2.destroyAllWindows()
