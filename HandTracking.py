from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)

while True:
  if kinect.has_new_depth_frame():

    # get image
    frame = kinect.get_last_depth_frame()

    # display 

    cv2.imshow('depth',frame)