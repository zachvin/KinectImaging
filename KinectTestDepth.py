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


while True:

  if kinect.has_new_color_frame():
  # if False:

    # get and reshape frame
    frame_c = kinect.get_last_color_frame()
    frame_c = np.reshape(frame_c, (1080,1920,4))

    width = frame_c.shape[1]
    height = frame_c.shape[0]
    # print(width,height)

    center_x = width // 2
    center_y = height // 2

    # cv2.circle(frame_c,(center_x,center_y),20,color=(120,32,203),thickness=3)

    display_img('Color', frame_c, .5)

  if kinect.has_new_depth_frame():
  # if False:
    # get kinect frame
    frame_d = kinect.get_last_depth_frame()
    frame_d = np.reshape(frame_d, (424,512))
    frame_d = frame_d.astype(np.uint8)

    # depth_data = frame.astype(np.uint16)
    # img = frame.astype(np.uint8)
    # img = np.reshape(frame, (424,512))
    # depth_data = np.reshape(depth_data, (424,512))
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        
    display_img('Depth',frame_d,.7)

  k = cv2.waitKey(1)
  if k == 27:
    break

  time.sleep(.5)

kinect.close()
cv2.destroyAllWindows()