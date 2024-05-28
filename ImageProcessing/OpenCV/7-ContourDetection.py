import cv2
import numpy as np

img = cv2.resize(cv2.imread('R.jpg'), (500,500))
cv2.imshow('org',img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)

canny = cv2.Canny(img, 125, 175)
cv2.imshow('Canny Edges', canny)

# ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
# cv2.imshow('thresh', thresh)
# Binarizes the image ; black if pixel density is below 125 and white(255) if above 125

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_TREE
#      Retrieves all the contours in a hierarchical system
# cv2.RETR_EXTERNAL
#      Retrieves only the external contours, or all the ones on the outside
# cv2.RETR_LIST
#      Retrieves all the contours that are found in the image
# cv2.CHAIN_APPROX_NONE is the approximation method
#      Does nothing, it just returns all of the contours
#      Gets all points in a line 
# cv2.CHAIN_APPROX_SIMPLE
#      Compresses all the retrieved contours into simple ones that make most sense
#      Gets only the end points in a line
# 'contours' is a python list of all the coordinates of the contours that were found in the image
# 'hierarchies' is out of the scope of this course, but essentially it refers to the hierarchical representations of contours
#      For example, if you have a rectangle, inside a square, inside a circle, the hierarchy is a representation to find these contours

cv2.drawContours(blank, contours, -1, (0,0,255), )
cv2.imshow('Contours Drawn', blank)
# It is recommended to use canny first, instead of thresholding, to count the contours

print(len(contours))
cv2.waitKey(0)