import cv2
import face_recognition as FR

font = cv2.FONT_HERSHEY_SIMPLEX

modiFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\modi.webp')
faceLoc = FR.face_locations(modiFace)[0]
modiFaceEncode = FR.face_encodings(modiFace)[0]

jaiShankarFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\jaiShankar.jpg')
jaiShankarfaceLoc = FR.face_locations(jaiShankarFace)[0]
jaiShankarFaceEncode = FR.face_encodings(jaiShankarFace)[0]

pavanKalyanFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\kalyan.webp')
pavanKalyanFaceLoc = FR.face_locations(pavanKalyanFace)[0]
pavanKalyanFaceEncode = FR.face_encodings(pavanKalyanFace)[0]

kalyaniPriyadarshan = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\known\kalyani.jpg')
kalyaniPriyadarshanLoc = FR.face_locations(kalyaniPriyadarshan)[0]
kalyaniPriyadarshanEncode = FR.face_encodings(kalyaniPriyadarshan)[0]

knownEncodings = [modiFaceEncode, jaiShankarFaceEncode, pavanKalyanFaceEncode, kalyaniPriyadarshanEncode ]
names = ['PM Modi','Minister JaiShenkar','Pavan Kalyan','kalyani Priyadarshan']

unknownFace = FR.load_image_file(r'C:\Users\Admin\Desktop\face_recognition\Photos\unknown\u2.webp')
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace,faceLocations)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
	top,right,bottom,left=faceLocation
	print(faceLocation)
	cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
	name='Unknown Person'
	matches=FR.compare_faces(knownEncodings,unknownEncoding)
	print(matches)

	if True in matches:
		matchIndex=matches.index(True)
		print(matchIndex)
		print(names[matchIndex])
		name=names[matchIndex]
	cv2.putText(unknownFaceBGR,name,(left,top),font,.5,(255,0,0),2)

cv2.imshow('My Faces', unknownFaceBGR)

cv2.waitKey(0)


