import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# we can create a mask and compute histogram only for that mask
# we can do this by setting mask parameter in cv.calcHist to mask

img = cv.imread("cat.jpg")
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 800, 255, -1)

# 1.b) Grayscale Histogram (with mask)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
mask = cv.bitwise_and(gray, gray, mask = circle)        # take mask of gray
cv.imshow('Mask', mask)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])        # the image that we pass in is a list, (almost all parameters are lists)


plt.figure()                    # It tells Matplotlib: “Start a fresh plot here.”
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])           # a limit to x axis 
plt.show()


cv.waitKey(0)