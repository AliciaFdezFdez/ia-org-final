import random
import pygame
import sys
from extras.constants import PosicionPA, GREEN, distanciaHex, YELLOW, BLACK, WIDTH, HEIGHT, size, FPS, FONT_SIZE
from extras.gameLogic import GameLogic
from minimax.algorithm import minimax, negamax 


def draw_text(text, fnt, color, surface, pos_x, pos_y):
    """Draw text method"""
    textobj = fnt.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (pos_x, pos_y)
    surface.blit(textobj, textrect)


def get_row_col_from_mouse(pos: tuple) -> tuple:
    """
    Method that implements the logic to control the cell that you are clicking at with the mouse
    """
    pos_x, pos_y = pos
    
    col = round((pos_x - (PosicionPA + 12)) / distanciaHex)
    if col % 2 != 0:
        row = round((pos_y - (PosicionPA + 20)) / distanciaHex)
    else:
        row = round((pos_y - (PosicionPA + 44)) / distanciaHex)

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
                game()

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


def game():
    """
    Main game loop
    """

    # Initialize the game
    running = True

    # Create GameLogic object which represents the screen and coordinates needed
    game_logic = GameLogic(screen, coord_list)

    # Main loop of the game
    while running:

        # P1 is a bot
        if game_logic.turn == "P1" and mode[1] == "b":
            # With minimax selected as algorithm
            if mode[2] == 'minimax' or mode[5] == 'minimax':
                # Long command version
                if len(sys.argv) == 8:
                    value, new_board = minimax(game_logic.get_board(), int(mode[3]), True, game_logic, "P1", "P2")
                # Short command version
                else:
                    value, new_board = minimax(game_logic.get_board(), int(mode[6]), True, game_logic, "P1", "P2")
                game_logic.ai_move(new_board)
            # With negamax selected as algorithm
            elif mode[2] == 'negamax' or mode[5] == 'negamax':
                # Long command version
                if len(sys.argv) == 8:
                    value, new_board = negamax(game_logic.get_board(), int(mode[3]), True, game_logic, "P1", "P2")
                # Short command version
                else:
                    value, new_board = negamax(game_logic.get_board(), int(mode[6]), True, game_logic, "P1", "P2")
                game_logic.ai_move(new_board)

        # P2 is a bot
        if game_logic.turn == "P2" and mode[4] == "b":
            # With minimax selected as algorithm  
            if mode[5] == 'minimax':
                value, new_board = minimax(game_logic.get_board(), int(mode[6]), True, game_logic, "P2", "P1")
                game_logic.ai_move(new_board)
            # With negamax selected as algorithm
            elif mode[5] == 'negamax':
                value, new_board = negamax(game_logic.get_board(), int(mode[6]), True, game_logic, "P2", "P1")
                game_logic.ai_move(new_board)

        # Check if there is already a winner to end game
        if game_logic.winner() is not None:
            print(game_logic.winner())
            running = False
        
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
                game_logic.select(row, col)

        # Game update
        game_logic.update()

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
    
    if not (len(sys.argv) == 6 or len(sys.argv) == 8):
        print("Too many arguments for the program, you have to invoke it with the following structure:\n\npython "
              "game.py h b minimax 2 f\n\nor if you want to versus AIs\n\npython game.py b negamax 2 b minimax 2 f\n")

    else:
        
        if len(sys.argv) == 6:

            mode = [sys.argv[0], sys.argv[1], None, None, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]

        else:
            mode = sys.argv.copy()

        click = False

        # Pygame init
        pygame.init()
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        pygame.display.set_caption("HexaQueen")
        font = pygame.font.SysFont(None, FONT_SIZE)

        coord_list = []
        
        for i in range(50):
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            coord_list.append([x, y])

        main_menu()
