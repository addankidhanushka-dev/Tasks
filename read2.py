# Reading Videos

import cv2 as cv

#capture = cv.VideoCapture(0)            # this method either takes integer arguments or path
                                         # we use an integer arg if we are using webcam, or cam that is connected to the comp
                                         # if we have multiple cams connected to our comp, then we could ref them using appropriate arg
                                         # 0 => our webcam, 1 => 1st cam that is connected to our comp, like this 2nd cam and so on
                                         # now, we are gonna be looking at how to read an already existing videos from a file path.
                                        
capture = cv.VideoCapture('dog.mp4')                        # reading voideos is diff from reading images
                                                            # in reading videos, we use a while loop and read video frame by frame.
                                                            # capture is a pointer here.
 
 
while True:
    isTrue, frame = capture.read()          # this capture.read() reads this video frame by frame.  
    cv.imshow('Video', frame)               # It returns a frame and a boolean that says whether the frame was successfully read in or not               
                                            # to display this video, we display an individual frame => cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):     # this stops the video from playing indefinitely
        break                               # Break out of while loop
                                            #0xFF==ord('d') => says that if letter d is pressed, break out of lop and stop playing this video
                    
                    
capture.release()                          # release the capture pointer
cv.destroyAllWindows()                     # it is is an OpenCV function, that closes all the windows opened by other OpenCV fns.

# the capture variable is an instance of this video capture class, inside of while loop the video frame by frame by
# using the captured.read() method, we display each frame of the vide by using cv.imshow method

# if we don't press any key=d, then it closes itself by giving error(as it can't find more frames), the same thing happens if u put wrong file path