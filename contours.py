# Contours
# Contours are the boundries of objects
# the line or curve that joins the continuous points along the boundary of an object
# From mathematical point of view they are not the same as edges
# ()for most of the time we can get away thinking that contours are edges)

# BASIC PIPELINE (must follow this order)
#Image → Grayscale → Blur → Threshold / Canny → findContours → drawContours



import cv2 as cv
import numpy as np

img = cv.imread("Boston.jpg")
cv.imshow('Boston', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges (blur & gray)", canny)

canny_non_blur = cv.Canny(img, 125, 175)
cv.imshow("Canny edges(gray)", canny_non_blur)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold (Boston in gray)", thresh)

# to get contours use findcontours() method

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')         

# ig contours drawn with canny are close to canny edges (with blur), but contours drawn with threshold are close to canny edges
# generally use canny and then find contours using that rather than using threshold




# cv.RETR_LIST => It returns and finds the contours
# cv.RETR_EXTERNAL => It retrives only the external contours, all the ones on the outside it returns those
# cv.RETR_TREE => It returns all the contours in the heirarachical system

#there are three arguments in cv.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method.


# cv.RETR_LIST => returns all the heirarchical contours (list)
# cv.CHATN_APPROX_NONE => this is contour approximation method, NONE => does ntg, it returns all the contours
# cv.CHAIN_APPROX_SIMPLE => this essentially compresses all the quantities that are returned into simple ones
# for ex: if we have a line in an image, if we use cv.CHATN_APPROX_NONE => it gives all the co ordinates of the line
# whether if we use  cv.CHAIN_APPROX_SIMPLE => it takes all the points of that line an compresses it into the two end points only. cuz
# wkt a line is defined by two end points only, we do not need all the points 


# if we blur then find canny and then find contours nstaed of directly doing, canny and then blur we get reduce the no of contour (drastically)
# instaed of using blur and then canny we can directly use threshold


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

cv.drawContours(blank, contours, -1, (0,0,255), 1) 
cv.imshow('Contours Drawn(blur)', blank)
# this method takes in an image to draw over, and it takes contours, and also contour index(number)=> -1 if all, and color






img2 = cv.imread("water_coins.jpg")
cv.imshow("Coins",img2)

gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.imshow("Coins", img2)

ret2, thresh2 = cv.threshold(gray2, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold (Coins in gray)", thresh2)
# threshold takes an image and binarize that image, if intensity < 125 => (0 or black) and if instensity > 125 => (255 or white)


contours2, heirarchies2 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)} contour(s) found!')




cv.waitKey(0)