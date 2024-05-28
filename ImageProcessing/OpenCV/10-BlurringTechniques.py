import cv2

img = cv2.resize(cv2.imread('R.jpg'), (500,500))
cv2.imshow('original image',img)

# The first thing that we need to define is a kernel window
#     This is a window drawn over a specific portion of an image
#     The size of the window is called the kernel size
#     Slides to the right then down

# Averaging
average = cv2.blur(img, (3,3))
cv2.imshow('AverageBlur', average)

MoreAverage = cv2.blur(img, (7,7))
cv2.imshow('MoreAverageBlur', MoreAverage)

# Gaussian Blur
# Use to reduce noise while preserving edges and produce a more natural-looking blur
# Each pixel in the kernel contributes differently to the result, with pixels closer to the center having a higher influence.
#     Higher weights are assigned to pixels near the center of the kernel
gauss = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('Guass', gauss)

# Median Blur
# Similar to averaging, except that it finds the median of the surrounding pixel
# Tends to be more effective in reducing noise in an image as compared to averaging, and even gaussian blur
# Use this to remove substantial amount of noise, such as 'salt and pepper' noise
# Not meant for high kernel sizes ; try to keep at 3x3
# Edges are much more pronounced
median = cv2.medianBlur(img, 3)
cv2.imshow('MedianBlur', median)

# Bilateral Filtering
# The most effective, because it retains edges
# The parameter 'sigmaColor': 
#     The standard deviation for intensity similarity
#     Larger values means that pixel intensities with greater difference will influence the blurring calculation more
# The parameter 'spaceSigma': 
#     The standard deviation for spatial closeness
#     Larger values means that pixels futher out from the central pixel will influence the blurring calculation more
bilateral = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow('Bilateral Filtering', bilateral)


cv2.waitKey(0)