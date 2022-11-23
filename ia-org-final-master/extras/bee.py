import pygame
from .constants import PosicionPA, distanciaHex

class Bee:

    def __init__(self, row, col, color):
        self.col = col
        self.row = row
        self.color = color
        self.PosicionPA = PosicionPA
        self.distanciaHex = distanciaHex
        self.x=0
        self.y=0
        self.calc_pos()
        self.PADDING = 3

    def calc_pos(self):
        self.x = self.PosicionPA + 12 + self.col * self.distanciaHex
        if self.col % 2 != 0:
            self.y = self.PosicionPA + 20 + self.row * self.distanciaHex
        else:
            self.y = self.PosicionPA + 44 + self.row * self.distanciaHex
     
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self, screen):
        radius = 20 - self.PADDING
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
    
    def __repr__(self):
        return str(self.color)