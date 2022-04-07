import cv2 
import numpy as np
from tenacity import retry_if_not_exception_type

def empty(a):
    pass






path = 'E:\\workspace\\opencv_class\\final_pro\\s\\img\\roll_1.png'#E:\\workspace\\work_2021_2022\\1094_13.jpg\\smoke_3.jpg
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",89,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",39,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",185,255,empty)

cap = cv2.VideoCapture(0) 
while True:
    #img = cv2.imread(path)
    ret, img = cap.read()
    print(retry_if_not_exception_type)
    img = cv2.resize(img,(400,400))
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask) #MIX both of ori and hsv


    cv2.imshow("ori",img)
    cv2.imshow("hsv",imgHSV)
    cv2.imshow("mask",mask)
    cv2.imshow("imgResult",imgResult)

    
    cv2.waitKey(1)
