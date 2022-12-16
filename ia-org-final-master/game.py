import random
import pygame
import sys
from extras.constants import PosicionPA, GREEN, distanciaHex, YELLOW, BLACK, WIDTH, HEIGHT, size, FPS, FONT_SIZE
from extras.gameLogic import GameLogic
from minimax.algorithm import minimax 

click = False

def draw_text(text, font, color, surface, x, y):
    "Draw text method"
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def get_row_col_from_mouse(pos:tuple)->tuple:
    """
    Method that implments the logic to control the cell that you are clicking at with the mouse 
    """
    x, y = pos
    
    col=round((x-(PosicionPA + 12))/distanciaHex)
    if col % 2 != 0:
        row = round((y -(PosicionPA + 20))/ distanciaHex)
    else:
        row = round((y -(PosicionPA + 44))/ distanciaHex)

    return row, col

def main_menu():
    """
    Main menu of the game
    """
    while True:

        # Background and graphics of menu
        screen.fill(GREEN)
        draw_text('Menú de inicio', font, BLACK, screen, 190, 50)
        boton_jugar = pygame.Rect(110, 200, 300, 50)
        boton_creditos = pygame.Rect(110, 300, 300, 50)

        # Obtain mouse coordinates
        mx, my = pygame.mouse.get_pos()

        # If boton_jugar is clicked, initialize the game
        if boton_jugar.collidepoint((mx, my)):
            if click:
                game(sys.argv)

        # If boton_creditos is clicked, initialize the credits
        if boton_creditos.collidepoint((mx, my)):
            if click:
                options()

        # More graphics and visual elements
        pygame.draw.rect(screen, YELLOW, boton_jugar)
        draw_text('Jugar', font, BLACK, screen, 230, 215)
        pygame.draw.rect(screen, YELLOW, boton_creditos)
        draw_text('Créditos', font, BLACK, screen, 220, 315)

        # Close the game logic
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Pygame display and tickrate
        pygame.display.flip()
        clock.tick(FPS)


def game(mode):
    """
    Main game loop
    """

    # Initialize the game
    running = True

    # Create GameLogic object which represents the screen and coordinates needed
    game = GameLogic(screen,coord_list)

    # Number of movements that are used to forecast
    DEPTH = 4
    
    # Main loop of the game
    while running:
        alpha = float('-inf')
        beta = float('inf')

        # Check if there is already a winner to end game
        if game.winner() != None:
            print(game.winner())
            running = False

        # If sys.argv[1] = b, player 1 will be a bot, if not it will be a human controlling the player
        if game.turn == "P1" and mode[1]=="b":
            value, new_board = minimax(game.get_board(), DEPTH, True, game, "P1", "P2", alpha, beta)
            game.ai_move(new_board)

        # If sys.argv[2] = b, player 2 will be a bot, if not it will be a human controlling the player
        if game.turn == "P2" and mode[2]=="b":
            value, new_board = minimax(game.get_board(), DEPTH, True, game, "P2", "P1", alpha, beta)
            game.ai_move(new_board)
        
        # Close the game logic
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

        # Game update
        game.update()

        # Pygame display and tickrate
        pygame.display.flip()
        clock.tick(FPS)

def options():
    """
    Options menu
    """
    running = True
    while running:
        # Close the game logic
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Graphic and text display
        screen.fill(GREEN)
        draw_text('Alumnos:', font, BLACK, screen, 210, 50)
        draw_text('Alicia Fernández Fernández', font, BLACK, screen, 120, 160)
        draw_text('Esteban Sánchez González', font, BLACK, screen, 125, 200)
        draw_text('Javier Chico García', font, BLACK, screen, 150, 240)
        draw_text('Jorge De la Cruz Luiña', font, BLACK, screen, 140, 280)

        # Pygame display and tickrate
        pygame.display.flip()
        clock.tick(FPS)

# Init program
if __name__ == "__main__":
    
    # Pygame init
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Hexaqueen")
    font = pygame.font.SysFont(None, FONT_SIZE)

    coord_list = []
    
    for i in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        coord_list.append([x, y])

    main_menu()

