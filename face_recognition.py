import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Bill Gates', 'Elon Musk',  'Mark Zuckerberg', 'Ratan Tata', 'Steve Jobs']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')
# we can now read in this face_trained.yml file

#Load trained face recognizer
#This does face recognition, not detection.

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')        # passing the path to .yml file

img = cv.imread(r'/Users/addankidhanushka/Downloads/images-3.jpeg')   # pass any image path of elon musk and others    
# while pasting the path from terminal make sure that there are no spaces, and in terminal some names have extra '/' in between , so remove that. 
# for ex: Elon\ Musk => Elon Musk


# TO GET PATH: just past the pic or folder or file onto terminal u can see the path

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)


# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)        # returns : [(x, y, w, h), (x, y, w, h), ...], each tuple is: (x, y) → top-left corner, w → width, h → height

# grab the region of intrest (roi)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]      # y to y+h, and x to x+h, Crop only the face region so LBPH (Local Binary Patterns Histogram) can analyze it.

    label, confidence = face_recognizer.predict(faces_roi)      #This compares the face ROI with trained faces, if confidence = 0 (perfect match) and the value worse match
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0), thickness=1 )
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

# we can also do:

# if confidence < 60:
#     name = people[label]
# else:
#     name = "Unknown"
# Otherwise, every face is forced to be someone from our list.

cv.waitKey(0)



