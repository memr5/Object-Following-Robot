import cv2
import numpy as np

def nothing(pos):
    pass

device = cv2.VideoCapture(1)

cv2.namedWindow('ColorSpace')

cv2.createTrackbar('lh','ColorSpace',0,179,nothing)
cv2.createTrackbar('ls','ColorSpace',0,255,nothing)
cv2.createTrackbar('lv','ColorSpace',0,255,nothing)

cv2.createTrackbar('hh','ColorSpace',0,179,nothing)
cv2.createTrackbar('hs','ColorSpace',0,255,nothing)
cv2.createTrackbar('hv','ColorSpace',0,255,nothing)

while(True):

    ret, frame = device.read()
    frame = cv2.flip(frame,1)

    newFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('lh','ColorSpace')
    ls = cv2.getTrackbarPos('ls','ColorSpace')
    lv = cv2.getTrackbarPos('lv','ColorSpace')

    hh = cv2.getTrackbarPos('hh','ColorSpace')
    hs = cv2.getTrackbarPos('hs','ColorSpace')
    hv = cv2.getTrackbarPos('hv','ColorSpace')

    lower_blue = np.array([lh,ls,lv])
    high_blue = np.array([hh,hs,hv])

    mask = cv2.inRange(newFrame,lower_blue,high_blue)
    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('ColorSpace',frame)
    cv2.imshow('Result',result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

device.release()
cv2.destroyAllWindows()