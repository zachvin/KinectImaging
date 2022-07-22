# string formatting method new in 3.6
# dictionaries are unordered (ordered in 3.7)

from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2
import time

kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth | PyKinectV2.FrameSourceTypes_Color)

def display_img(window_name: str, img, scale: float) -> None:
  width = int(img.shape[1] * scale)
  height = int(img.shape[0] * scale)

  img_s = cv2.resize(img, (width,height))
  cv2.imshow(window_name, img_s)