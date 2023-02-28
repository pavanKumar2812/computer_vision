import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit = np.array([34,73,232])
    upperLimit = np.array([179,255,255])
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    # cv2.imshow('mask',mask)
    _,mask1 = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    # cv2.imshow('mask1',mask1)
    contours,_ = cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print(f"Number of contours found = {len(contours)}")
    cv2.drawContours(frame,contours,-1,(255,0,0),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()