import numpy as np
import cv2

cap = cv2.VideoCapture(0)

i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    print(i)
    i+=1

# When everything done, release the capture
cap.release()
