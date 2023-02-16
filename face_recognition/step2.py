import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX
modiFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\modi.webp')
faceLoc = FR.face_locations(modiFace)[0]
print(faceLoc)
top,right,bottom,left = faceLoc
cv2.rectangle(modiFace,(left,top),(right,bottom),(255,0,0),3)
modiFaceBGR=cv2.cvtColor(modiFace,cv2.COLOR_RGB2BGR)
cv2.imshow('without_Convert_color', modiFace)
cv2.imshow('after color convert', modiFaceBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

