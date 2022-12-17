import pygame
from .constants import PosicionPA, ROWS, GREEN, distanciaHex, COLS, WHITE, RED, BLUE, YE, GREEN2, HEIGHT, YELLOW, tipos, VALIDPOS
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
                        pygame.draw.polygon(screen, YE, [(PosicionPA + col * distanciaHex, PosicionPA + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + row * distanciaHex),
                                                             (PosicionPA + 36 + col * distanciaHex, PosicionPA + 20 + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + 40 + row * distanciaHex),
                                                             (PosicionPA + col * distanciaHex, PosicionPA + 40 + row * distanciaHex), (PosicionPA - 12 + col * distanciaHex, PosicionPA + 20 + row * distanciaHex)])
                    if col % 2 == 0:
                        pygame.draw.polygon(screen, YELLOW, [(PosicionPA + col * distanciaHex, PosicionPA + 24 + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + 24 + row * distanciaHex),
                                                             (PosicionPA + 36 + col * distanciaHex, PosicionPA + 44 + row * distanciaHex), (PosicionPA + 24 + col * distanciaHex, PosicionPA + 64 + row * distanciaHex),
                                                             (PosicionPA + col * distanciaHex, PosicionPA + 64 + row * distanciaHex), (PosicionPA - 12 + col * distanciaHex, PosicionPA + 44 + row * distanciaHex)])

    def evaluate(self, player):
        """
        Evaluate function that returns the difference between player bees/pieces and rival bees/pieces
        """
        if player == "P2":
            return self.player2bees - self.player1bees
        else:
            return self.player1bees - self.player2bees

    
    def get_all_bees(self, owner):
        """
        Returns all the pieces of a given owner
        """
        bees = []
        for col in self.board:
            for cell in col:
                if type(cell) != int and cell.owner == owner:
                    bees.append(cell)
        return bees

    def move(self, bee, row, col):
        """
        Move bee at certain row-col
        """
        if type(bee)!=int:
            self.board[bee.col][bee.row],  self.board[col][row] = self.board[col][row], self.board[bee.col][bee.row]
            bee.move(row, col)

    def get_piece(self, row, col):
        """
        Get piece at certain row-col
        """
        if col in range(len(self.board)) and row in range(len(self.board[col])):
            return self.board[col][row]
        return 2

    def create_board(self):
        counterP1 = self.player1bees
        counterP2 = self.player2bees
        cellsLeft = self.boardSize
        for col in range(0, COLS):
            self.board.append([])
            for row in range(0, len(ROWS)):
                if col in ROWS[row]:
                    if counterP1 > 0:
                        if counterP1 > 4:
                            bee = Bee(row, col, GREEN2, "P1")
                            self.board[col].append(bee)
                        elif counterP1 > 2 and counterP1 <= 4:
                            bee = Bee(row, col, RED, "P1")
                            self.board[col].append(bee)
                        elif counterP1 > 0 and counterP1 <= 2:
                            bee = Bee(row, col, BLUE, "P1")
                            self.board[col].append(bee)
                        counterP1 -= 1
                        cellsLeft -= 1
                    elif counterP2 > 0 and cellsLeft <= 6:
                        if counterP2 > 4:
                            bee = Bee(row, col, BLUE, "P2")
                            self.board[col].append(bee)
                        elif counterP2 > 2 and counterP2 <= 4:
                            bee = Bee(row, col, RED, "P2")
                            self.board[col].append(bee)
                        elif counterP2 > 0 and counterP2 <= 2:
                            bee = Bee(row, col, GREEN2, "P2")
                            self.board[col].append(bee)
                        counterP2 -= 1
                        cellsLeft -= 1
                    else:
                        self.board[col].append(0)
                        cellsLeft -= 1
                else:
                    self.board[col].append(1)
               
    def draw(self, screen, coord_list):
        self.draw_polygon(screen, coord_list)
        for col in range(0, COLS):
            for row in range(0, len(ROWS)):
                if col in ROWS[row]:
                    bee = self.board[col][row]
                    if bee != 0:
                        bee.draw(screen)
                        
    def get_valid_moves(self, bee):
        moves = {}
        posBee = (bee.row, bee.col)
        for futureCol in range (0, COLS):
            for futureRow in range (0, len(ROWS)):
                if self._distancia(posBee, (futureRow, futureCol)) == 1 and self.board[futureCol][futureRow]==0 and VALIDPOS[posBee]:
                    for i in VALIDPOS[posBee]:
                            if i == (futureRow, futureCol):
                                moves[(futureRow, futureCol)]=[]
                elif self._distancia(posBee, (futureRow, futureCol)) == 1 and type(self.board[futureCol][futureRow])!=int  and VALIDPOS[posBee]:
                    otherBee = self.board[futureCol][futureRow]
                    if otherBee.owner != bee.owner:
                        weakness = tipos[bee.color]
                        if otherBee.color == weakness:
                            for i in VALIDPOS[posBee]:
                                if i == (futureRow, futureCol):
                                    moves[(futureRow, futureCol)] = [otherBee]
        return moves
    
    def _distancia(self, a, b):
        return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.col][piece.row] = 0
            if piece != 0:
                if piece.owner == "P1":
                    self.player1bees -= 1
                else:
                    self.player2bees -= 1
    
    def winner(self):
        if self.player1bees + self.player2bees <= 10:
            bees = self.get_all_bees("P1")+self.get_all_bees("P2")
            colorCount = 0
            for i in range(len(bees)):
                if i == 0:
                    color = bees[i].color
                    colorCount += 1
                else:
                    if color == bees[i].color:
                        colorCount += 1
            if colorCount == len(bees):
                return "Empate"
        if self.player1bees <= 0:
            return "Gana el jugador 2"
        elif self.player2bees <= 0:
            return "Gana el jugador 1"
        
        return None 
