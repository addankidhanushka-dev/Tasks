import cv2 as cv
import numpy as np

img = cv.imread("cat.jpg")
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 800, 255, -1)
cv.imshow("Circle", circle)

rectangle = cv.rectangle(blank.copy(), (800,800), (2000,2000), 255, -1)
cv.imshow("Rectangle", rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)  
cv.imshow("Weird Shape", weird_shape)     

# using weird image as mask
# always remember that the size of your mask has to be in same dimensions as that of your image, otherwise u would get an error
# here, initially blank was in same dim and all came in same dim

masked = cv.bitwise_and(img, img, mask = weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)

