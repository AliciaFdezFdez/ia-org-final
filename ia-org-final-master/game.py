import random
import pygame
import sys
from extras.constants import PosicionPA, ROWS, GREEN, distanciaHex, COLS, YELLOW, WHITE, BLACK, WIDTH, HEIGHT, size
from extras.board import Board

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

    if y in range(177, 350) and x in range(110, 134):
        col = 0
        l=list(range(177, 350, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1

    if y in range(154, 370) and x in range(110+44*1, 134+44*1):
        col = 1
        l=list(range(154, 370, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1
    
    if y in range(133, 394) and x in range(110+44*2, 134+44*2):
        col = 2
        l=list(range(133, 394, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1
    
    if y in range(110, 414) and x in range(110+44*3, 134+44*3):
        col = 3
        l=list(range(154, 370, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1

    if y in range(133, 394) and x in range(110+44*4, 134+44*4):
        col = 4
        l=list(range(154, 370, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1
    
    if y in range(154, 370) and x in range(110+44*5, 134+44*5):
        col = 5
        l=list(range(154, 370, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1
    
    if y in range(177, 350) and x in range(110+44*6, 134+44*6):
        col = 6
        l=list(range(154, 370, 44))
        for i in range(1, len(l)):
            if y < l[i]:
                row = i-1
                break
            else:
                row = len(l)-1

    print (row, col)
    return row, col

def game():
    running = True
    # bee1 = pygame.image.load("sprites/bee.png")
    # bee1 = pygame.image.load("sprites/bee.png")
    # bee1 = pygame.image.load("sprites/bee.png")


    while running:
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
                bee = board.get_piece(row, col)
                board.move(bee, 3, 3)

        board.draw(screen,coord_list)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


def options():
    running = True
    while running:
        for event in pygame.event.get():
            print(event)
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

