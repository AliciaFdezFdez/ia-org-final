import random
import pygame
import sys
from extras.constants import PosicionPA, ROWS, GREEN, distanciaHex, COLS, YELLOW, WHITE, BLACK, WIDTH, HEIGHT, size
from extras.board import Board
from extras.gameLogic import GameLogic
from minimax.algorithm import minimax 

pygame.init()

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Hexabee")
# icono = pygame.image.load("sprites/bee.png")
# pygame.display.set_icon(icono)

font = pygame.font.SysFont(None, 30)
# bee = pygame.image.load("sprites/bee.png")

coord_list = []
for i in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    coord_list.append([x, y])


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False

board = Board()

def main_menu():
    while True:
        screen.fill(GREEN)
        draw_text('Menú de inicio', font, BLACK, screen, 190, 50)

        mx, my = pygame.mouse.get_pos()

        boton1 = pygame.Rect(110, 200, 300, 50)
        boton2 = pygame.Rect(110, 300, 300, 50)
        if boton1.collidepoint((mx, my)):
            if click:
                game()
        if boton2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, YELLOW, boton1)
        draw_text('Jugar', font, BLACK, screen, 230, 215)
        pygame.draw.rect(screen, YELLOW, boton2)
        draw_text('Créditos', font, BLACK, screen, 220, 315)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        clock.tick(30)

def get_row_col_from_mouse(pos):
    x, y = pos
    
    # Esto es para que al pulsar sepa que casilla es la que esta pulsando y actue en consecuencia
    col=round((x-(PosicionPA + 12))/distanciaHex)
    if col % 2 != 0:
        row = round((y -(PosicionPA + 20))/ distanciaHex)
    else:
        row = round((y -(PosicionPA + 44))/ distanciaHex)

    return row, col

def game():
    running = True
    # bee1 = pygame.image.load("sprites/bee.png")
    # bee1 = pygame.image.load("sprites/bee.png")
    # bee1 = pygame.image.load("sprites/bee.png")

    game = GameLogic(screen,coord_list)

    
    while running:
        alpha = float('-inf')
        beta = float('inf')

        # if game.turn == "P2":
        #     value, new_board = minimax(game.get_board(), 1, True, game, "P2", "P1", alpha, beta)
        #     game.ai_move(new_board)
        
       
        if game.turn == "P1":
            value, new_board = minimax(game.get_board(), 4, True, game, "P1", "P2", alpha, beta)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            running = False

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
        pygame.display.flip()
        clock.tick(30)


def options():
    running = True
    while running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(GREEN)

        draw_text('Alumnos:', font, BLACK, screen, 210, 50)
        draw_text('Alicia Fernández Fernández', font, BLACK, screen, 120, 160)
        draw_text('Esteban Sánchez González', font, BLACK, screen, 125, 200)
        draw_text('Javier Chico García', font, BLACK, screen, 150, 240)
        draw_text('Jorge De la Cruz Luiña', font, BLACK, screen, 140, 280)

        pygame.display.flip()
        clock.tick(30)


main_menu()

