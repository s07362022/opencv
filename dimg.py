import cv2
import sys
from PIL import Image


def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 960)
    #cv2.VideoWriter(window_name,(1280,960))
  
    
   
    cap = cv2.VideoCapture(0)#,cv2.CAP_DSHOW),cv2.CAP_DSHOW  ,camera_idx              
    #cap = cap.set(3,1080)
   
    #classfier = cv2.CascadeClassifier("C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml")
    conter = 0
    
    color = (0, 255, 0)
    num = 0   
    while cap.isOpened():
        ok, frame = cap.read()#讀取一幀資料
        conter +=1
        if not ok:            
            break                
    
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)            
        
        
        #faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(frame) > 0:          #大於0則檢測到人臉                                                                        
 
            if conter % 200 ==0:
                img_name = '%s//%d.jpg'%(path_name, num)                
                image = frame#[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, frame)                                
                                
                num += 1                
            if num > (catch_pic_num):  
                break
                
                
            #cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(frame,'num:%d' % (num),(x + 30, y + 30), font, 1, (255,0,255),4)                
        
        
        if num > (catch_pic_num): break                
                       
        
        cv2.imshow(window_name, frame)        
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break        
    
    
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id face_num_max path_name\r\n" % (sys.argv[0]))
    else:
        CatchPICFromVideo("catchface", 0, 500,"F:\\img_test\\")
    
