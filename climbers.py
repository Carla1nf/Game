import math

def avance_x(dir,speed):
    avance_x = speed * math.cos(dir)
    return avance_x

def avance_y(dir,speed):
    avance_y = speed * math.sin(dir)
    return avance_y

def is_it_secure(x_act,y_act,direction,speed,radio = 23000):
    if math.sqrt((x_act + avance_x(direction,speed))**2 + (y_act + avance_y(direction,speed))** 2) < (radio-50):
        return direction
    else:
        return is_it_secure(x_act,y_act,direction + 1, speed - 1)
    
def escalar(inclinacion_y,inclinacion_x):
    angulo_pendiente = math.atan2(inclinacion_y, inclinacion_x)
    return angulo_pendiente

def angulo(actual,direccion):
    direction = math.atan2(direccion[1] - actual[1], direccion[0] - actual[0])
    return direction

cima = (0,0)

class Climber:
    def __init__(self,name,direction,color,algoritmo):
        self.color = color
        self.posible_cima = True
        self.name = name
        self.direction = direction
        self.algoritmo = algoritmo
        self.contador = 0
        self.diccionario = {}
        self.player_info = ""
        self.speed = 50
        self.contador2 = 0
        self.point_color = "black"
        
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
        if contador > 10 and self.algoritmo == 1:
            loop_cords = (self.diccionario[contador-7]["x"],self.diccionario[contador-7]["y"],self.diccionario[contador-7]["z"])
            actual_cords = (self.diccionario[contador]["x"],self.diccionario[contador]["y"],self.diccionario[contador]["z"])
            if (abs(loop_cords[0] - actual_cords[0]) < 100) and (abs(loop_cords[1] - actual_cords[1]) < 100) and (abs(loop_cords[2] - actual_cords[2]) < 2):
                self.posible_cima = False
                contador2 = 0
                return self.posible_cima
        if contador > 15 and self.algoritmo == 2:
            loop_cords = (self.diccionario[contador-15]["x"],self.diccionario[contador-15]["y"],self.diccionario[contador-15]["z"])
            actual_cords = (self.diccionario[contador]["x"],self.diccionario[contador]["y"],self.diccionario[contador]["z"])
            if (abs(loop_cords[0] - actual_cords[0]) < 200) and (abs(loop_cords[1] - actual_cords[1]) < 200) and (abs(loop_cords[2] - actual_cords[2]) < 2):
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
        if contador == 0 or contador == 1 or self.posible_cima == False:
            return self.direction
        x = self.diccionario[contador]["x"]
        y = self.diccionario[contador]["y"]
        z = self.diccionario[contador]["z"]
        before_x = self.diccionario[contador-1]["x"]
        before_y = self.diccionario[contador-1]["y"]
        before_z = self.diccionario[contador-1]["z"]
        if (self.posible_cima == True or math.sqrt((x**2)+(y**2)) > 22750) and self.algoritmo == 1:
            self.direction = is_it_secure(x,y,escalar(self.diccionario[contador]["inclinacion_y"],self.diccionario[contador]["inclinacion_x"]),self.speed)
        elif self.posible_cima == True and self.algoritmo == 2 and z < before_z:
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
        else:
            self.speed = 50
        return self.speed

    def main_climb(self,team1,c):
        global cima
        datos = []
        self.contador += 1
        self.player_info = c.get_data()[team1][self.name]
        self.diccionario[self.contador] = self.player_info
        x = self.diccionario[self.contador]["x"]
        y = self.diccionario[self.contador]["y"]
        z = self.diccionario[self.contador]["z"]
        datos.append(x)
        datos.append(y)
        datos.append(z)
        print(f"{self.name} {self.contador}: x: {datos[0]:.02f}\t y: {datos[1]:.02f}\t z: {datos[2]:.02f}\t cima: {self.player_info['cima']}\n")
        for team in c.get_data():
            for player in c.get_data()[team]:
                if c.get_data()[team][player]["cima"] == True:
                    cima = (c.get_data()[team][player]["x"],c.get_data()[team][player]["y"])
                    print(cima)
        if self.algoritmo == 3 or math.sqrt((x**2)+(y**2)) > 22900 or cima != (0,0):
            self.algoritmo == 3
            actual = (x,y)
            if abs(actual[0] - cima[0]) < 50 and abs(actual[1] - cima[1]) < 50:
                self.speed = 15
                if abs(actual[0] - cima[0]) < 15 and abs(actual[1] - cima[1]) < 15:
                    self.algoritmo = 1
            print(self.speed)
            return {"direction":angulo(actual,cima), 'speed':self.speed}
        if self.algoritmo == 2 or self.algoritmo == 5:
            if self.algoritmo == 2:
                punto = (3500,15000)
            else:
                punto = (15000,3500)
            actual = (x,y)
            if abs(actual[0] - punto[0]) < 15 and abs(actual[1] - punto[1]) < 15:
                self.algoritmo = 1
            print(self.speed)
            return {"direction":angulo(actual,punto), 'speed':self.speed}
        if self.contador > 2 and math.sqrt((x**2)+(y**2)) > 22750:
                self.algoritmo = 1
        if ((self.algoritmo == 5 and self.contador < 150) or (self.algoritmo == 2 and self.contador < 250)) and ((math.sqrt((x**2)+(y**2)) < 22750)):
            self.player_info = c.get_data()[team1][self.name]
            self.diccionario[self.contador] = self.player_info
            return {"direction":self.direction, 'speed':self.speed}
        if self.algoritmo == 3 or self.algoritmo == 4:
            self.algoritmo = 1
        if self.posible_cima == False:
            self.contador2 += 1
        self.posible_cima = self.cima_posible(self.contador,self.contador2)
        if self.posible_cima == True:
            self.contador2 = 0 
        self.direction = self.find_direction(self.contador)
        self.speed = self.find_speed(self.contador)
        return {"direction":self.direction, 'speed':self.speed}