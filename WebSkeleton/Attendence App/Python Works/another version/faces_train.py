import os
from PIL import Image
import numpy as np
import cv2
import pickle

face_detect=cv2.CascadeClassifier("Cascade\haarcascade_frontalface_alt2.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()

basedirect=os.path.dirname(os.path.abspath(__file__))
imgdirect=os.path.join(basedirect,"images")

ylabel=[]
xtrain=[]
currentid=0
labelid={}

for root,dirs,files in os.walk(imgdirect):
    for file in files:
        if ((file.endswith("png")) or (file.endswith("jpg")) or (file.endswith("jpeg"))):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(" ","-").lower()
            #print(label,path)

            if label in labelid:
                pass
            else:
                labelid[label]=currentid
                currentid=currentid+1
            
            ids=labelid[label]
            print(labelid)

            pilimg=Image.open(path).convert("L")
            size=(550,550)
            finalimg=pilimg.resize(size,Image.ANTIALIAS)
            imgarr=np.array(pilimg,"uint8")
            #print(imgarr)

            faces=face_detect.detectMultiScale(imgarr,scaleFactor=1.5,minNeighbors=5)

            for(x,y,w,h) in faces:
                roi=imgarr[y:y+h,x:x+w]
                xtrain.append(roi)
                ylabel.append(ids)

#print(ylabel)
#print(xtrain)

with open("labels.pickle","wb") as f:
    pickle.dump(labelid,f)

recognizer.train(xtrain,np.array(ylabel))
recognizer.save("Trainer.yml")


