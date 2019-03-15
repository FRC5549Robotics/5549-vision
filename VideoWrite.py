import cv2
import timeit
from AutoVideo import AutoVideo
import networktables
import cscore
import sys

totaltime = timeit.default_timer()

file = open("/home/nvidia/5549/PycharmProjects/OpenCV/5549-vision/num", "r")
num = file.readline()

cap = cv2.VideoCapture("/dev/video1")
fourcc = cv2.VideoWriter_fourcc(*'X264')

videoname = '/media/nvidia/2AD3543917EA5C81/Test Videos/video' + num + '.avi'
out = cv2.VideoWriter(videoname, fourcc, 30, (640, 480), True)

AutoVideo.videoNum()

framenum = 0

# Video Stream

start = timeit.default_timer()

networktables.NetworkTables.initialize(server='10.99.91.2')
table_instance = networktables.NetworkTables.getTable('SmartDashboard')

file = open("/home/nvidia/TX2-Stat.txt", "w+")

table_instance.putNumber("TX2Num", 2)

status = False

toggle = table_instance.getString("TX2State", 'Not Found')

if toggle == 'Disable':
    status = False
elif toggle == 'Enable':
    status = True

while status is False:
    toggle = table_instance.getString("TX2State", 'Not Found')
    if toggle == 'Enable':
        status = True
        toggle = 'Enable'
        break

if toggle is 'Enable':
    print("Recording")
    while True:
        file.write("Enabled successfully")
        ret, frame = cap.read()
        if ret is True:
            cv2.imshow('frame', frame)
            out.write(frame)
            print(framenum)
            framenum += 1
        toggle = table_instance.getString("TX2State", 'Not Found')
        print(toggle)
        if toggle == 'Disable':
            cap.release()
            out.release()
            break

end = timeit.default_timer()
file.write("Total Execution Time: " + str(end-totaltime))
file.write("Recording Time: " + str(end-start))
print(framenum)
