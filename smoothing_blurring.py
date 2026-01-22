import cv2 as cv

img = cv.imread('kitten.jpg')
cv.imshow('Kitten',img)

# Methods of Blurring

# 1. Averaging 

# we define a kernel window ovr the specific portion of am image
# this window will compute the pixel intensity of middle pixel of the true centre as the avg of surrounding pixel intensities 
# This window (kernel) slides over the entire image, and for each pixel, the averaging operation is repeated

average = cv.blur(img, (3,3))       # blur() => avg blur but generally pass in odd (3,3) kernel
cv.imshow('Average Blur', average)     # more is the kernel size => more is blur

# 2. Gaussian Blur

# It does the same thing as blur, but instead of computing the average of all of this pixel intensity,
# each surrounding pixel is given a particular weight.
# And, the avg of the products of those weights give u the value of centre
# gaussian blur is more natural and gives less blur compared to avg blur

gauss = cv.GaussianBlur(img, (3,3), 0)      # sigmaX => std deviaviation in x direction
cv.imshow('Gaussian Blur', gauss)

# though kernal size is same, the blur is more in avg blur

# 3. Median Blur

# its same as avg blur, instead of doing avg it takes median
# it is more effective in reducing noise in an image as compared to averaging and even gaussian blur. 
# it is good at removing some salt and pepper noise that may exist in the image
# it is used in adv opencv projects that tend to depend on the reduction of substantial amount of noise

median = cv.medianBlur( img, 3)         # here the kernel size is an int and not tuple, 
                                        # cuz opencv automatically assumes that kernal is 3,3 just by passing 3  

cv.imshow('Median Blur', median)
# median blurring is not meant for high kernel sizes like 7 and even 5 is some cases

# 4. Bilateral Blur

# it is the most effective, sometimes it is used in a lot adv cv projects
# Traditional blurring methods basically blur the image without looking at whether you're
# reducing edges in the image or not.
# Bilateral blurring, applies blurring but retains the edges in the image,
# So u have a blurred image, but you get to retain the edges as well

bilateral = cv.bilateralFilter(img, 10, 35, 15)                     # we pass diameter of the pixel neighbourhood and not kernel size

# sigmaColor : a larger value of it => there are more colors in the neighbourhood, that will be considered when the blur is computed
# sigmaSpace : larger the value => pixels further out from the central pixel will influence the blurring calculation of centre
cv.imshow('Bilateral',bilateral)        
# we get smushed or washed out image fo higher values of sigma space, color



cv.waitKey(0)


