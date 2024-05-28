import cv2 
import matplotlib.pyplot as plt
import numpy as np

img = cv2.resize(cv2.imread('Images\lake.jpg'), (500,500))
cv2.imshow('orignal image', img)

# Histograms allow you to visualize the distribution of pixel intensities in an image
# Works for both color and grayscale images

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# Mask
blank = np.zeros(img.shape[:2], dtype='uint8')

Mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv2.imshow('circle', Mask)

maskedGray = cv2.bitwise_and(gray, gray, mask=Mask)
cv2.imshow('mask', maskedGray)

# GrayScale Histogram
gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])
maskedGrayOnGray_hist = cv2.calcHist([gray], [0], maskedGray, [256], [0,256])
maskOnGray_hist = cv2.calcHist([gray], [0], Mask, [256], [0,256])
# Both the mask_hist and circle_hist give the same output, which means that the white circle is the mask
# The histogram may be calculating based on not-zero pixel intensities in the mask, meaning that any mask black pixels will not be considered
diff_hist = maskOnGray_hist - maskedGrayOnGray_hist

plt.figure(figsize=(10,5)) # Initializes a new Matplotlib figure to plot the histograms
plt.subplot(2,2,1)
plt.plot(gray_hist)
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.xlim([0,256])

plt.subplot(2,2,2)
plt.plot(maskedGrayOnGray_hist)
plt.title('maskedGrayOnGray Histogram')

plt.subplot(2,2,3)
plt.plot(maskOnGray_hist)
plt.title('maskOnGray Histogram')

plt.subplot(2,2,4)
plt.plot(diff_hist)
plt.title('Difference between maskedGrayOnGray and maskOnGray')
plt.tight_layout()
plt.show()

# Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], Mask, [256], [0,265])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv2.waitKey(0)

