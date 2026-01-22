import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Thresholding : It is binarization of an image
# In general, we convert an image to binary image i.e, an image where pixels are 0 (or black) or 255 (or white) 
# For ex: take an image, then take some particular value that we're going to call the thresholding value and compare each pixel of the image 
# to this thresholding value. If the pixel intensity is less than threshold value , we set that pixel intensity to 0 (black), else 255 (white).
# In this way we can create a binary image from a regular standalone image


# 1. Simple Thresholding

# before thresholding, convert bgr to grayscale
# We use cv.threshold()   fn  that returns threshold value

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# it takes 4 parameters, image, thereshold value, max limit(255), Type of threshold
# simple one that converts below thresh value to 0 and above to 255 is cv.THRESH_BINARY
# It returns two things, 1.thresh=> thresholded(binarized) image, and 2. threshold=> the threshold value we passed (150 here)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# evythg is same just pixels less threshold are now white(255) and above are black(0)



# 2. Adaptive Thresholding

# we observed that, we get diff thresholded images with diff threshold values.
# we have to manuallyspecify threshold value, we can let the computer find the optimal threshold value itself
# using that value it bnarises the image.

# the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image
#  which gives better results for images with varying illumination.

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1 )
cv.imshow('Adaptive Thresholding', adaptive_thresh)

# it takes source image, max limit, adaptiveMethod, type of threshold, kernel size to find the optimal threshold value and blocksize =>C(int) value which is subtracted from mean ;as parameters
# in adaptive threshold threshold value is diff for diff regions of image

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding Inverse', adaptive_thresh_inv)
# Gaussian method=> add a weight to each pixel value and computed mean across the pixels
 


cv.waitKey(0)