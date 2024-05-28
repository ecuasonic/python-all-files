import cv2
import numpy as np

img = cv2.imread('R.jpg')
cv2.imshow('Lake', img)

# img.shape = blank.shape = (height, width, colorChannels)
blank = np.zeros(img.shape, dtype='uint8')

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0,0,255

# 2. Draw a Rectangle (width, height)
cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1) # or you can use 'cv2.FILLED' instead of -1

# 3. Draw a Circle (width, height)
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)

# 4. Draw a line (width, height)
cv2.line(blank, (0,0), (blank.shape[1], blank.shape[0]), (255,0,0), thickness=30)

# 5. Write Text (width, height)
cv2.putText(blank, 'Hello', (blank.shape[1]//2, blank.shape[0]//2), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv2.imshow('Blank', blank)


cv2.waitKey(0)