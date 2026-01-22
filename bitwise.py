# Bitwise Operators

# four basic bitwise op => and or xor and 
# bitwise op are used a lot in image processing like in masks
# they oprate in a binary manner, pixel is turned off if it has a value of 0 and on if 1

import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
# use this blank variable as a basis to draw a rectangle and draw a circle

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
# color = 255, single it is a binary image not a color image
# thickness = -1 , cuz we want to fill this image

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
# pass centre, rad, color, thickness


cv.imshow('Rectangle', rectangle)
cv.imshow("Circle", circle)

# 1. bitwise AND -> intersecting regions

bitwise_and = cv.bitwise_and(rectangle, circle)             # pass in two source images (rec, cirle)
cv.imshow("Bitwise AND", bitwise_and)

# What did bitwise did was, it took he two images and placed them on top of each other and returned the intersection

# 2. bitwise OR -> non-intersecting and intersecting regions

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)
# it just placed the two images on top of each, and found regions which common and uncommon

# 3. bitwise XOR -> non-intersecting regions

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# 4. bitwise NOT -> inverts the binary color

# it doesn't return anything, it inverts the binary color
# it takes in only one source image

bitwise_not = cv.bitwise_not(circle)        # black to white and white to black
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)