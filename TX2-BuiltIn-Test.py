import numpy as np
import cv2

cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420, "
                       "framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! "
                       "videoconvert ""! video/x-raw, format=(string)BGR ! appsink")

if cap.isOpened():
    windowName = 'test'
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowName, 1280, 720)
    cv2.moveWindow(windowName, 0, 0)
    cv2.setWindowTitle(windowName, "Test")
    while True:
        if cv2.getWindowProperty(windowName, 0 ) < 0:
            break
        ret, frame = cap.read()
        cv2.imshow('test', frame)
        cv2.waitKey(1)

cv2.destroyAllWindows()
