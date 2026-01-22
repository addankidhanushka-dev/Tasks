import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Boston.jpg")
cv.imshow('Boston', img)

# plt.imshow(img)                 # we get an inversion of colors since, in opencv => bgr and in others => rgb

# plt.show()


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)            # here also we see inversion of colors, cuz we gave gave OpenCV an rgb image and it assumes it was bgr 

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# L*a*b to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)


plt.imshow(rgb)                 # proper image, cuz rgb is given to matplotlib
plt.show()


# We cannot convert gray directly to hsv 
# we first convert gray to bgr and then to hsv
# convert gray to bgr and then to lab too!
cv.waitKey(0)


















