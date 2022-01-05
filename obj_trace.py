import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("E:\\workspace\\opencv_class\\final_pro\\s\\roo.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
#find the ball color (pink)
myColors = [[159,43,46,179,255,255]   
            ]  
myColorValues = [[0,0,255]          ## BGR
                ]


myPoints =  []  ## [x , y , colorId ]

#利用HSV找到顏色
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

#找輪廓,包含最小矩形box 
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt) # 輪廓面積
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3) #輪廓邊緣
            peri = cv2.arcLength(cnt,True) #弧長
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #近似，為了減少離散點數
            x, y, w, h = cv2.boundingRect(approx) #取得最小外接矩形
          
    return x+w//2,y

#描出原點軌跡
def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED) #描出原點軌跡
 
 
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
 
    
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
