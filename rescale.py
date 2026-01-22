import cv2 as cv

img = cv.imread("cat.jpg")                   # rescaling => modify height and width
                                                    # it's a good practice to downscale them, while rescaling                                 
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and live Video
    width = int (frame.shape[1] * scale)                  #frame.shape[1] => width, frame.shape[0] => height, they are floats
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)                          # tuple of wid and heig
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)                    # cv.resize => resizes the frame into a particular dim



def changeRes(width, height):                        # changeRes changes the resol of video
    # Live video only
    capture.set(3, width)                            # capture.set() => 3, 4 are properties of this class
    capture.set(4, height)


resized_image = rescaleFrame(img, 0.2)              # pass another arg to scale = 0.2 (20%))
cv.imshow('Image', resized_image)                   # resizing image



# Reading videos

capture = cv.VideoCapture("dog.mp4")

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, 0.2)         # (resizing videos frame by frame) scale = 0.75 can be changed by passing another arg
    
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
    
capture.release()
cv.destroyAllWindows()