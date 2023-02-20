import os
import cv2
import face_recognition as FR
import pickle

print(cv2.__version__)
encodings=[]
names=[]
imageDir=r'C:\Users\Admin\Desktop\face_recognition\Photos\known'

for root,dirs,files in os.walk(imageDir):
	# print(root)
	# print(dirs)
	# print(files)
	for file in files:
		#print(file)
		fullFilePath=os.path.join(root,file)
		print(fullFilePath)
		myPictute=FR.load_image_file(fullFilePath)
		encoding=FR.face_encodings(myPictute)[0]
		name=os.path.splitext(file)[0]
		encodings.append(encoding)
		names.append(name)

with open('train.pk1','wb') as f:
	pickle.dump(names,f)
	pickle.dump(encodings,f)