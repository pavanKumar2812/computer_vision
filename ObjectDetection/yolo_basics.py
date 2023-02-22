from ultralytics import YOLO
import cv2


model = YOLO('../Yolo-weights/yolov8n.pt')
results = model('Images/SchoolBus.jpg', show=True)
cv2.waitKey(0)