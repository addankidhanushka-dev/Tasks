# TO RUN THESE FILES:
#1. cd OPENCV_PROJECTS
#2. python filename.py

# Reading Images

import cv2 as cv

img = cv.imread("cat.jpg")                # cv.imread() is a method to read an image from a file, and returns it as a matrix (numpy array) or pixel data.
                                    # it can take ealtive or absolute file paths as input.
                                    
cv.imshow("Cat", img)              # cv.imshow method displays the image as a new window,                            
                                    # we have to pass in the name of the window, and the actual matrix of pixels to display (img, here)
                                    
        
cv.waitKey(0)                       # cv.waitKey(0) is a keyboard binding fn,
                                    # it waits for specific delay or time in milli seconds for a key to be pressed
                                    # here, zero meas it waits for infinite amount of time for a keyboard key to be pressed.
                                    # the image was of dim 350 by 350

# to get a much larger version:

#img = cv.imread("cat_large.jpg")      # this makes image goes off screen, this is cause the dim of image is far greater than the monitor he was working on.
        
        
        
        
        
        
        
        
        
        
        
        
        