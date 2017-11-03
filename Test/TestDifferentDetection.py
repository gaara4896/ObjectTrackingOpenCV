import sys
sys.path.insert(0, '../utils')
import cv2
import DifferentTracking

video = cv2.VideoCapture("../Video/CCTV.mp4")

DifferentTracking.init(10)

while video.isOpened():
    timer = cv2.getTickCount()
    ok, frame = video.read()
    if not ok:
        break
    
    frame = DifferentTracking.update(frame)
    
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    
    cv2.imshow("feed", frame)
    
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

cv2.waitKey()
cv2.destroyAllWindows()