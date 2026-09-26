import cv2
import numpy as np


def get_limits(color):
    c=np.uint8([[color]])
    hsvC= cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    hue = int(hsvC[0][0][0])
    lowerLimit= max(hue - 10, 0),100,100
    upperLimit= min(hue + 10, 179),255,255

    lowerLimit=np.array(lowerLimit,dtype=np.uint8)
    upperLimit=np.array(upperLimit,dtype=np.uint8)

    return lowerLimit,upperLimit
