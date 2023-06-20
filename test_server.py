
from communication.server.server import MountainServer
import random
from communication.server.mountain.ackley_mountain import AckleyMountain
from communication.server.mountain.easom_mountain import EasomMountain
from communication.server.mountain.easy_mountain import EasyMountain
from communication.server.mountain.mccormick_mountain import McCormickMountain
from communication.server.mountain.mishra_mountain import MishraBirdMountain
from communication.server.mountain.rastrigin_mountain import RastriginMountain
from communication.server.mountain.sinosidal_mountain import SinosidalMountain

montanas = [AckleyMountain,EasomMountain,EasyMountain,McCormickMountain,MishraBirdMountain,RastriginMountain,SinosidalMountain]
num = random.randint(0,6)
m= montanas[0](50,23000)
s= MountainServer(m, (14000,14000),50)
s.start()