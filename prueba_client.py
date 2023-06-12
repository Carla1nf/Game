from communication.client.client import MountainClient
from tests.main_animation_groups import main_graf
import time
import math

class Climber:
    def __init__(self,name,direction):
        self.posible_cima = True
        self.name = name
        self.direction = direction
        self.contador = 0
        self.diccionario = {}
        self.player_info = c.get_data()[team1][name]
        self.speed = 50
        self.contador2 = 0
        
    def peligro(self,x,y) -> bool:
        if math.sqrt((x**2)+(y**2)) > 22900:
            return True

    def cima_posible(self,diccionario,contador,posible_cima,contador2):
        contador -= 1
        if contador == 0 or contador == 1:
            return posible_cima
        x = diccionario[contador]["x"]
        y = diccionario[contador]["y"]
        z = diccionario[contador]["z"]
        before_z = diccionario[contador-1]["z"]
        if self.peligro(x,y):
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

    def find_direction(self,diccionario,direction,contador,posible_cima) -> float:
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
        if self.peligro(x,y):
            if self.peligro(before_x,before_y):
                return direction
            print("PELIGRO!")
            direction -= (7*math.pi/8)
            return direction
        if z < before_z and posible_cima == True:
            direction -= (math.pi/4)
        return direction

    def find_speed(self,contador):
        contador -= 1
        if contador == 0 or contador == 1:
            return self.speed
        x = self.diccionario[contador]["x"]
        y = self.diccionario[contador]["y"]
        z = self.diccionario[contador]["z"]
        before_z = self.diccionario[contador-1]["z"]
        if self.peligro(x,y):
            self.speed = 30
        if z < before_z:
            self.speed = 20
        else:
            self.speed = 50
        return self.speed

    def main_climb(self):
        self.contador += 1
        if self.posible_cima == False:
            self.contador2 += 1
        self.posible_cima = self.cima_posible(self.diccionario,self.contador,self.posible_cima,self.contador2)
        if self.posible_cima == True:
            self.contador2 = 0 
        self.direction = self.find_direction(self.diccionario,self.direction,self.contador,self.posible_cima)
        self.speed = self.find_speed(self.contador)
        self.player_info = c.get_data()[team1][self.name]
        self.diccionario[self.contador] = self.player_info
        print(f"{self.name} {self.contador}: {self.diccionario[self.contador]}")
        return {"direction":self.direction, 'speed':self.speed}
        


team1 = "racing"
climber1 = "leo messi"
climber2 = "tete"
climber3 = "lautaro martinez"
climber4 = "copetti"
equipo = [climber1,climber2,climber3,climber4]




c = MountainClient()
c.add_team(team1,equipo)

c.finish_registration()

print(c.get_data()[team1])
climber_1 = Climber("leo messi",(math.pi))
climber_2 = Climber("tete",((5*math.pi)/4))
climber_3 = Climber("lautaro martinez",((3*math.pi)/4))
climber_4 = Climber("copetti",((math.pi)/2))
while not c.is_over():
    c.next_iteration(team1,{climber1:climber_1.main_climb(),climber2:climber_2.main_climb(),climber3:climber_3.main_climb(),climber4:climber_4.main_climb()})
    data = c.get_data()[team1]
    main_graf(data)
    time.sleep(0.1)