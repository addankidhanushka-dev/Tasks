import cv2 as cv
import numpy as np

img = cv.imread("Boston.jpg")
cv.imshow('Boston', img)

# SPLIT

b,g,r = cv.split(img)               # split into respective channels
                                    # look at american flag in all 3 greycaled images

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)            # for bgr, tuple: (M,N,3) M => Y AXIS, N=> X AXIS, 3 => Z ZXIS ( 3 b,g,r color channels)
print(b.shape)              # here, the shape of the componenet is not mentioned, but it is 1
print(g.shape)              # cv.imshow for b,g,r is showing greyscale image because they have shape 1.
print(r.shape)

# Merge

merge = cv.merge([b,g,r])               # pass in a list of b,g,r
cv.imshow('Merged Image', merge)        # original image

# we can create a blank image an make these grayscaled images of individual channels into their respective colors

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank,blank])        # blank has height and width not necessarily the no of color channels in the image
green = cv.merge([blank,g,blank])       # setting only the componenets we want and others to blank
red = cv.merge([blank,blank,r])

cv.imshow('Blue (with color)', blue)
cv.imshow('Green(with color)', green)
cv.imshow('Red (with color)', red)

cv.waitKey(0)