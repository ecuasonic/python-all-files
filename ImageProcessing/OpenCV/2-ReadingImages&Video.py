import cv2

# This method basically takes in a path to an image and returns that image as a matrix of pixels
img = cv2.imread('Images\Lake.jpg')

# This method is used to display the image as a new window; The image could be too big for the monitor, in terms of pixels
cv2.imshow('A picture of a lake', img)

# Reading Videos
capture = cv2.VideoCapture('MindMap #1.mp4')
# cv2.VideoCapture(Integer) ; You would provide an integer argument, if you are using your webcame or a camera connected to your computer
# Zero would reference your webcame, one would reference the first camera connected to your computer, and so on

# In the case of reading and videos, we actually use a one loop and read the video frame by frame.
while True:
    isTrue, frame = capture.read() 
    # This capture.read() reads in this video frame by frame, and returns the frame and a boolean that says whether the frame was successfully read in or not
    cv2.imshow('Video from PHIL class', frame)
    if cv2.waitKey(1) & 0xFF==ord('d'): # if the letter d is pressed, then break out of video
        # The purpose of '0xFF' is to ensure that only the lower 8 bits of the result are used, and the higher bits are discarded
        break
    # If the video ends and there are no more frames, an error will pop up
capture.release()
cv2.destroyAllWindows()

# This method is basically a keyword binding function, it waits for a specific delay, or time in milliseconds for a key to be pressed.
#cv2.waitKey(0) # input of zero means that it basically waits for an inifinite amount of time for a keyboard key to be pressed. 