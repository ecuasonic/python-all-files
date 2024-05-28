import cv2
import numpy as np

# How to split and merge color channels in openCV
# All the BGR or RGB images are three color channels merged together. 
# OpenCV allows you to split an image into its respective color channels

img = cv2.resize(cv2.imread('images\lake.jpg'), (500,500))
cv2.imshow('original', img)

# Spliting the color channels into single channels (grayscale)
b,g,r = cv2.split(img)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
# The color channels are depicted and displayed as grayscale images that show the distribution of pixel distribution

# Merging the three single channels into three channels
merged = cv2.merge([b,g,r])
cv2.imshow('merged image', merged)

# Merging single channel with blank channels
blank = np.zeros(img.shape[:2], dtype='uint8')

Blue = cv2.merge([b, blank, blank])
cv2.imshow('Blue color only', Blue)

Green = cv2.merge([blank, g, blank])
cv2.imshow('Green color only', Green)

Red = cv2.merge([blank, blank, r])
cv2.imshow('Red color only', Red)

cv2.waitKey(0)