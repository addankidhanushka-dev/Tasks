import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Boston.jpg")
cv.imshow('Boston', img)

# 1. BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# 2. BGR to HSV
#( HSV => huge saturation value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3. BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

cv.waitKey(0)