import numpy as np
import cv2
import timeit

class CamLib(object):
    class PlatformType:
        USB_CAM_LINUX = 1
        USB_CAM_WIN = 2
        JETSON_TX2_INT = 3

    @staticmethod
    def __init__(self):
        self.FrameCount = 0


    @staticmethod
    def cv_video_source(platform):
        """Gets a camera/video source.
        Args:
            platform: A PlatformType or a custom camera string.
        Returns:
            A VideoCapture object.
        """

        global camSrc
        camSrc = 0

        if platform is 1:

            try:
                camSrc = cv2.VideoCapture("/dev/video1")

            except:
                raise ("Error, Video source not found [USB_CAM_LINUX]")

        elif platform is 2:

            try:
                camSrc = cv2.VideoCapture(0)

            except:
                raise ("Error, Video source not found [USB_CAM_WIN]")

        elif platform is 3:

            try:
                camSrc = cv2.VideoCapture(
                    "nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)I420 ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")

            except:
                raise ("Error, Video source not found [JETSON_TX2_INT]")

        else:

            try:
                camSrc = cv2.VideoCapture(platform)

            except:
                raise ("Error, Video source not found [Custom Input]")

        return camSrc

    @staticmethod
    def cv_display_source(self, videosrc, width, height, title):
        """Displays a cv2.VideoCapture to a window.
        Args:
            videosrc: A VideoCapture object.
            width: Width of video.
            height: Height of video.
            title: Title of window.
            kwarg - keyExit: Value ID of keyboard key. If this value is True then the default key will be 'q'.
        Returns:
            A video feed from the VideoCapture in a new window.
        """
        if type(videosrc) is not cv2.VideoCapture:
            raise ("Error, object provided is not cv2.VideoCapture object")

        windowName = "cv2WindowDisplay"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(windowName, width, height)
        cv2.setWindowTitle(windowName, title)

        while videosrc.isOpened():

            if cv2.getWindowProperty(windowName, 0) < 0:
                break
            ret, frame = videosrc.read()
            cv2.imshow(windowName, frame)
            self.FrameCount += 1
            if cv2.waitKey(1) & 0xFF is ord('q'):
                break

            cv2.waitKey(1)

    @staticmethod
    def cv_write_video_stream(self, videosrc, width, height, videoname, keyexit):
        """Displays a cv2.VideoCapture to a window.
                Args:
                    videosrc: A VideoCapture object.
                    width: Video width.
                    height: Video height.
                    videoname: Name of video file to be output.
                    keyexit: Value ID of keyboard key.
                Returns:
                    No values, runs stream to file until key is pressed.
        """
        totaltime = timeit.default_timer()

        cap = cv2.VideoCapture(str(videosrc))
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter('%s.avi' % videoname, fourcc, 30, (width, height), True)

        self.FrameCount = 0

        keyexit = keyexit

        if keyexit is True:
            keyexit = 'q'

        start = timeit.default_timer()
        while True:
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('frame', frame)
                out.write(frame)
                global framecount
                print(framecount)
                framecount += 1
                if cv2.waitKey(1) & 0xFF == ord(keyexit):
                    cap.release()
                    out.release()
                    cv2.destroyAllWindows()
                    break
            else:
                break

        end = timeit.default_timer()
        print("Total Execution Time: " + str(end - totaltime))
        print("Recording Time: " + str(end - start))

    @staticmethod
    def cv_read_video(self, path):
        """Displays a cv recorded video to a window.
                Args:
                    path: Path to video file to be read (must be string)
            Returns:
                    No values, plays until end of file unless "q" is hit by user
        """
        cap = cv2.VideoCapture(path)
        start = timeit.default_timer()
        while cap.isOpened():
            ret, frame = cap.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if ret is True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame', gray)
                self.FrameCount += 1
                cv2.waitKey(22)
            else:
                break

        end = timeit.default_timer()
        print("Playback Time:" + str(end - start))
        cap.release()
        cv2.destroyAllWindows()

    def getFrames(self):
        return self.FrameCount
