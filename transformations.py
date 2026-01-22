import cv2 as cv
import numpy as np


img = cv.imread('water_coins.jpg')

cv.imshow("Coins", img)


# 1. Translation
# It is basically shifting an image along the x and the y axis.( up, down, left, right)

# s1) Create a Translation fn:

def translate(img, x, y):                                 # x and y stands for number of pixels u want to shift along the x and y axes respectively.
    transMAT = np.float32([[1,0,x], [0,1,y]])             # s2) create a matrix that takes a list with two lists inside it.
    dimensions = (img.shape[1], img.shape[0])             # dim => (a tuple of wid and heig); img.shape[1] => width and img.shape[0] => height
    return cv.warpAffine(img, transMAT, dimensions)

# -x --> Left 
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)           # shifted left and down both by 100 pixels
cv.imshow("Translated", translated)



# 2. Rotation
# rotation point is centre by default


def rotate(img, angle, rotPoint=None):                          # by default angle is in anti clockwise
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint= (width//2, height//2)              

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)          # scale = 1.0, cuz we don't wanna scale it while rotating 
    dimensions = (width,height)                                     # it tells opencv what hould be the dim of output image

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)                       # rotates anti clockwise by default
cv.imshow('Rotated',rotated)                    # here, we get to see some black triangle

# we can rotate rotated image too!

rotated_rotated = rotate(img, 90)
cv.imshow('Rotated Rotated', rotated_rotated)       # here there is some black which is due to black triangles created earlier



# 3. Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)       # INTER_LINEAR , INTER_CUBIC are used to enlarge, but latter is slower but much better 
cv.imshow("Resized", resized)


# 4. Flipping 

img2 = cv.imread('monkey.jpg')
cv.imshow("Monkey",img2)

flip = cv.flip(img2, 1)          # the 2nd argument is flipcode. It can be 
                                # 0 => flip vertically (x axis) 
                                # or 1 => flip hori (y axis)) => look like mirror images
                                # or -1 => flip hori and vert ( both x and y axes)
cv.imshow('Flip',flip)


# 5. Cropping

cropped = img2[200:400, 300:400]         # slicing 
#200:400 → rows 200 to 399 → vertical range (top → bottom)
#300:400 → columns 300 to 399 → horizontal range (left → right)

cv.imshow('Cropped', cropped)








cv.waitKey(0) 