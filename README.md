# Object Tracking OpenCV

### Tools

```
Python Interpreter (Python 3 recommended)
OpenCV
```

***For Arch***

`$sudo pacman -S opencv hdf5`

### Usage

```
Usage: python MotionDetection.py [<ARGS>...] [-m <Number of Tracker>] [-d <Number of Compare Frames>] [-v <Path>] 

<ARGS>
  -d  Detect Differences Between Frames
  -f  Enable Face Detection
  -e  Enable Eye Detection
  -b  Enable Full Body Detection
  -u  Enable Upper Body Detection
  -l  Enable Lower Body Detection
  -t  Enable Motion Tracking
  -m  Enable Multiple Motion Tracking
  -v  Play from videos    
  -w  Play from webcam  
```

##### Example

`python MotionDetection.py -ftw`

`python MotionDetection.py -d 5 -v /Video/CCTV.mp4`

`python MotionDetection.py -febw`