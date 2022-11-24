import pygame
from .board import Board

class GameLogic:

    def __init__(self, screen, coord_list):
        self.screen = screen
        self.coord_list = coord_list
        self.board=Board()
    
    def update(self):
        self.board.draw(self.screen,self.coord_list)
        # self.draw_valid_moves(self.valid_moves)
        pygame.display.update()