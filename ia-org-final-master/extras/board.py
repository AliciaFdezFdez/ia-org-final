import pygame
from .constants import PosicionPA, ROWS, GREEN, distanciaHex, COLS, WHITE, RED, BLUE, BLACK, WIDTH, HEIGHT, size, YELLOW
from .bee import Bee
    
class Board:

    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.player1bees = self.player2bees = 6

        self.boardSize=0
        for r in ROWS:
            self.boardSize += len(r)
        
        self.create_board()
    
    def draw_polygon(self, screen, coord_list):
        screen.fill(GREEN)
        for z in coord_list:
            pygame.draw.circle(screen, WHITE, z, 2)
            z[1] += 1
            if z[1] > HEIGHT:
                z[1] = 0
        for col in range(0, COLS):
            for row in range(0, len(ROWS)):
                if col in ROWS[row]:
                    if col % 2 != 0:
                        pygame.draw.polygon(screen, YELLOW, [(PosicionPA + col * distanciaHex, PosicionPA + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + row * distanciaHex),
                                                             (PosicionPA + 36 + col * distanciaHex, PosicionPA + 20 + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + 40 + row * distanciaHex),
                                                             (PosicionPA + col * distanciaHex, PosicionPA + 40 + row * distanciaHex), (PosicionPA - 12 + col * distanciaHex, PosicionPA + 20 + row * distanciaHex)])
                    if col % 2 == 0:
                        pygame.draw.polygon(screen, YELLOW, [(PosicionPA + col * distanciaHex, PosicionPA + 24 + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + 24 + row * distanciaHex),
                                                             (PosicionPA + 36 + col * distanciaHex, PosicionPA + 44 + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + 64 + row * distanciaHex),
                                                             (PosicionPA + col * distanciaHex, PosicionPA + 64 + row * distanciaHex), (PosicionPA - 12 + col * distanciaHex, PosicionPA + 44 + row * distanciaHex)])
    
    def move(self, bee, row, col):
        if self.board[col][row]==0:
            self.board[bee.row][bee.col],  self.board[row][col] = self.board[row][col], self.board[bee.row][bee.col]
            bee.move(row, col)
            print (self.board[0][3])


    def get_piece(self, row, col):
        return self.board[col][row]

    def create_board(self):
        counterP1=self.player1bees
        counterP2=self.player2bees
        cellsLeft = self.boardSize
        for col in range(0, COLS):
            self.board.append([])
            for row in range(0, len(ROWS)):
                if col in ROWS[row]:
                    if counterP1 > 0:
                        if counterP1 > 4:
                            bee = Bee(row, col, BLACK)
                            self.board[col].append(bee)
                        elif counterP1 > 2 and counterP1 <= 4:
                            bee = Bee(row, col, RED)
                            self.board[col].append(bee)
                        elif counterP1 > 0 and counterP1 <= 2:
                            bee = Bee(row, col, BLUE)
                            self.board[col].append(bee)
                        counterP1 -= 1
                        cellsLeft -= 1
                    elif counterP2 > 0 and cellsLeft <= 6:
                        if counterP2 > 4:
                            bee = Bee(row, col, BLUE)
                            self.board[col].append(bee)
                        elif counterP2 > 2 and counterP2 <= 4:
                            bee = Bee(row, col, RED)
                            self.board[col].append(bee)
                        elif counterP2 > 0 and counterP2 <= 2:
                            bee = Bee(row, col, BLACK)
                            self.board[col].append(bee)
                        counterP2 -= 1
                        cellsLeft -= 1
                    else:
                        self.board[col].append(0)
                        cellsLeft -= 1

    def draw(self, screen, coord_list):
        self.draw_polygon(screen, coord_list)
        for col in range(0, len(self.board)):
            for row in range(0, len(self.board[col])):
                    bee = self.board[col][row]
                    if bee != 0 and type(bee)!=str:
                        bee.draw(screen)
                        
                
