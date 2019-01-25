import numpy as np
import cv2
import timeit

cap = cv2.VideoCapture("/home/nvidia/PycharmProjects/OpenCV/5549-vision/output.avi")
start = timeit.default_timer()
while cap.isOpened():
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        cv2.waitKey(44)
    else:
        break

end = timeit.default_timer()
print("Playback Time:" + str(end - start))
cap.release()
cv2.destroyAllWindows()

