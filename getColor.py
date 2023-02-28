import cv2
import numpy as np

def get_limits(color):

    col = np.uint8([[color]]) # here insert the bgr value which we want to convert to HSV

    hsvC = cv2.cvtColor(col,cv2.COLOR_BGR2HSV)

    lowestLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowestLimit = np.array(lowestLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowestLimit , upperLimit

print(get_limits([0,255,0]))
