
from communication.server.server import MountainServer

from communication.server.mountain.easy_mountain import EasyMountain

m= EasyMountain(50,23000)
s= MountainServer(m, (14000,14000),50)
s.start()