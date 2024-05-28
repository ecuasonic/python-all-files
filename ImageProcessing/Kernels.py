# Week 5 - Image theory and spatial filtering
#     feature map -> kernel -> output
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Average *********************************************
# A rectangular averaging kernel of size rxc. The default is 3x3. A single number instead of [r c] specifies a square kernel
# define the size of the filter (r,c)
r,c = 5,5 # Change these values to the desired filter size

# Create a kernal of ones
kernel = np.ones((r,c), dtype=np.float32)

# Normalize the kernel to get an average filter
kernel =/ (r*c)

# The resulting 'kernel' can be used with OpenCV's 'cv2.filter2D()' function to apply the filter to an image

# Disk ********************************************************
# A circular averaging kernel (within a square of size 2r+1) with radius r. The default radius is 5.
# Define the radius of the disk (structuring element)
radius = 3

# Create a disk-shaped structuring element
selem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*radius+1, 2*radius+1))

# Now, you can use this structuring element with morphological operations.
# For example, if you have a binary image 'image_image':
# - To perform erosion:
#   eroded_image = cv2.erode(input_image, salem)
# - To perform dilation:
#   dilated_image = cv2.dilate(input_image, salem)

# Gaussian *******************************************
# A Guassian lowpass filter kernel of size rxc and standard deviation sig (positive). The defaults are 3x3 and 0.5. A single number instead of [r c] specifies a square kernel.
# Define the size of the filter (r,c)
r,c = 5,5 # Change these values to the desired filter size

# Create a 1D Gaussina kernel in the horizontal direction
gaussian_kernel_x = cv2.getGaussianKernel(c,0)

# Create a 1D Gaussian kernel in the verticle direction
gaussian_kernel_y = cv2.getGaussianKernel(r,0)

# Compute the 2D Gaussian kernel by multiplying the two 1D kernels
gaussian_kernel = gaussian_kernel_x * gaussian_kernel_y

# The resulting 'guassian_kernel' can be used with OpenCV's 'cv2.filter2D()' function to apply the Guassian filter to an image

# Laplacian ****************************************************
# A 3x3 Laplacian kernel whos shape is specified by alpha, a number in the range of [0,1]. The default value for alpha is 0.2.
# Load an image (replace 'image.jpg' with your image file)
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply the Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_8U)

# Convert the result back to the original image format and scale it for the visualization
laplacian_abs = cv2.convertScaleAbs(laplacian)

# Display the original image and the Laplacian-filtered image
cv2.imshow('Original Image', image)
cv2.imshow('Laplacian Filtered Image', laplacian_abs)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

