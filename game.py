import random
import pygame
import sys

pygame.init()

#Colores
GREEN = (145, 210, 144)
YELLOW = (255, 237, 81)
WHITE = (181, 225, 174)
BLACK = (0, 0, 0)

#Pantalla
WIDTH = 520
HEIGHT = 540
size = (WIDTH, HEIGHT)
COLS = 7
ROWS = 7

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Hexabee")
icono = pygame.image.load("sprites/bee.png")
pygame.display.set_icon(icono)

font = pygame.font.SysFont(None, 30)
bee = pygame.image.load("sprites/bee.png")

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


def main_menu():
    while True:
        screen.fill(GREEN)
        draw_text('Menú de inicio', font, BLACK, screen, 180, 50)

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
        pygame.draw.rect(screen, YELLOW, boton2)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        clock.tick(30)


def game():
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
        for z in coord_list:
            pygame.draw.circle(screen, WHITE, z, 2)
            z[1] += 1
            if z[1] > HEIGHT:
                z[1] = 0

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if (i == 0 and j not in range(1, 5)) or (i == 1 and j not in range(1, 6)) or (
                        i == 2 and j not in range(0, 6)) or (i == 4 and j not in range(0, 6)) or (
                        i == 5 and j not in range(1, 6)) or (i == 6 and j not in range(1, 5)):
                    pass

                else:
                    if i % 2 != 0:
                        pygame.draw.polygon(screen, YELLOW, [(110 + i * 44, 110 + j * 48), (134 + i * 44, 110 + j * 48),
                                                             (146 + i * 44, 130 + j * 48), (134 + i * 44, 150 + j * 48),
                                                             (110 + i * 44, 150 + j * 48), (98 + i * 44, 130 + j * 48)])
                    if i % 2 == 0:
                        pygame.draw.polygon(screen, YELLOW, [(110 + i * 44, 134 + j * 48), (134 + i * 44, 134 + j * 48),
                                                             (146 + i * 44, 154 + j * 48), (134 + i * 44, 174 + j * 48),
                                                             (110 + i * 44, 174 + j * 48), (98 + i * 44, 154 + j * 48)])

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
        pygame.display.flip()
        clock.tick(30)


main_menu()

