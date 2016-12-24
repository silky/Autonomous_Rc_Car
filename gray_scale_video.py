#converts incoming video to grayscale 
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, gray = cv2.threshold(gray, 127, 255, 0)
   # dst = cv2.fastNlMeansDenoising(gray, None, 4,7,21 )
    cv2.imshow('gray_scale', gray)
   # cv2.imshow('denoised', dst)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
