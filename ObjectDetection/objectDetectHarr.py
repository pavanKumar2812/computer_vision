import cv2

path = 'haarCascade/cascade.xml' # Path of the cascade
objectName = 'NodeMCU'
frameWidth = 640
frameHeight = 480
color=(255,0,255)


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

def empty(a):
    pass

# Create Trackbar
cv2.namedWindow("Result")
cv2.resizeWindow('Result',frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig",'Result',8,20,empty)
cv2.createTrackbar('Min Area','Result',0,100000,empty)
cv2.createTrackbar('Brightness','Result',100,255,empty)

# Load the classifiers downloaded
cascade = cv2.CascadeClassifier(path)

while True:
    # Set camera brightness from Trackbar value
    cameraBrightness = cv2.getTrackbarPos('Brightness','Result')
    cam.set(10,cameraBrightness)
    # Get camera image and convert into Grayscale
    ignore, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Detect the object using cascade
    scaleVal = 1 + (cv2.getTrackbarPos('Scale','Result') / 1000)
    neig = cv2.getTrackbarPos('Neig','Result')
    objects = cascade.detectMultiScale(gray,scaleVal,neig)
    
    # Display the detected objects
    for (x,y,w,h) in objects:
        area = w * h
        minArea = cv2.getTrackbarPos('Min Area','Result')
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color = img[y:y+h,x:x+w]

    cv2.imshow('Result',img)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()