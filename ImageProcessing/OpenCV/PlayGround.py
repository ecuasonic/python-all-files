import cv2

haar_cascade = cv2.CascadeClassifier('haar_face.xml')
capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces_rect:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
    cv2.imshow('video', frame)
    if cv2.waitKey(20) & 0xFF == ord(' '):
        break
