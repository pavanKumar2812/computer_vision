from ultralytics import YOLO
import cv2
import cvzone
import math

width=1280 #640
height=360 #720

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

model= YOLO('../Yolo-weights/yolov8n.pt')

while True:
    ignore, img = cam.read()

    if img.shape[0] > 0 and img.shape[1] > 0:
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1,y1,x2,y2 = box.xyxy[0]
                x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                # print(x1,y1,x2,y2)
                cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)

                # w,h = x2-x1,y2-y1
                # cvzone.cornerRect(img,(x1,y1,w,h))

                conf = math.ceil((box.conf[0]*100))/100
                print(conf)
                # cvzone.putTextRect(img,f'{conf}',(x1,y1-20))
                cvzone.putTextRect(img,f'{conf}',(max(0,x1), max(0, y1 - 20)))
        cv2.imshow('Image',img)
        cv2.moveWindow('Image',0,0)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        print('Invalid image dimensions')
cam.release()