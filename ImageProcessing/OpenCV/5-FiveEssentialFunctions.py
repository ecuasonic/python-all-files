import cv2

img = cv2.imread('R.jpg') # currently, this is BGR image, a three channel blue, gree, and read image

# Converting to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
# To remove noise in an image, blurring is used
blur = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)

# Edge Cascade
canny = cv2.Canny(img, 125, 175)
cannyBlur = cv2.Canny(blur, 125, 175)

# Dilating the Image
# Dilate image using a specific structring element, which is the canny edges in this case
dilated = cv2.dilate(canny, (3,3), iterations=3)

# Eroding the Dilated Image (Dilate Inverse)
eroded = cv2.erode(dilated, (7,7), iterations=3)

# Resize
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
# interpolation=cv2.INTER_AREA, by default, which is useful when making images smaller
# use interpolation=cv2.INTER_LINEAR or interpolation=cv2.INTER_CUBIC when making images larger
cv2.imshow('resized', resized)

# Cropping
# Images are arrays, and we can employ array splicing
cropped = resized[50:200, 200:400]
cv2.imshow('cropped', cropped)

cv2.waitKey()