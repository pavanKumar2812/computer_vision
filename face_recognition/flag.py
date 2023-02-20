import cv2
print(cv2.__version__)
import numpy as np
while True:
    frame=np.zeros([255,255,3],dtype=np.uint8)
    frame[:85,:]=(51, 153, 255)
    frame[85:170,:]=255
    frame[170:255,:] = (0,128,0)
    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
