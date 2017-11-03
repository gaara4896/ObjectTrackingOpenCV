import cv2
import HumanDetection

video = cv2.VideoCapture("../Video/CCTV.mp4")
#HumanDetection.faceInit()
#HumanDetection.eyeInit()
#HumanDetection.fullBodyInit()
#HumanDetection.upperBodyInit()
HumanDetection.lowerBodyInit()

while video.isOpened():
    timer = cv2.getTickCount()
    ok, frame = video.read()
    if not ok:
        break
    
    frame = HumanDetection.update(frame)
    
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    
    cv2.imshow("feed", frame)
    
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break

cv2.waitKey()
cv2.destroyAllWindows()