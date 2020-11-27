import numpy as np
#YOLO_network
net = cv2.dnn.readNetFromDarknet("F:\\program1\\yolo\\darknet-master\\build\\darknet\\x64\\yolov3.cfg","F:\\program1\\yolo\\darknet-master\\build\\darknet\\x64\\all\\yolov3_last.weights")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
classes = [line.strip() for line in open("F:\\program1\\yolo\\darknet-master\\build\\darknet\\x64\\obj.names")]
colors = [(0,0,255),(255,0,0),(0,255,0)]
####################CNN
import imutils
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Dropout, Flatten ,BatchNormalization
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
import keras
IMAGE_SIZE =640
train_list = []
train_ary= np.zeros(shape=(100,640,640,3))
model = load_model('C:\\Users\\User.DESKTOP-IIINHE5\\Desktop\\stand_fall3.h5') #model_load
def resize_image(image, height = IMAGE_SIZE, width = IMAGE_SIZE):
    top, bottom, left, right = (0, 0, 0, 0)
    
    h, w, _ = image.shape
    
    longest_edge = max(h, w)    
    
    if h < longest_edge:
        dh = longest_edge - h
        top = dh // 2
        bottom = dh - top
    elif w < longest_edge:
        dw = longest_edge - w
        left = dw // 2
        right = dw - left
    else:
        pass 
    
    BLACK = [0, 0, 0]
    
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value = BLACK)
    
    return cv2.resize(constant, (height, width))
################################
def yolo_detect(frame):
    # forward propogation
    img = frame
    print(type(img))
    #img = cv2.resize(frame, None, fx=0.4, fy=0.4)
    #print(type(img))<class 'numpy.ndarray'>
    height, width, channels = img.shape 
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # get detection boxes
    class_ids = []
    confidences = []
    boxes = []
    
    for out in outs:
        for detection in out:
            tx, ty, tw, th, confidence = detection[0:5]
            scores = detection[5:]
            class_id = np.argmax(scores)  
            if confidence > 0.6:   
                center_x = int(tx * width)
                center_y = int(ty * height)
                w = int( tw * width)#tw *
                h = int( th * height)#th *

                
                x = int(center_x - w/2 )
                y = int(center_y - h/2 )
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                
    # draw boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x,y), (x+w,y+h), color, 1) 
            #print(x,y,(x+w),(y+h))
            image = img[y - 10: y + h + 10, x - 10: x + w + 10]
            cv2.putText(img, label, (x, y -5), font, 1, color, 1)
            ################
            train = resize_image(image, IMAGE_SIZE, IMAGE_SIZE)
            train_list.append(train)
            global train_ary
            train_ary = np.array(train_list, dtype=np.float32)
            ID = model.predict_classes(train_ary)#_classes
            #preds = model.predict(train_ary)
            #ID = np.argmax(preds[0])
            print(ID[-1])
    
    return img

import cv2
import imutils
import time

#VIDEO_IN = cv2.VideoCapture(0)
import os
while True:
    
    #hasFrame, frame = VIDEO_IN.read()
    datasets = ['F:\\img_test\\'+ f for f in os.listdir('F:\\img_test\\') if not f.endswith('.txt')]
    #print(len(datasets) *0.8)
    print(datasets[-1])
    a = cv2.imread(datasets[-1])
    frame= a
    
    img = yolo_detect(frame)
    cv2.imshow("Frame", imutils.resize(img, width=1200,height=960))#imutils.resize(img), width=, width=860
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
VIDEO_IN.release()
cv2.destroyAllWindows()

