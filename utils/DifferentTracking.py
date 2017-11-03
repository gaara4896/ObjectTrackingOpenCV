import cv2
import queue

previousFrames = queue.Queue()

Different_Scan = False
Frames_Number = 0

def init(frameNum):
    global Different_Scan, Frames_Number
    Different_Scan = True
    Frames_Number = frameNum

def update(frame):
    global previousFrames, Different_Scan, Frames_Number
    
    if not Different_Scan:
        return frame
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    previousFrames.put(gray)
    
    if previousFrames.qsize() < Frames_Number:
        return frame
    
    previousFrame = previousFrames.get()
    
    frameDelta = cv2.absdiff(previousFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    
    thresh = cv2.dilate(thresh, None, iterations=2)
    _, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue
        
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    return frame