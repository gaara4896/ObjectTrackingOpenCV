import cv2
face_cascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("resources/haarcascade_eye.xml")
fullbody_cascade = cv2.CascadeClassifier("resources/haarcascade_fullbody.xml")
upperbody_cascade = cv2.CascadeClassifier("resources/haarcascade_upperbody.xml")
lowerbody_cascade = cv2.CascadeClassifier("resources/haarcascade_lowerbody.xml")

Face_Scan = False
Eye_Scan = False
Full_Body_Scan = False
Upper_Body_Scan = False
Lower_Body_Scan = False

def faceInit():
    global Face_Scan
    Face_Scan = True

def eyeInit():
    global Eye_Scan
    Eye_Scan = True
    
def fullBodyInit():
    global Full_Body_Scan
    Full_Body_Scan = True
    
def upperBodyInit():
    global Upper_Body_Scan
    Upper_Body_Scan = True
    
def lowerBodyInit():
    global Lower_Body_Scan
    Lower_Body_Scan = True
    
def draw(frame, detection):
    for x, y, w, h in detection:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    return frame

def update(frame):
    global Face_Scan, Eye_Scan, Full_Body_Scan, Upper_Body_Scan, Lower_Body_Scan
    if not Face_Scan and not Eye_Scan and not Full_Body_Scan and not Upper_Body_Scan and not Lower_Body_Scan:
        return frame
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if Face_Scan:
        frame = draw(frame, face_cascade.detectMultiScale(gray, 1.3, 5))
    if Eye_Scan:
        frame = draw(frame, eye_cascade.detectMultiScale(gray))
    if Full_Body_Scan:
        frame = draw(frame, fullbody_cascade.detectMultiScale(gray))
    if Upper_Body_Scan:
        frame = draw(frame, upperbody_cascade.detectMultiScale(gray))
    if Lower_Body_Scan:
        frame = draw(frame, lowerbody_cascade.detectMultiScale(gray))
    
    return frame    