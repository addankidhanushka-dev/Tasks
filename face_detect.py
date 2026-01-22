# face detection => detects the resence of a face in an image, performed using classifiers
# face recognition => involves identifying whose face it is
# classifier => is an algorithm that decides whether a given image is positve(present) or negtive(absent)
# two main classifiers => haar cascade, local binary patterns
# the latter is more advanced than other, they are not as prone to noise in an image as compared to the haar cascades



import cv2 as cv

img = cv.imread('Photos/group1.jpg')
cv.imshow('People', img)

# Face detection does not involve color, i.e, skin tone etc...
# so we convert it into

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')        # read haar_cascade file

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# neighbors => rectangles
# With minNeighbors, higher value = stricter acceptance
# it detects the faces, and returns the rectanular coordinates of face to faces_rect ( rect=> rectangle)
# faces_rect → list of bounding boxes
# img.shape        = (H, W, 3)
# faces_rect[i]    = (x, y, w, h), x → left (column), y → top (row), w → width, h → height
# do not get confused bw these two diff concepts

print(f'Number of faces found = {len(faces_rect)}')

# we can loop over the rect coordinates and draw a rectangle over the detected faces

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)     #(x, y) → top-left corner of the detected face, w → width of the face box, h → height of the face box

cv.imshow('Detected Faces', img)        # cv.rectangle() modifies the image you pass to it — in place.



# the number of faces is not always accurate, they are really sensitive to noise
# we can also use DLIB’s face recognizer
# we use the same method for videos also

cv.waitKey(0)  








