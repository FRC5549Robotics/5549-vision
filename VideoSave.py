import cv2

videoFile = cv2.VideoCapture("/dev/video1")
fourcc = cv2.VideoWriter_fourcc(*'X264')
frame_width = int(videoFile.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(videoFile.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('/home/nvidia/PycharmProjects/OpenCV/output.avi', fourcc, 20.0, (frame_height, frame_width))

while videoFile.isOpened():
    ret, frame = videoFile.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    dev = "/dev/video1"
    width = frame_width
    height = frame_height
    gst_str = ('v4l2src device=/dev/video{} ! '
               'video/x-raw, width=(int){}, height=(int){}, '
               'format=(string)RGB ! '
               'videoconvert ! appsink').format(dev, width, height)
    cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

    if True:
        out.write(frame)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
         break

videoFile.release()
out.release()
cv2.destroyAllWindows()
