import cv2
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle', circle)

# bitwise AND
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow('bitwise NOT', bitwise_not)

cv2.waitKey(0)