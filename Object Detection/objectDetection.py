import cv2 
from random import randint

with open('Object Detection/coco.names','rt') as f:
    class_name = f.read().rstrip('\n').split('\n')

class_color = []
for i in range(len(class_name)):
    class_color.append((randint(0,255),randint(0,255),randint(0,255)))

modelPath = 'Object Detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'Object Detection/frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightPath,modelPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=0.5)
    if len(classIds)!=0:
        for classId,confidence,box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img,box,color=class_color[classId-1],thickness=2)
            cv2.putText(img,class_name[classId-1].upper(),(box[0],box[1]-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,class_color[classId-1],2)
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break