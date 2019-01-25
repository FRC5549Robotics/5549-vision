import cv2
import timeit

totaltime = timeit.default_timer()

cap = cv2.VideoCapture("/dev/video1")
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480), True)

framenum = 1

start = timeit.default_timer()
while True:
    ret, frame = cap.read()
    print(framenum)
    framenum += 1
    if ret == True:
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break
    else:
        break

end = timeit.default_timer()
print("Total Execution Time: " + str(end-totaltime))
print("Recording Time: " + str(end-start))
