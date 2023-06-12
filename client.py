from communication.client.client import MountainClient
from tests.main_animation import main_graf
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

def peligro(x,y) -> bool:
    if math.sqrt((x**2)+(y**2)) > 22900:
        return True

def find_direction(diccionario,direction,contador,posible_cima,contador2) -> float:
    """
    returns the next direction
    """
    contador -= 1
    if contador == 0 or contador == 1:
        return direction
    x = diccionario[contador]["x"]
    y = diccionario[contador]["y"]
    z = diccionario[contador]["z"]
    before_x = diccionario[contador-1]["x"]
    before_y = diccionario[contador-1]["y"]
    before_z = diccionario[contador-1]["z"]
    if peligro(x,y):
        if peligro(before_x,before_y):
            return direction
        print("PELIGRO!")
        direction -= (7*math.pi/8)
        return direction
    if z < before_z and posible_cima == True:
        direction -= (math.pi/4)
    return direction

def find_speed(diccionario,speed,contador):
    contador -= 1
    if contador == 0 or contador == 1:
        return speed
    x = diccionario[contador]["x"]
    y = diccionario[contador]["y"]
    z = diccionario[contador]["z"]
    before_z = diccionario[contador-1]["z"]
    if peligro(x,y):
        speed = 30
    if z < before_z:
        speed = 20
    else:
        speed = 50
    return speed

def cima_posible(diccionario,contador,posible_cima,contador2):
    contador -= 1
    if contador == 0 or contador == 1:
        return posible_cima
    x = diccionario[contador]["x"]
    y = diccionario[contador]["y"]
    z = diccionario[contador]["z"]
    before_z = diccionario[contador-1]["z"]
    if peligro(x,y):
        posible_cima=True
        return posible_cima
    if contador2 < 20 and posible_cima == False:
        return posible_cima
    if contador > 15:
        loop_cords = (diccionario[contador-15]["x"],diccionario[contador-15]["y"],diccionario[contador-15]["z"])
        actual_cords = (diccionario[contador]["x"],diccionario[contador]["y"],diccionario[contador]["z"])
        if (abs(loop_cords[0] - actual_cords[0]) < 200) and (abs(loop_cords[1] - actual_cords[1]) < 200) and (abs(loop_cords[2] - actual_cords[2]) < 2):
            print("loop")
            posible_cima = False
            contador2 = 0
            return posible_cima
    if z > before_z and posible_cima == False:
        print("cambio")
        posible_cima = True
    return posible_cima
def main():
    global posible_cima
    posible_cima = True
    direction = (5*(math.pi)/4)
    contador = 0
    diccionario = {}
    player_info = c.get_data()[team2][climber1]
    speed = 50
    contador2 = 0
    while not c.is_over():
        contador += 1
        if posible_cima == False:
            contador2 += 1
        posible_cima = cima_posible(diccionario,contador,posible_cima,contador2)
        if posible_cima == True:
            contador2 = 0 
        direction = find_direction(diccionario,direction,contador,posible_cima,contador2)
        speed = find_speed(diccionario,speed,contador)
        c.next_iteration(team2,{climber1:{"direction":direction, 'speed':speed}})
        player_info = c.get_data()[team2][climber1]
        diccionario[contador] = player_info
        print(f"{climber1} {contador}: {diccionario[contador]}")
        time.sleep(0.1)
        main_graf(player_info)
    print(climber1,":", c.get_data()[team2][climber1])


main()