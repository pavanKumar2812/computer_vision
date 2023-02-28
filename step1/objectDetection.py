import cv2

# Defining lower bounds and upper bounds of founded mask

min_blue, min_green, min_red = 16,62,61  #21, 222, 70
max_blue, max_green, max_red = 101,255,255 #176, 255, 255

camera = cv2.VideoCapture(0)

while True:
    # capture fram by frame from camera
    ignore, frame_BGR = camera.read()

    frame_HSV = cv2.cvtColor(frame_BGR, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame_HSV, (min_blue,min_green,min_red),(max_blue,max_green,max_red))

    cv2.namedWindow('Binary frame with Mask', cv2.WINDOW_NORMAL)
    cv2.imshow('Binary frame with mask', mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # Finding the biggest Contour by sorting from biggest to smallest
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    if contours:
        (x_min, y_min, box_width, box_height) = cv2.boundingRect(contours[0])

        cv2.rectangle(frame_BGR, (x_min - 15, y_min - 15),(x_min + box_width + 15, y_min + box_height + 15),(0, 255, 0), 3)

        label = 'Detected Object'

        cv2.putText(frame_BGR, label, (x_min - 5, y_min - 25),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
   
    cv2.namedWindow('Detected Object',cv2.WINDOW_NORMAL)
    cv2.imshow('Detected Object',frame_BGR)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()