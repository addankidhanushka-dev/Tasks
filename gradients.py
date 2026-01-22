import cv2 as cv
import numpy as np

img = cv.imread('Boston.jpg')
cv.imshow('Boston', img)

# Gradients and edge detection
# Gradients => are like edge-like regions that are present in an image
# in mathematical pov they are completely diff,  in programming perspective we can get away assuming that they are almost the same.
# previously we have seen the canny-edge detector , now we'll see 2 other edge detector

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Methods of edge detection
# 1. Laplacion

# An edge is where intensity changes suddenly.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)
# this looks like pencil shading and then lightly smurged
# thismethod computes the gradients of this image the greyscale image.
# when we transition from black to white and white to black , that considered positive and neg slope
# but images cannot have neg pixel values, so we compute absolute value of that image so all the pixel values of the image are converted to abs values
# and then we convert them to uint8 a image specific data type


# 2. Sobel (gradient magnitude representation)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow('Combined Sobel', combined_sobel)

# 3. Canny edge detector

canny = cv.Canny(gray, 150, 175)        # canny is a binary image, it is a multi stage process, in which one stage is sobel method
cv.imshow('Canny', canny)



cv.waitKey(0)