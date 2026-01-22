import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Histograms allow us to visualize the distribution of pixel intensities in an image
# Whether it is a color image or a greyscale image
# It's kinda like a graph or a plot

img = cv.imread("kitten.jpg")
cv.imshow('Kitten', img)


# 1. Grayscale Histogram

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])        # the image that we pass in is a list, (almost all parameters are lists)

# histSize => No.of bins that we want to use for computing the histogram
# range => range of all possible pixel values

plt.figure()                    # It tells Matplotlib: “Start a fresh plot here.”
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])           # a limit to x axis 
plt.show()
# Bins are intervals, Since we know that the range of information value for this case is 256 values, we can segment our range in subparts (called bins) 
# and we can keep count of the number of pixels that fall in the range of each (bin)i. Applying this to the example above we get the image below (axis x represents the bins and axis y the number of pixels in each of them).

# we can create a mask and compute histogram only for that mask
# we can do this by setting mask parameter in cv.calcHist to mask




cv.waitKey(0)