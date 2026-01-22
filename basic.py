import cv2 as cv

img = cv.imread('water_coins.jpg')

cv.imshow("coins", img)


# 1. Converting (image) to grayscale
# we can only see intensity distribution rather than the color itself

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)              # bgr => gray
cv.imshow("Gray", gray)

# 2. Blur
# it is used to remove some noise that exists in an image
# for ex, there might be some elements having bad lighting etc...
# the blurring technique we are gonna use is 'Gaussian blur'

blur =cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)               # ksize or kernel size is a tuple of size 2 with only odd numbers
cv.imshow("Blur", blur)



# 3. Edge Cascade
# We are gonna use canny edge detector

canny = cv.Canny(img, 125, 175)         # threshold 1 and 2
cv.imshow("Canny Edges", canny)


canny2 = cv.Canny(blur, 125, 175)          # passing Blur image
cv.imshow("Canny Edges of Blur", canny2)   # here we found far less edges

# by using slight blur we can reduce edges



# 4. Dilating the image

dilated = cv.dilate(canny, (7,7), iterations=1 )          # dilations we apply on canny image
cv.imshow("Dilated of Canny", dilated)

# Canny detects edges in an image, while dilation expands existing edges to make them thicker and more connected.



# 5. Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded of (dilated)", eroded)

# erode (erosion) is a morphological operation used in image processing to shrink white (foreground) regions and remove small noises from an image.
# White pixels are removed from the edges



# 6. Resize

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)             # it resizes the image to 500 by 500 ignoring the aspect ratio
cv.imshow("Resized",resized)                                        # interpolation is usefu if we r trying to shrink image to dimensions that r smaller than that of orginal dim (interpolation=cv.INTER_AREA)
                                                                    # in some cases, to enlarge the image or scale the image to a much larger dimensions we use:
                                                                    # interpolation=cv.INTER_LINEAR OR interpolation=cv.INTER_CUBIC
                                                                    # INTER_CUBIC : it is slowest , but the resultant image is of much higher quality compared to others



# 7. Cropped
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)



cv.waitKey(0)


