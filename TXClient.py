from vislib5549 import camlib as cl, nettable as nt, robotvisionlib as rbvl

import numpy as np
import networktables as NetworkTables


def client():
    SmartDash = nt.ConnectTable()

    while SmartDash.Connected:
        SmartDash.Table.putBoolean("tableExists", True)


if __name__ == '__main__':
    client()
