import cv2
import numpy as np

img = cv2.imread('R.jpg')

# Translation
def translate(img, x, y):
    # The translation portion (x and y) are with respect to the (0,0) point of the image
    M = [[1,0,x],
         [0,1,y]]
    transMat = np.float32(M)
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)

# Resizing
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)

# Flipping
flip = cv2.flip(img, 0)
# 0 --> across the x-axis
# 1 --> across the y-axis
# -1 --> across both

# Cropping
cropped = img[200:600, 300:1000]
cv2.imshow('crop', cropped)

cv2.waitKey(0)