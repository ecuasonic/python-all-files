import cv2
import matplotlib.pyplot as plt

# Color spaces are systems of representing an array of pixel colors
#     BGR, RGB, GrayScale, HSV (Hue, Saturation, Value), LAB (CIELAB) (Lightness, a (green to read), and b (blue to yellow)),...

img = cv2.resize(cv2.imread('R.jpg'), (500,500))
cv2.imshow('Lake', img)

# BGR to RBG
# plt.imshow(img)
# plt.title('original picture in BGR')
# plt.show()
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb)
# plt.imshow(rgb)
# plt.title('original picture in RGB')
# plt.show()

# BGR to GrayScale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

# BGR to L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('lab', lab)

# GrayScale to BGR 
bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imshow('bgr', bgr) # is now three-channel color, but retains black-and-white colors of grayscale

cv2.waitKey(0)