import cv2
import numpy as np

lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])

cam = cv2.VideoCapture("/dev/video1")

windowName = "cv2WindowDisplay"
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.resizeWindow(windowName, 640, 480)
cv2.setWindowTitle(windowName, "test")
while cam.isOpened():
    if cv2.getWindowProperty(windowName, 0) < 0:
        break
    ret, img = cam.read()
    cv2.resize(img, (340, 220))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) & 0xFF is ord('q'):
        break
    cv2.waitKey(1)
