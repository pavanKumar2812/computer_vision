# convenient way for choosing right color mask to detect needed object

# Reading Image ==> Converting to HSV ==> Getting Mask

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

image_BGR = cv2.imread('a.png')

image_BGR = cv2.resize(image_BGR,(600,426))

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original Image', image_BGR)

# converting original Image into HSV ( Hue, Saturation, value) color space is a model
image_HSV = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2HSV)

cv2.namedWindow('HSV Image',cv2.WINDOW_NORMAL)
cv2.imshow('HSV Image', image_HSV)

# while True:
#     if cv2.waitKey(0):
#         break

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

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()

print(f'min_blue, min_green, min_red = {min_blue} {min_green} {min_red}' )
print(f'max_blue, max_green, max_red = {max_blue} {max_green} {max_red}' )