from communication.client.client import MountainClient
import time
import math

team2 = "racing"
climber1 = "leo messi"
climber2 = "tete"
climber3 = "chango cardenas"
climber4 = "copetti"
equipo = [climber1,climber2,climber3,climber4]

c= MountainClient()
c.add_team(team2,equipo)

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
    if z < before_z:
        direction -= (math.pi/4)
    return direction

def find_speed(diccionario,speed,contador):
    contador -= 1
    if contador == 0 or contador == 1:
        return speed
    z = diccionario[contador]["z"]
    before_z = diccionario[contador-1]["z"]
    if z < before_z:
        speed = 25
    elif z > 4950:
        speed = 25
    else:
        speed = 50
    return speed

def main():
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
        print(f"{climber1}: {diccionario[contador]}")
        time.sleep(0.1)
    print(climber1,":", c.get_data()[team2][climber1])

main()