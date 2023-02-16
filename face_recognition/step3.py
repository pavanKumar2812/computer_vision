import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX

modiFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\modi.webp')
faceLoc = FR.face_locations(modiFace)[0]
modifaceEncode = FR.face_encodings(modiFace)[0] #  It return array of arrays 

jaiShankarFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\jaiShankar.jpg')
MinisterfaceLoc = FR.face_locations(jaiShankarFace)[0]
MinisterfaceEncode = FR.face_encodings(jaiShankarFace)[0]

knownEncodings = [modifaceEncode,MinisterfaceEncode]
names=['PM Modi','Minister JaiShankar']

unknownFace = FR.load(r'C:\Users\Admin\Desktop\face_recognition\Photos\unknown\u1.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_BGB2BGR)
faceLocations = FR.face_locations(unknownFace)
unknownEncondings = FR.face_encodings(unknownFace,faceLocations)


top,right,bottom,left = faceLoc
cv2.rectangle(modiFace,(left,top),(right,bottom),(255,0,0),3)
modiFaceBGR=cv2.cvtColor(modiFace,cv2.COLOR_RGB2BGR)
cv2.imshow('without_Convert_color', modiFace)
cv2.imshow('after color convert', modiFaceBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
