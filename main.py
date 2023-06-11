import cv2
from simple_facerec import SimpleFacerec 
import time
import os
import numpy as np
from datetime import datetime

# Load Camera
cap = cv2.VideoCapture(0)

sfr = SimpleFacerec()
sfr.load_encoding_images("photos/")
NAMES = []
def markAttendence(name):
    with open('attendence.csv', 'r+') as f:
        myDataList = f.readline()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%D-%H:%M')
            f.writelines(f'\n{name}, {dtString}') 



while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        

        cv2.putText(frame, name,(x1 , y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        if name != "Unknown" and name not in NAMES:
            NAMES.append(name)
            markAttendence(name)
    


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

