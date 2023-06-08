from communication.client.client import MountainClient
import time

c= MountainClient()
c.add_team("racing",["papanatas","cebolla"])
c.add_team("sacachispas",["julian","miguel"])

c.finish_registration()

while not c.is_over():
    c.next_iteration('sacachispas',{'julian':{"direction":1, 'speed':50}})
    print(c.get_data())
    time.sleep(0.1)