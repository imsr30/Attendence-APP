import cv2
import numpy as np
import face_recognition

imgtest1=face_recognition.load_image_file("TempImg/Sriram.png")
imgtest1=cv2.cvtColor(imgtest1,cv2.COLOR_BGR2RGB)

facezone=face_recognition.face_locations(imgtest1)[0]
encodeface=face_recognition.face_encodings(imgtest1)[0]
cv2.rectangle(imgtest1,(facezone[3],facezone[0]),(facezone[1],facezone[2]),(0,0,255),2)

cv2.imshow("Jeyadev",imgtest1)

imgtest2=face_recognition.load_image_file("TempImg/Sriram.png")
imgtest2=cv2.cvtColor(imgtest2,cv2.COLOR_BGR2RGB)

facezone1=face_recognition.face_locations(imgtest2)[0]
encodeface1=face_recognition.face_encodings(imgtest2)[0]
cv2.rectangle(imgtest2,(facezone1[3],facezone1[0]),(facezone1[1],facezone1[2]),(0,0,255),2)

cv2.imshow("Sriram",imgtest2)

compimgs=face_recognition.compare_faces([encodeface],encodeface1)
facedis=face_recognition.face_distance([encodeface],encodeface1)
print(compimgs,facedis)

cv2.waitKey(0)
