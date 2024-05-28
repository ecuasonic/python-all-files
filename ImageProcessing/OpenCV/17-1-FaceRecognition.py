import os
import cv2
import numpy as np

p = []
# r'string' is know as a 'raw string,' or 'raw string literal'
# Its a way to define strings that treat backslashes ('\') as literal characters and not as escape characters
# This is particularly useful when working with file paths, regular expressions, or any string that might contain backslashes
for i in os.listdir(r'Images'):
    p.append(i)

DIR = r'Images'

haar_cascade = cv2.CascadeClassifier('haar_face.xml')

features=[]
labels = []


# This function collects the face from each picture, then puts it in the features list
# Then the corresponding index will be recorded in labels
# The features and labels lists are like a dictionary pair 
def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done --------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

faces_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
faces_recognizer.train(features, labels)

faces_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
