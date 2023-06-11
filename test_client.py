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
    before_z = diccionario[contador-1]["z"]
    inclinacion_x = diccionario[contador]["inclinacion_x"]
    before_inc = diccionario[contador-1]["inclinacion_x"]
    inclinacion_y = diccionario[contador]["inclinacion_y"]
    before_inc_y = diccionario[contador-1]["inclinacion_y"]
    if z < before_z:
        speed = 1
        direction -= (math.pi/4)
    elif z > 4999.9:
        speed = 1
    elif z > 4950:
        speed = 25
    else:
        speed = 50
    print(direction)
    return direction

def find_speed(diccionario,speed,contador):
    contador -= 1
    if contador == 0 or contador == 1:
        return speed
    z = diccionario[contador]["z"]
    before_z = diccionario[contador-1]["z"]
    inclinacion_x = diccionario[contador]["inclinacion_x"]
    before_inc = diccionario[contador-1]["inclinacion_x"]
    inclinacion_y = diccionario[contador]["inclinacion_y"]
    before_inc_y = diccionario[contador-1]["inclinacion_y"]
    if z < before_z:
        speed = 1
    elif z > 4999.9:
        speed = 1
    elif z > 4950:
        speed = 25
    else:
        speed = 50
    print(f"speed: {speed}")
    return speed

direction = ((5*math.pi)/4)
contador = 0
diccionario = {}
player_info = c.get_data()[team2][climber1]
speed = 50
while not c.is_over():
    contador += 1
    direction = find_direction(diccionario,direction,contador)
    speed = find_speed(diccionario,speed,contador)
    c.next_iteration(team2,{climber1:{"direction":direction, 'speed':speed}})
    player_info = c.get_data()[team2][climber1]
    diccionario[contador] = player_info
    print(diccionario[contador])
    time.sleep(0.1)
print(c.get_data()[team2][climber1])