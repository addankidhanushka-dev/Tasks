import cv2 as cv
import numpy as np

img = cv.imread("cat.jpg")
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  

mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 800, img.shape[0]//2 + 800), 255, -1)
cv.imshow("Mask", mask)

#masked = cv.bitwise_and(img, mask)          # this is incorrect => we can't pass in mask and img as two source images
masked = cv.bitwise_and(img, img, mask = mask)

cv.imshow("Masked Image", masked)                   


cv.waitKey(0)


