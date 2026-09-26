import cv2
from util import get_limits
from PIL import Image



red=[0, 0, 255] #red in BGR colors
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsvImg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit,upperLimit = get_limits(color=red)

    mask = cv2.inRange(hsvImg,lowerLimit,upperLimit)
    mask_= Image.fromarray(mask)

    boundingBox=mask_.getbbox()
    if boundingBox is not None:
        x1,y1,x2,y2=boundingBox
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)



    cv2.imshow('frame' ,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
