
from communication.server.server import MountainServer

from communication.server.mountain.mccormick_mountain import McCormickMountain

m= McCormickMountain(50,23000)
s= MountainServer(m, (14000,14000),50)
s.start()