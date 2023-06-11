import pygame

pygame.init()

# Dimensiones de la pantalla
ancho_pantalla = 500
alto_pantalla = 600

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Dashboard")

# Reloj para controlar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

# Clase para manejar las piezas del Tetris
class Pieza:
    def __init__(self, forma, color):
        self.forma = forma
        self.color = color
        self.x = ancho_pantalla // 2 - len(forma[0]) // 2
        self.y = 0