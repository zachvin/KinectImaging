from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2
import time

# kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

# while True:
#   if kinect.has_new_color_frame():

#     frame = kinect.get_last_color_frame()

#     print(np.shape(frame))

#     time.sleep(0.5)

cap = cv2.VideoCapture(0)

while True:

  updated,frame = cap.read()

  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

  cols = 9
  rows = 6

  # findCirclesGrid takes (num_cols,num_rows)
  ret,corners = cv2.findCirclesGrid(gray,(cols,rows),None)

  # once the grid is found, press a button to start tracking and make everything around it dark

  # if it's not a dark point, then make it white
  ret1,thresh = cv2.threshold(gray,100,255,cv2.THRESH_TOZERO)

  cv2.drawChessboardCorners(thresh,(cols,rows),corners,ret)

  cv2.imshow('thresh',thresh)

  k = cv2.waitKey(1)
  if k == 27:
    break

cv2.destroyAllWindows()