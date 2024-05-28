import cv2

# We usually resize and rescale video files and images to prevent computation strain.
# Large media files tend to store a lot of information in it and displaying it takes up a lot of processing needs
# By resizing and rescaling, we're getting rid of some information

# The frame / image has dimensions format as (height, width, colorChannels)
# The imput dimension for cv2.resize() has dimensions format as (width, height)
def rescaleFrame(frame, scale=0.75):
    # Images, Videos, and Live Video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3,width) # '3' references the width
    capture.set(4,height) # '4' references the height

img = cv2.imread('images\lake.jpg')
cv2.imshow('Lake Pic', img)
cv2.imshow('Rescale Lake Pic', rescaleFrame(img))

# Reading Videos
capture = cv2.VideoCapture('MindMap #1.mp4')

while True:
    isTrue, frame = capture.read() 

    frame_resized = rescaleFrame(frame, scale = 0.2)
    
    cv2.imshow('Original Video', frame)
    cv2.imshow('Rescale Video', frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv2.destroyAllWindows()

capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    
    cv2.imshow('Live Video', frame)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release() # releases the camera, freeing up system resources
cv2.destroyAllWindows() # closed all OpenCV windows