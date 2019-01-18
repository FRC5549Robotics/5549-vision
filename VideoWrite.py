import cv2

cap = cv2.VideoCapture("/dev/video1")
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('output.avi', fourcc, 60, (640, 480), True)

framenum = 0

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        frame = cv2.flip(frame, 1)
        out.write(frame)

        print(framenum)
        framenum += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
