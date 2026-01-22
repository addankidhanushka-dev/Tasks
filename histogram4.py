import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# we can create a mask and compute histogram only for that mask
# we can do this by setting mask parameter in cv.calcHist to mask

img = cv.imread("cat.jpg")
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 800, 255, -1)
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Mask', masked)

# 2.b) Color Histogram (with mask)
    

plt.figure()                    # It tells Matplotlib: “Start a fresh plot here.”
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0,256])           # a limit to x axis 


colors = ('b', 'g', 'r')
for i,col in enumerate(colors):  # iterates 3 times             # enumerate(colors) => used to loop over a list and get both the index and the value at the same time.
    hist = cv.calcHist([img], [i], mask, [256], [0,256])        # None => no mask use full image, # do not use masked, we must use mask cuz it is the filter
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)