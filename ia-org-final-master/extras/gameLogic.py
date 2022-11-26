import pygame
from .board import Board
from .constants import PosicionPA, ROWS, GREEN, distanciaHex, COLS, WHITE


class GameLogic:

    def __init__(self, screen, coord_list):
        self._init()
        self.screen = screen
        self.coord_list = coord_list
        self.board=Board()
    
    def update(self):
        self.board.draw(self.screen,self.coord_list)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = "P1"
        self.valid_moves = {}

    def reset(self):
        self._init()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        bee = self.board.get_piece(row, col)
        if bee != 0 and bee.owner == self.turn:
            self.selected = bee
            self.valid_moves = self.board.get_valid_moves(bee)
            return True
            
        return False

    def _move(self, row, col):
        cell = self.board.get_piece(row, col)
        if self.selected and cell !=1 and (row, col) in self.valid_moves:
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False

        return True
    
    def calc_pos(self, row, col):
        x = PosicionPA + 12 + col * distanciaHex
        if col % 2 != 0:
            y = PosicionPA + 20 + row * distanciaHex
        else:
            y = PosicionPA + 44 + row * distanciaHex
        return x, y
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            x, y = self.calc_pos(row, col)
            pygame.draw.circle(self.screen, WHITE, (x, y), 6)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == "P1":
            self.turn = "P2"
            # print("Ahora es turno del jugador 2")
        else:
            self.turn = "P1"
            # print("Ahora es turno del jugador 1")

    def winner(self):
        return self.board.winner()
    
    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        self.board = board
        self.change_turn()