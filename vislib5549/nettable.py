import threading
from networktables import NetworkTables


class ConnectTable(object):
    """
    Class facilitating connectivity to a Network Table

    Usage: Construct this object in order to establish connection and set up a network table quickly.
        Params:
        **kwargs:
            tableName: The name of a table that is to be connected to/set up.
            server: The hostname or address of a server that hosts a NetworkTable.
        Variables:
            self.Connected: Becomes true once a connection has been established.
            self.Table: The NetworkTable. Once this class has been constructed, this can be called with -
                - *ConnectTable*.Table and be issued getTable associated commands. (putBoolean, getInteger, etc.)
    """

    def __init__(self, **kwargs):

        tableName = kwargs.get('tableName', 'SmartDashboard')
        server = kwargs.get('server', '10.55.49.2')

        cond = threading.Condition()
        notified = [False]
        self.Connected = False

        def connectionListener(connected, info):
            print(info, '; Connected=%s' % connected)
            with cond:
                notified[0] = True
                cond.notify()

        NetworkTables.initialize(server=server)
        NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

        with cond:
            print("Waiting")
            if not notified[0]:
                cond.wait()
            else:
                self.Connected = True

        print("Connected!")

        self.Table = NetworkTables.getTable(tableName)
