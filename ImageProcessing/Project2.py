import cv2
import numpy as np
import matplotlib.pyplot as plt

# Question 2

# MedianBlur, which is analogous to medfilt2 in MatLab, doesn't work well
#     The salt and pepper noise appears smudged
#     The function works by calculating the median within the 3x3 neighborhood and sets it to the central pixel

# ordfilt2(A,i,ones(3,3)) takes the ith lowest intensity value within the 3x3 neighborhood and sets it to the central pixel
#     i = 1 --> minfilte
#     i = 5 --> medfilt2
#     i = 9 --> maxfilter

# Within a 3x3 neighborhood, maxfilter sets the center pixel to the maximum intensity value in the neighborhood. 
def maxfilter(f):
    m,n = 1,1
    fp = cv2.copyMakeBorder(f, m, m, n, n, cv2.BORDER_REPLICATE)
    g = np.zeros_like(f)
    for i in range(m, f.shape[0] + m):
        for j in range(n, f.shape[1] + n):
            neighborhood = fp[i-m:i+m+1, j-n:j+n+1]
            g[i-m, j-n] = np.max(neighborhood)
    return g

# Within a 3x3 neighborhood, minfilter sets the center pixel to the minimum intensity value in the neighborhood. 
def minfilter(f):
    m,n = 1,1
    fp = cv2.copyMakeBorder(f, m, m, n, n, cv2.BORDER_REPLICATE)
    g = np.zeros_like(f)
    for i in range(m, f.shape[0] + m):
        for j in range(n, f.shape[1] + n):
            neighborhood = fp[i-m:i+m+1, j-n:j+n+1]
            g[i-m, j-n] = np.min(neighborhood)
    return g

img = cv2.imread('images\dentalXray-pepper-noise.tif', cv2.IMREAD_GRAYSCALE)
plt.subplot(3,2,1)
plt.imshow(img, cmap = 'gray')
plt.title('Img')

plt.subplot(3,2,2)
plt.imshow(img2, cmap = 'gray')
plt.title('Img2')

plt.subplot(3,2,3)
plt.imshow(maxfilter(img), cmap = 'gray')
plt.title('Max(Img)')

plt.subplot(3,2,4)
plt.imshow(minfilter(img2), cmap = 'gray')
plt.title('Min(Img2)')

plt.subplot(3,2,5)
plt.imshow(cv2.equalizeHist(maxfilter(img)), cmap = 'gray')
plt.title('Hist(Max(Img))')

plt.subplot(3,2,6)
plt.imshow(cv2.equalizeHist(minfilter(img2)), cmap = 'gray')
plt.title('Hist(Min(Img2))')

plt.tight_layout()
plt.show()


# Quesiton 3

# For part B, I did not observe any negative valued pixels, which might have been due to the fact
#     that all the bits are taken up by pixel intensity values, which leave no space for postive or negative sign
# For part E, there were negative intensity valued pixels present. 
# For part G, from the results of (b) and (e), the pixel values are not the same
#     The pixel values in (b) are integers, while they are floats in (e)
#     I don't really see a difference between (c) and (f), but (f) has more resolution in terms of intensity values due to the floats
#     so I would go with (f)

image = cv2.imread('liver-cells-gray.tif',cv2.IMREAD_GRAYSCALE)
image64 = np.float64(image)/255

laplacian = cv2.Laplacian(image, cv2.CV_8U)
laplacian_abs = cv2.convertScaleAbs(laplacian)
laplacian64 = cv2.Laplacian(image64, cv2.CV_64F)
laplacian64_abs = np.float64(laplacian_abs)/255

plt.subplot(3,2,1)
plt.imshow(image, cmap='gray')
plt.title('A) Original')

plt.subplot(3,2,2)
plt.imshow(image64, cmap='gray')
plt.title('D) Original64')

plt.subplot(3,2,3)
plt.imshow(laplacian, cmap='gray')
plt.title('B) Laplacian')

plt.subplot(3,2,4)
plt.imshow(laplacian64, cmap='gray')
plt.title('E) Laplacian64')

plt.subplot(3,2,5)
plt.imshow(image - laplacian, cmap='gray')
plt.title('C) Image - Laplacian')

plt.subplot(3,2,6)
plt.imshow(image64 - laplacian64_abs, cmap='gray')
plt.title('F) Image64 - Laplacian64')

plt.tight_layout()
plt.show()
