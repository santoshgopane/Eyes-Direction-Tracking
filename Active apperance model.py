import numpy as np
import pandas as pd
import cv2

cap = cv2.VideoCapture(0)

while True:
    success,image = cap.read()
    cv2.imshow('Eyes Tracking',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
