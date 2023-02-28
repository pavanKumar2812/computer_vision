import cv2


# for track bars defining empty function
def do_nothing(x):
    pass

cv2.namedWindow('Track Bars', cv2.WINDOW_NORMAL)

# For minimum range
cv2.createTrackbar('min_blue','Track Bars',0,255,do_nothing)
cv2.createTrackbar('min_green','Track Bars',0,255, do_nothing)
cv2.createTrackbar('min_red','Track Bars',0,255, do_nothing)

# For maximum range
cv2.createTrackbar('max_blue','Track Bars',0,255,do_nothing)
cv2.createTrackbar('max_green','Track Bars',0,255,do_nothing)
cv2.createTrackbar('max_red','Track Bars',0,255,do_nothing)

load_img_BGR = cv2.imread(r'C:\Users\Admin\Desktop\Team1\step1\b.jpeg')

cv2.namedWindow('Original Image',cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', load_img_BGR)

image_HSV = cv2.cvtColor(load_img_BGR, cv2.COLOR_BGR2HSV)

cv2.namedWindow('HSV Image',cv2.WINDOW_NORMAL)
cv2.imshow('HSV Image', image_HSV)

while True:
    # min value storing the value in variables from the track bar 
    min_blue = cv2.getTrackbarPos('min_blue','Track Bars')
    min_green = cv2.getTrackbarPos('min_green','Track Bars')
    min_red = cv2.getTrackbarPos('min_red','Track Bars')

    # max value
    max_blue = cv2.getTrackbarPos('max_blue','Track Bars')
    max_green = cv2.getTrackbarPos('max_green','Track Bars')
    max_red = cv2.getTrackbarPos('max_red','Track Bars')

    # Implementing mask with chosen color from track bars to HSV Image
    # Defining lower bounds and upper bounds from thresholdings
    mask = cv2.inRange(image_HSV, (min_blue,min_green,min_red),(max_blue,max_green,max_red))

    # showing binary image with implemented mask
    cv2.namedWindow('Binary Image with Mask',cv2.WINDOW_NORMAL)
    cv2.imshow('Binary Image with Mask',mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # Finding the biggest Contour by sorting from biggest to smallest
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    if contours:
        (x_min, y_min, box_width, box_height) = cv2.boundingRect(contours[0])

        cv2.rectangle(load_img_BGR, (x_min - 15, y_min - 15),(x_min + box_width + 15, y_min + box_height + 15),(0, 255, 0), 3)

        label = 'Detected Object'

        cv2.putText(load_img_BGR, label, (x_min - 5, y_min - 25),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
   
    cv2.namedWindow('Detected Object',cv2.WINDOW_NORMAL)
    cv2.imshow('Detected Object',load_img_BGR)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break


cv2.destroyAllWindows()

print(f'min_blue, min_green, min_red = {min_blue} {min_green} {min_red}' )
print(f'max_blue, max_green, max_red = {max_blue} {max_green} {max_red}' )