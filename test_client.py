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

    def cima_posible(self,contador,contador2):
        contador -= 1
        if contador == 0 or contador == 1:
            return self.posible_cima
        x = self.diccionario[contador]["x"]
        y = self.diccionario[contador]["y"]
        z = self.diccionario[contador]["z"]
        before_z = self.diccionario[contador-1]["z"]
        if math.sqrt((x**2)+(y**2)) > 22900:
            self.posible_cima=True
            return self.posible_cima
        if contador2 < 20 and self.posible_cima == False:
            return self.posible_cima
        if contador > 15:
            loop_cords = (self.diccionario[contador-15]["x"],self.diccionario[contador-15]["y"],self.diccionario[contador-15]["z"])
            actual_cords = (self.diccionario[contador]["x"],self.diccionario[contador]["y"],self.diccionario[contador]["z"])
            if (abs(loop_cords[0] - actual_cords[0]) < 200) and (abs(loop_cords[1] - actual_cords[1]) < 200) and (abs(loop_cords[2] - actual_cords[2]) < 2):
                print("loop")
                self.posible_cima = False
                contador2 = 0
                return self.posible_cima
        if z > before_z and self.posible_cima == False:
            print("cambio")
            self.posible_cima = True
        return self.posible_cima

    def find_direction(self,contador) -> float:
        """
        returns the next direction
        """
        contador -= 1
        if contador == 0 or contador == 1:
            return self.direction
        x = self.diccionario[contador]["x"]
        y = self.diccionario[contador]["y"]
        z = self.diccionario[contador]["z"]
        before_x = self.diccionario[contador-1]["x"]
        before_y = self.diccionario[contador-1]["y"]
        before_z = self.diccionario[contador-1]["z"]
        if math.sqrt((x**2)+(y**2)) > 22900:
            if math.sqrt((before_x**2)+(before_y**2)) > 22900:
                return self.direction
            print("PELIGRO!")
            self.direction -= (7*math.pi/8)
            return self.direction
        if z < before_z and self.posible_cima == True:
            self.direction -= (math.pi/4)
        return self.direction

    def find_speed(self,contador):
        contador -= 1
        if contador == 0 or contador == 1:
            return self.speed
        x = self.diccionario[contador]["x"]
        y = self.diccionario[contador]["y"]
        z = self.diccionario[contador]["z"]
        before_z = self.diccionario[contador-1]["z"]
        if math.sqrt((x**2)+(y**2)) > 22900:
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
        self.posible_cima = self.cima_posible(self.contador,self.contador2)
        if self.posible_cima == True:
            self.contador2 = 0 
        self.direction = self.find_direction(self.contador)
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