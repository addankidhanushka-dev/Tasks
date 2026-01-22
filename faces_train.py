import os
import cv2 as cv
import numpy as np

# Method to print names of people (aliter)

# p = []
# for i in os.listdir(r'/Users/addankidhanushka/Downloads/faces_train'):          #DS_Store is a hiddlen file in mac
#     p.append(i)                   # prints all the folder names in the folder
    
# print(p)


people = [ 'Bill Gates', 'Elon Musk',  'Mark Zuckerberg', 'Ratan Tata', 'Steve Jobs']

DIR = r'/Users/addankidhanushka/Downloads/faces_train'      # folder containing five folders of people
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []       # for every face what is it's corresponding label
labels = []

def create_train():              # this fn is gonna loop over every folder in this base folder and 
    for person in people:                            #inside each folder it's gonna loop over every image and grab the 
        path = os.path.join(DIR, person)                        # face in that image and add that to our training set
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)         # DS_Store is a hiddlen file in mac 
            if img_array is None:
                continue   
            
            img_array = cv.imread(img_path)         # Loads the image into a NumPy array
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
                
            for (x,y,w,h) in faces_rect:        # faces_roi => faces of region of intrest
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)          # the idea behind converting label to numerical values is reducing the strain that your will have
                                            # by creating some sort of mapping between a string and a numerical label
create_train()
print('Training done ----------------')
# print(f'Length of the features = {len(features)}')          # faces may not be detected in all the images
# print(f'Length of the labels = {len(labels)}')

# Now we can use this features and labels list to train our recognizer on it




features = np.array(features, dtype='object')       # converting into numpy arrays
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list 
face_recognizer.train(features,labels)      # if we plan to use this face recognizer in another file, we'll have to seperately
                                            # and manually repeat the above process, of adding those images to a list and getting the corresponding labels, and then converting
                                            # them into NumPy arrays, and then training all over again.
                                            # what we can do in OpenCV is we can save this trained model so that we can this in another file, directory etccc just by using that particular YAML source file
                                            
face_recognizer.save('face_trained.yml')        # we can observe that we have the file in our directory, features.npy, labels.npy, features_train.yml
np.save('features.npy', features)
np.save('labels.npy', labels)

# let's use this train model to recognize images
# continued on face_recognition.py file





