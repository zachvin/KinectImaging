from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)

while True:

  if kinect.has_new_depth_frame():
    frame = kinect.get_last_depth_frame()
    depth_data = frame.astype(np.uint16)
    img = frame.astype(np.uint8)
    img = np.reshape(frame, (424,512))
    depth_data = np.reshape(depth_data, (424,512))
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    x = int(img.shape[0]/2)
    y = int(img.shape[1]/2)

    dist = depth_data[y,x]
    print(dist)
    
    cv2.circle(img,center=(y,x),radius=10,color=(0,255,0),thickness=-1)
    cv2.putText(img,text=str(dist),org=(10,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,255,255),thickness=2)
    
    cv2.imshow('Depth',img)  

  k = cv2.waitKey(1)
  if k == 27:
    break