import cv2

cap = cv2.VideoCapture("/dev/video1")
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('output.mp4', 0x00000021, 20.0, (1280,360))

ret, frame = cap.read()

while(cap.isOpened()):
    windowName = 'test'
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowName, 1280, 360)
    cv2.moveWindow(windowName, 0, 0)
    cv2.setWindowTitle(windowName, "Canny Edge Detection")
    cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
    cv2.imshow('test', frame)
    cv2.waitKey(1)
    if ret==True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
