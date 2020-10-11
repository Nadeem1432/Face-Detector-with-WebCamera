#import modules
import numpy as np
import cv2
import winsound
import os

count = 0 #var for save faces as a jpg file

# here we use haarcascade for detect to face
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#capture camera of PC/Laptop
cap = cv2.VideoCapture(0)

#loop use for everytime detect when camera is on 
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray image
    faces = detector.detectMultiScale(gray, 1.3, 5)
    if len(faces)==1:
        winsound.Beep(2500,900) #soound of beep when face is detected
    else:
        pass
    for (x,y,w,h) in faces:
        face = img[y:y+h, x:x+w] #slice the face from the image
        try:
            os.mkdir('saved')
        except:
            pass
        cv2.imwrite(f'saved/{count}.jpg', face) #save the image
        count+=1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #rectangle

    cv2.imshow('My Face Detecter',img)
    if cv2.waitKey(27) & 0xFF == ord('q'):# press 'ESC' to quit
        break
    
cap.release()
cv2.destroyAllWindows()
