import cv2
import numpy as np

img = cv2.resize(cv2.imread('R.jpg'), (500,500))
cv2.imshow('Original Image', img)

blurred = cv2.blur(img, (3,3))
cv2.imshow('Blurred', blurred)

mask = np.zeros(img.shape[:2], dtype='uint8')
cv2.circle(mask, (250,250), 3, 255, -1)
mask = mask / np.sum(mask)

cv2.imshow('circle',mask)

filt = cv2.filter2D(img, -1, mask)
cv2.imshow('Filt', filt)

cv2.waitKey(0)

cv2.pr