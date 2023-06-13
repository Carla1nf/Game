
from communication.server.server import MountainServer

from communication.server.mountain.mishra_mountain import MishraBirdMountain

m= MishraBirdMountain(50,23000)
s= MountainServer(m, (14000,14000),50)
s.start()