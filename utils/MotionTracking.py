import cv2

trackers = []
    
def addTracker(frame, roi):
    global trackers
    [major_ver, minor_ver, subminor_ver] = cv2.__version__.split(".")
    if int(major_ver) < 3 and int(minor_ver) < 1:
        tracker = cv2.TrackerMIL_create()
    else:
        tracker = cv2.TrackerKCF_create()
    tracker.init(frame, roi)
    trackers.append(tracker)
        
def update(frame):
    global trackers
    successFlag = False
    
    for tracker in trackers:
        ok, trackBox = tracker.update(frame)
        if ok:
            p1 = (int(trackBox[0]), int(trackBox[1]))
            p2 = (int(trackBox[0] + trackBox[2]), int(trackBox[1] + trackBox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            successFlag = True
        
    return successFlag, frame