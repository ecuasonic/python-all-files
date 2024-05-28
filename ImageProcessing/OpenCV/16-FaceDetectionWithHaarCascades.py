# Face detection is performed using classifiers, which is an algorithm that decides whether a face is present or not
# Classifiers need to be trained on 1000s or 10000s of images with or without faces
# OpenCV already comes with many pre-trained classifiers

import cv2

img = cv2.resize(cv2.imread('einstein-low-contrast.jpg'), (500,600))
cv2.imshow('Three Channel Gray Photo', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Single Channel Gray Photo', gray)

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(len(faces_rect)) # Prints the number of faces detected

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv2.imshow('Detected Faces', img)

cv2.waitKey(0)