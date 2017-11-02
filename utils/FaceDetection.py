import cv2

face_cascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

def update(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces