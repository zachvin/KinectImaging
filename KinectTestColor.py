from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

while True:
  
  if kinect.has_new_color_frame():
    frame = kinect.get_last_color_frame()
    frame = frame.astype(np.uint8)
    img = np.reshape(frame,(1080,1920,-1))
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    cv2.imshow('Color frame', img)

  k = cv2.waitKey(1)
  if k == 27:
    break