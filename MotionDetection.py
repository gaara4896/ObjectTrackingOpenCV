import sys
sys.path.insert(0, 'utils')
import FaceDetection
import DifferentTracking
import MotionTracking
import cv2

#video = cv2.VideoCapture("Video/CarGame.avi")
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Could not open video")
    sys.exit()
    
ok, frame = video.read()

while cv2.waitKey() != 27:
    MotionTracking.addTracker(frame, cv2.selectROI(frame, False))

while True:
    ok, frame = video.read()
    if not ok:
        break
    
    motion, frame = MotionTracking.update(frame)
    face, frame = FaceDetection.update(frame)
    
    if not motion and not face:    
        frame = DifferentTracking.update(frame)
    
    cv2.imshow("Tracking", frame)
 
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

cv2.waitKey()
cv2.destroyAllWindows()