import cv2
import numpy as np
import matplotlib.pyplot as plt

# Question 4
img = cv2.imread('magnified-pollen-dark.tif', cv2.IMREAD_GRAYSCALE) # has only one channel instead of three
img_eq = cv2.equalizeHist(img)

plt.subplot(221)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title('Original Image')
plt.subplot(222)
plt.imshow(img_eq, cmap='gray', vmin=0, vmax=255)
plt.title('Histogram Equalized Image')

hist = cv2.calcHist([img], [0], None, [256], [0,256])
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0,256])

plt.subplot(223)
plt.plot(hist)
plt.title('Original Image')
plt.subplot(224)
plt.plot(hist_eq)
plt.title('Histogram Equalized Image')
plt.tight_layout()
plt.show()

# Question 5
img2 = cv2.imread('hidden-symbols.tif', cv2.IMREAD_GRAYSCALE)
img2_adapt = cv2.createCLAHE().apply(img2)
img2_eq = cv2.equalizeHist(img2)

plt.figure(figsize=(10,5))
plt.subplot(221)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title('Original Image')
plt.subplot(222)
plt.imshow(img2_adapt, cmap='gray', vmin=0, vmax=255)
plt.title('Adaptive Histogram Equalized Image')
plt.subplot(223)
plt.imshow(img2_eq, cmap='gray', vmin=0, vmax=255)
plt.title('Histogram Equalized')
plt.tight_layout()
plt.show()