from communication.client.client import MountainClient
import time
import math

team2 = "sacachipas"
climber1 = "julian"
c= MountainClient()
c.add_team("racing",["papanatas","cebolla"])
c.add_team(team2,[climber1,"miguel"])

c.finish_registration()

def find_direction(diccionario,direction,contador) -> float:
    """
    returns the next direction
    """
    contador -= 1
    if contador == 0 or contador == 1:
        return direction
    z = diccionario[contador]["z"]
    beforez = diccionario[contador-1]["z"]
    if z < beforez:
        direction -= (math.pi/64)
    print(direction)
    return direction

direction = ((5*math.pi)/4)
contador = 0
diccionario = {}
player_info = c.get_data()[team2][climber1]
while not c.is_over():
    contador += 1
    direction = find_direction(diccionario,direction,contador)
    c.next_iteration(team2,{climber1:{"direction":direction, 'speed':50}})
    player_info = c.get_data()[team2][climber1]
    diccionario[contador] = player_info
    print(diccionario[contador])
    time.sleep(0.1)