import cv2

img = cv2.resize(cv2.imread('R.jpg'), (500,500))
cv2.imshow('Original Photo', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Simple Thresholding
# threshold -> 150
# thresh -> image with threshold applied
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
# Computes the optimal thresholding for a neighborhood of pixels using mean or gaussian
cv2.imshow('Adaptive Thresholding', adaptive_thresh)

cv2.waitKey(0)