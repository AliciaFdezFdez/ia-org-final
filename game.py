import random
import pygame
import sys

pygame.init()

GREEN = (145, 210, 144)
YELLOW = (255, 237, 81)
WHITE = (181, 225, 174)
size = (520, 540)

alto = 7
ancho = 7

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coord_list = []
for i in range(50):
    x = random.randint(0, 520)
    y = random.randint(0, 540)
    coord_list.append([x, y])

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(GREEN)
    for z in coord_list:
        pygame.draw.circle(screen, WHITE, z, 2)
        z[1] += 1
        if z[1] > 540:
            z[1] = 0

    for i in range(0, alto):
        for j in range(0, ancho):
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
