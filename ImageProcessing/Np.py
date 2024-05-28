import numpy as np
import cv2
import matplotlib.pyplot as plt

M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[2,1,7],[8,9,3],[3,4,6]]

M1 = np.array(M1)
M2 = np.array(M2)

# Matrix dimensions
np.shape(M1)

# Matrix Multiplication
C_mat = np.matmul(M1,M2)

# ELementwise Multiplication
C_element = np.multiply(M1,M2)


# Zero Matrix
Zeros = np.zeros(shape=[3,3])

# One Matrix
Ones = np.zeros(shape=[3,3])

# Identity Matrix
I = np.eye(3)

# Random Matrix
R = np.random.rand(3,3)


# Random Image
rand_im = np.random.rand(300,400)
plt.imshow(rand_im)
plt.title("Random Image")
#plt.show()

plt.imshow(rand_im, cmap = 'gray')
plt.title("Random Image with Grayscale Colormap, Colorbar, Axis Labels")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar()
#plt.show()

# Loading image as is
img = cv2.imread('R.jpg')
np.shape(img)

first_channel = img[:,:,0]
second_channel = img[:,:,1]
print(np.array_equal(first_channel, second_channel))

img = cv2.imread('R.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
plt.show()

# Generating Noise
shape_of_image = np.shape(img)
noise = np.random.rand(shape_of_image[0], shape_of_image[1])
print("The minimum and maximum value of the noise is: ", np.min(noise), "and ", np.max(noise))

noise_255 = noise*256
print("Min and max value of scaled noise is: ", np.min(noise_255), "and ", np.max(noise_255))

# Additive Noise
img_additive = np.add(img, noise_255)
plt.imshow(img_additive, cmap='gray')
plt.title('Additive Noise')
plt.show()

# Multiplicative Noise
img_multiplicative = np.multiply(img,noise)
plt.imshow(img_multiplicative, cmap='gray')
plt.title('Multiplicative Noise')
plt.show()