import pygame
from .board import Board
from .constants import PosicionPA, distanciaHex, WHITE


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
        """
        Returns the position of a row-col pair
        """
        x = PosicionPA + 12 + col * distanciaHex
        if col % 2 != 0:
            y = PosicionPA + 20 + row * distanciaHex
        else:
            y = PosicionPA + 44 + row * distanciaHex
        return x, y
    
    def draw_valid_moves(self, moves):
        """
        Draw valid moves in the board with white dots
        """
        for move in moves:
            row, col = move
            x, y = self.calc_pos(row, col)
            pygame.draw.circle(self.screen, WHITE, (x, y), 6)

    def change_turn(self):
        """
        Swap turns between player when its called
        """
        self.valid_moves = {}
        if self.turn == "P1":
            self.turn = "P2"
        else:
            self.turn = "P1"

    def winner(self):
        """
        Return the winner
        """
        return self.board.winner()
    
    def get_board(self):
        """
        Return the current board
        """
        return self.board
    
    def ai_move(self, board):
        """
        Update board after AI move
        """
        self.board = board
        self.change_turn()