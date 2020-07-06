import cv2
import numpy as np

def sketch(image):
       gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
       blur= cv2.GaussianBlur(gray_image,ksize=(3,3),sigmaX=0,sigmaY=0)
       edge = cv2.Canny(blur,5,70)
       ret,th = cv2.threshold(edge,100,255,cv2.THRESH_BINARY_INV)
       return th

cap = cv2.VideoCapture(0)
while True:
       ret,frame = cap.read()
       cv2.imshow('Live Sketch',sketch(frame))
       
       if cv2.waitKey(1)==13:
              break
cv2.imshow("live",sketch(frame))
cap.release()
cv2.destroyAllWindows()
