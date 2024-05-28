import cv2
import numpy as np

img = cv2.resize(cv2.imread('R.jpg'), (500,500))
cv2.imshow('original image', img)

# Masking allows us to focus on certain parts of an image

blank = np.zeros(img.shape[:2], dtype='uint8')
mask_BW = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# Error will raise if mask size is not the same as the original image
cv2.imshow('mask', mask_BW)

masked = cv2.bitwise_and(img, img, mask=mask_BW)
cv2.imshow('masked image', masked)

cv2.waitKey(0)
