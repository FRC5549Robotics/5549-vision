from vislib5549 import camlib as cam

source = "/dev/video1"

cam.CamLib.cv_write_video_stream(source, 640, 480, "/home/nvidia/Videos/test", keyexit=True)

