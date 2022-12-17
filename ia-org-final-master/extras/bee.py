import pygame
from .constants import PosicionPA, distanciaHex, WHITE2, BLACK, BEE


class Bee:
    PADDING = 4
    OUTLINE = 3

    def __init__(self, row, col, color, owner):
        self.col = col
        self.row = row
        self.color = color
        self.PosicionPA = PosicionPA
        self.distanciaHex = distanciaHex
        self.owner = owner

        self.x = 0
        self.y = 0
        self.calc_pos()

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
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius + self.OUTLINE)
        if self.owner == "P1":
            pygame.draw.circle(screen, BLACK, (self.x, self.y), radius)
        else:
            pygame.draw.circle(screen, WHITE2, (self.x, self.y), radius)
        screen.blit(BEE, (self.x - BEE.get_width()//2, self.y - BEE.get_height()//2))

    def __repr__(self):
        return str(self.color)
