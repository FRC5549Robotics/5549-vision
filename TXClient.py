from vislib5549 import camlib as cl
from vislib5549 import nettable as nt
import networktables as nwt



def client():
    SmartDash = nt.ConnectTable()

    while SmartDash.Connected:
        SmartDash.Table.putBoolean("tableExists", True)
        cl.CamLib.cv_display_source("/dev/video1", 640, 480, "test")
        SmartDash.Table.putNumber('FPS', cl.CamLib.getFrames())


if __name__ == '__main__':
    client()
