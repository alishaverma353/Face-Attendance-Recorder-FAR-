import cv2
import numpy as np
import face_recognition

# Load and convert images
imgelon = face_recognition.load_image_file('imagesbasic/elon musk.png')
imgelon = cv2.cvtColor(imgelon, cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('imagesbasic/elon test.png')
imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

# Find face location and encodings in the Elon Musk image
faceloc = face_recognition.face_locations(imgelon)[0]
encodeElon = face_recognition.face_encodings(imgelon)[0]
# Draw rectangle around Elon Musk's face
cv2.rectangle(imgelon, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)

# Find face location and encodings in the test image
facelocTest = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest)[0]
# Draw rectangle around the test face
cv2.rectangle(imgtest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (255, 0, 255), 2)

# Compare the faces and calculate the distance
results = face_recognition.compare_faces([encodeElon], encodetest)
faceDis = face_recognition.face_distance([encodeElon], encodetest)
print(results, faceDis)
cv2.putText(imgtest,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

# Display the images
cv2.imshow('Elon Musk', imgelon)
cv2.imshow('Elon Test', imgtest)
cv2.waitKey(0)
cv2.destroyAllWindows()
