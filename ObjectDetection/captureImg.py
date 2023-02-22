import cv2
import os
import time


mypath = '../custom_haarCascade/p'
cameraBrightness = 190
moduleVal = 10 # saving every 10th frame to avoid repetition
minBlur = 500 # smaller value means more blurriness present
grayImage = False # Image saved colored or gray
saveData = True # save data flag
showImage = True # Image display flag
imgWidth = 180
imgHeight = 120

global countFolder
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cam.set(10,cameraBrightness)

count = 0 
countSave = 0

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(mypath + str(countFolder)):
        countFolder = countFolder + 1
    os.makedirs(mypath + str(countFolder))

if saveData:
    saveDataFunc()

while True: 

    ignore, img = cam.read()
    img = cv2.resize(img,(imgWidth,imgHeight))
    if grayImage: img = cv2.cvtcolor(img,cv2.COLOR_BGR2Gray)
    if saveData:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % moduleVal == 0 and blur > minBlur:
            nowTime = time.time()
            cv2.imwrite(mypath + str(countFolder) + "/" + str(countSave) + " " + str(int(blur)) + " " + str(nowTime) + '.png', img)
            countSave += 1
        count += 1

    if showImage:
        cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cam.release()
