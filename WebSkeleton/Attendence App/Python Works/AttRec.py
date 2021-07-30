import cv2
import numpy as np
import face_recognition
import os
import time
from datetime import datetime

path="TempImg"
imgs=[]
imgname=[]
imgdata=os.listdir(path)
for cl in imgdata:
    curimg=cv2.imread(f'{path}/{cl}')
    imgs.append(curimg)
    imgname.append(os.path.splitext(cl)[0])
now1=datetime.now()
process_start_time=now1.strftime("%H:%M:%S")
print(imgname,process_start_time)

def attendencerec(name):
    with open("attendencedata.csv",'r+') as f:
        data=f.readlines()
        namedata=[]
        for dat in data:
            getdata=dat.split(",")
            namedata.append(getdata[0])
        if name not in namedata:
            now3=datetime.now()
            timedate=now3.strftime("%d-%m-%Y %H:%M:%S")
            Attendence_Record_Date,Attendence_Record_Time = timedate.split(" ")
            f.writelines(f'\n{name},{Attendence_Record_Date},{Attendence_Record_Time}')


def findencodings(imgs):
    encodelist=[]
    for img in imgs:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeface=face_recognition.face_encodings(img)[0]
        encodelist.append(encodeface)
    return encodelist

knownencodedata=findencodings(imgs)
print("Encoding Process Done")

cap=cv2.VideoCapture(0)
now2=datetime.now()
camera_start_time=now2.strftime("%H:%M:%S")
print("Camera Starts Now",camera_start_time)
TIMER=int(5)

while True:
    ret,img=cap.read()
    imgsize=cv2.resize(img,(0,0),None,0.25,0.25)
    imgsize=cv2.cvtColor(imgsize,cv2.COLOR_BGR2RGB)
    faceCurFrame=face_recognition.face_locations(imgsize)
    encodeCurFrame=face_recognition.face_encodings(imgsize,faceCurFrame)
    k = cv2.waitKey(125)
    if k == ord('q'):
        prev = time.time()
        while TIMER >= 0:
            ret, img = cap.read()
            print(TIMER)
            if(TIMER==0):
                quit()
            cv2.waitKey(125)
            cur = time.time()
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1


    for encode,facepos in zip(encodeCurFrame,faceCurFrame):
        matches=face_recognition.compare_faces(knownencodedata,encode)
        facedis=face_recognition.face_distance(knownencodedata,encode)
        #print(facedis)
        matchindex=np.argmin(facedis)

        if matches[matchindex]:
            name=imgname[matchindex].upper()
            #print(name)
            y1,x2,y2,x1=facepos
            y1,x2,y2,x1=(y1*4),(x2*4),(y2*4),(x1*4)
            cv2.rectangle(img,(x1,y1),(x2,y2),(160,160,85),2)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
            attendencerec(name)



    cv2.imshow("WebCam",img)
    cv2.waitKey(20)
