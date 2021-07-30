import numpy as np
import cv2
import pickle

face_detect=cv2.CascadeClassifier("Cascade\haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

labels={}
with open("labels.pickle","rb") as f:
    oglabels=pickle.load(f)
    labels={v:k for k,v in oglabels.items()}

cap= cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_detect.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)
    for(x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_grey=grey[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        ids,conf=recognizer.predict(roi_grey)
        if((conf>=45) and (conf<=100)):
            print(ids)
            print(labels[ids])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[ids]
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            
        img_item="my_image.png"
        cv2.imwrite(img_item,roi_color)

        color=(0,0,255) #BGR
        stroke=2
        xcord=x+w
        ycord=y+h
        cv2.rectangle(frame,(x,y),(xcord,ycord),color,stroke)

    cv2.imshow("frame",frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()