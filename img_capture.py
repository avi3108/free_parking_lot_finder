import cv2 
import pickle

try:
    with open("carparkpos","rb") as f:
        pos = pickle.load(f)
except:
    pos = []

weidth , height = 107, 48 

def mouseClick(events , x, y, flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        pos.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos1 in enumerate( pos):
            x1 , y1 = pos1
            if x1<x<x1+weidth and y1<y<y1+height:
                pos.pop(i)
    with open("carparkpos","wb") as f:
        pickle.dump(pos,f)

while True:
    img = cv2.imread("video/carParkImg.png")
    for pos1 in pos:
        cv2.rectangle(img,pos1,(pos1[0] + weidth, pos1[1] + height),(255,0,255),2)
        print("first")

    print("second")
    cv2.imshow("Myimage",img)
    cv2.setMouseCallback("Myimage",mouseClick)
    cv2.waitKey(1)