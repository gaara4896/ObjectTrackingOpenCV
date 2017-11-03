import sys
sys.path.insert(0, 'utils')
import HumanDetection
import DifferentTracking
import MotionTracking
import cv2

trackNum = 0
playMode = None
Output_To_File = False
outputName = None

def printUsage():
    print("Usage: python MotionDetection.py [<ARGS>...] [-m <Number of Tracker>] [-d <Number of Compare Frames>] [-v <Path>] [-o <Name>] \n")
    print("<ARGS>")
    print("%2s%-4s%-20s" % ("", "-d", "Detect Differences Between Frames"))
    print("%2s%-4s%-20s" % ("", "-f", "Enable Face Detection"))
    print("%2s%-4s%-20s" % ("", "-e", "Enable Eye Detection"))
    print("%2s%-4s%-20s" % ("", "-b", "Enable Full Body Detection"))
    print("%2s%-4s%-20s" % ("", "-u", "Enable Upper Body Detection"))
    print("%2s%-4s%-20s" % ("", "-l", "Enable Lower Body Detection"))
    print("%2s%-4s%-20s" % ("", "-t", "Enable Motion Tracking"))
    print("%2s%-4s%-20s" % ("", "-m", "Enable Multiple Motion Tracking"))
    print("%2s%-4s%-20s" % ("", "-v", "Play from videos"))
    print("%2s%-4s%-20s" % ("", "-w", "Play from webcam"))
    print("%2s%-4s%-20s" % ("", "-o", "Output to a video"))
    
def init(arg):
    global trackNum, playMode
    if arg == "f":
        HumanDetection.faceInit()
        return True
    elif arg == "e":
        HumanDetection.eyeInit()
        return True
    elif arg == "b":
        HumanDetection.fullBodyInit()
        return True
    elif arg == "u":
        HumanDetection.upperBodyInit()
        return True
    elif arg == "l":
        HumanDetection.lowerBodyInit()
        return True
    elif arg == "t":
        trackNum = 1
        return True
    elif arg == "w":
        playMode = 0
        return True
    else:
        return False

if int(sys.version[0]) < 3:
    print("Please use Python 3")
    sys.exit()
    
if len(sys.argv) == 1:
    printUsage()
    sys.exit()

for x in range(1, len(sys.argv)):
    if sys.argv[x][0] == "-" and len(sys.argv[x]) > 2:
        arg = sys.argv[x].split("-")[1]
        for y in arg:
            if not init(y):
                print("Argument %s in %s invalid" % (y, sys.argv[x]))
                sys.exit()      
    elif sys.argv[x] == "-d":
        DifferentTracking.init(int(sys.argv[x+1]))
    elif sys.argv[x] == "-m":
        trackNum = int(sys.argv[x+1])
    elif sys.argv[x] == "-v":
        playMode = sys.argv[x+1]
    elif sys.argv[x] == "-o":
        Output_To_File = True
        outputName = sys.argv[x+1]
    elif sys.argv[x-1] == "-d" or sys.argv[x-1] == "-m" or sys.argv[x-1] == "-v" or sys.argv[x-1] == "-o":
        continue
    elif sys.argv[x][0] == "-":
        arg = sys.argv[x].split("-")[1]
        if not init(arg):
            print("Argument %s invalid" % (arg))
            sys.exit()  
    else:
        print("Argument %s invalid" % (sys.argv[x]))
        sys.exit()

video = cv2.VideoCapture(playMode)

if not video.isOpened():
    print("Could not open video")
    sys.exit()
    
ok, frame = video.read()

for x in range(0, trackNum):
    MotionTracking.addTracker(frame, cv2.selectROI(frame, False))

if Output_To_File:
    output = cv2.VideoWriter(outputName, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                             video.get(cv2.CAP_PROP_FPS), (int(video.get(3)), int(video.get(4))))
    
while True:
    ok, frame = video.read()
    if not ok:
        break
    timer = cv2.getTickCount()
    
    frame = MotionTracking.update(frame)
    frame = HumanDetection.update(frame)
    frame = DifferentTracking.update(frame)
        
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)

    if Output_To_File:
        output.write(frame)
    cv2.imshow("Tracking", frame)
 
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break
if Output_To_File:
    output.release()

video.release()
cv2.waitKey()
cv2.destroyAllWindows()