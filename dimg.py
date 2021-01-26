import cv2
import sys
from PIL import Image
#######下載攝影機錄製的圖片#######

def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1280, 860)
    
    #視訊來源，可以來自一段已存好的視訊，也可以直接來自USB攝像頭
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)#,cv2.CAP_DSHOW  ,camera_idx              
    
    color = (0, 255, 0)
    num = 0   
    while cap.isOpened():
        ok, frame = cap.read() #讀取一幀資料
        if not ok:            
            break                
    
        
        if len(frame) > 0:          #大於0則檢測到人臉                                                                         
            #將當前幀儲存為圖片
            img_name = '%s//%d.jpg'%(path_name, num)                
            
            cv2.imwrite(img_name, frame)                                
                                
            num += 1                
            if num > (catch_pic_num):   #如果超過指定最大儲存數量退出迴圈
                break
                
                
            font = cv2.FONT_HERSHEY_SIMPLEX
                           
        
        #超過指定最大儲存數量結束程式
        if num > (catch_pic_num): break                
                       
        #顯示影象
        cv2.imshow(window_name, frame)        
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break        
    
    #釋放攝像頭並銷燬所有視窗
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id face_num_max path_name\r\n" % (sys.argv[0]))
    else:
        CatchPICFromVideo("catchface", 0, 100,"C:\\Users\\User\\Desktop\\C")
