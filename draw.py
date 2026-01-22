import cv2 as cv
import numpy as np

# we can draw on images in 2 ways: 
# a. by drawing on standalone images like this cat
# b. or we can create a dummy image or blank image to work with                                   


blank = np.zeros((500, 500, 3), dtype='uint8')          # create a blank image => of shape 500 by 500 and no.of color channels is 3. data type => uint8
                                                        # uint8 is datatype of an image
           
cv.imshow('Blank', blank)                           # blank image which we're gonna use to draw  
              
                                
# 1. Paint the image a certain color

                                            # It takes image(img) to draw rect over, point1, point2, color, thickness (of borders)=2 or thickness=cv.FILLED/ -1
#blank[:] = 0,255,0                          # all pixels are in same color , (slicing))
#blank[200:300, 300:400]= 0,0,255           # this gives a range of pixels, 200 to 300 and then 300 to 400
#cv.imshow('Green', blank)


# 2. Draw a Rectangle

cv.rectangle(blank, (0,0), (250,250), (255,255,255 ), thickness=-1)  # cv.rectangle is a method 
                                            # cv.FILLED or -1 => fills the rectangle with color , if thickness =2 , then only borders is colored
                                            
cv.imshow('Rectangle', blank)

# instead of giving co ord : 

# cv.rectangle(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2) , (255,255,255 ), thickness=-1)                  
# cv.imshow('Rectangle2', blank)

# 3. Draw A circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40, (0,0,255), thickness=-1)     # 40 is radius of circle and blank.shape... is centre, here the the color is bgr not rgb
cv.imshow("Circle", blank)

# 4. Draw a line                            (standalone line on the image)

# cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (25, 50,95), thickness=3 )
# cv.imshow("Line", blank)

cv.line(blank, (100,250),(300,400), (25, 50,95), thickness=3 )
cv.imshow("Line", blank)

# 5. Write text

cv.putText(blank, "Hello, I'm rishi", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (86, 232, 245), 2 )
cv.imshow("Text", blank)



cv.waitKey(0)