import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\modi.webp')

cv2.imshow('img',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
