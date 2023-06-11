from communication.client.client import MountainClient
import time
import math

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

class Climber:
    def __init__(self,name,direction):
        self.name = name
        self.direction = direction
        self.contador = 0
        self.diccionario = {}
        self.player_info = c.get_data()[team1][name]
        self.speed = 50

    def main_climb(self):
        self.contador += 1
        self.direction = find_direction(self.diccionario,self.direction,self.contador)
        self.speed = find_speed(self.diccionario,self.speed,self.contador)
        c.next_iteration(team1,{self.name:{"direction":self.direction, 'speed':self.speed},"tete":{"direction":self.direction, 'speed':self.speed}})
        player_info = c.get_data()[team1][self.name]
        self.diccionario[self.contador] = player_info
        print(f"{self.name}: {self.diccionario[self.contador]}")
        time.sleep(0.1)


team1 = "racing"
climber1 = "leo messi"
climber2 = "tete"
climber3 = "chango cardenas"
climber4 = "copetti"
equipo = [climber1,climber2,climber3,climber4]




c = MountainClient()
c.add_team(team1,equipo)

c.finish_registration()

print(c.get_data()[team1])
climber_1 = Climber("leo messi",(math.pi))
climber_2 = Climber("tete",((5*math.pi)/4))
while not c.is_over():
    climber_1.main_climb()
    print(c.get_data())
    climber_2.main_climb()
print(c.get_data()[team1])

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

"""
def main():
    direction = ((5*math.pi)/4)
    contador = 0
    diccionario = {}
    player_info = c.get_data()[team1][climber1]
    speed = 50
    while not c.is_over():
        contador += 1
        direction = find_direction(diccionario,direction,contador)
        speed = find_speed(diccionario,speed,contador)
        c.next_iteration(team1,{climber1:{"direction":direction, 'speed':speed}})
        player_info = c.get_data()[team1][climber1]
        diccionario[contador] = player_info
        print(f"{climber1}: {diccionario[contador]}")
        time.sleep(0.1)

main()
"""