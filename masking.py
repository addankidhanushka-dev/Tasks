import cv2 as cv
import numpy as np

# Masking
# It allows us to focus on certain parts of an image that we'd like to focus on

img = cv.imread("kitten.jpg")
cv.imshow('Kitten', img)

blank = np.zeros(img.shape[:2], dtype='uint8')      # img.shape[:2] => give the height and width of image
# The dimensions of the mask have to be the same size as that of the image
# otherwise it doesn't work
cv.imshow("Blank Image", blank)

# draw a circle over this blank image and we're gonna call it mask
mask = cv.circle(blank, (img.shape[1]//2 + 95, img.shape[0]//2 - 25 ), 100, 255, -1)
# color => 255 (binary)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask = mask)      # RHS mask=> the circle image on blank
cv.imshow("Masked Image", masked)                   # finding the intersection




cv.waitKey(0)




