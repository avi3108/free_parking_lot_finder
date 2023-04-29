import numpy as np
import pickle
import cvzone
import cv2

cap = cv2.VideoCapture("video/carPark.mp4")
weidth , height = 107, 48 

with open("carparkpos","rb") as f:
    pos = pickle.load(f)

def checkparkingstat(imgpro):
    spaceCounter = 0
    for pos1 in pos:
        x , y = pos1
        imgCrop = imgpro[y:y+height, x:x+weidth]
        # cv2.imshow(str(x*y),imgCrop)
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale = 1, thickness=2,offset =0,colorR=(0,0,255))
        if count <900 :
            color =(0,255,0)
            thickness = 5
            spaceCounter +=1
        else :
            color =(0,0,255)
            thickness = 2
        cv2.rectangle(img,pos1,(pos1[0] + weidth, pos1[1] + height),color,thickness)
        cvzone.putTextRect(img,str(count),(x,y+height-3),scale = 1, thickness=2,offset =0,colorR=color)
    cvzone.putTextRect(img,f'free: {spaceCounter} / {len(pos)} ',(100,50),scale = 3, thickness=5,offset =20,colorR=(0,200,0))

while True :
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    succ , img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    adpThres = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    medianBlur = cv2.medianBlur(adpThres,5)
    kerne1 = np.ones((3,3),np.uint8)
    imgDialet = cv2.dilate(medianBlur,kerne1,iterations=1)
    checkparkingstat(imgDialet)
    
    

    cv2.imshow("video",img)
    # cv2.imshow("videoBlur",imgBlur)
    # cv2.imshow("videothresh",adpThres)
    # cv2.imshow("videomedian",adpThres)
    # cv2.imshow("videoDialet",imgDialet)
    cv2.waitKey(1)