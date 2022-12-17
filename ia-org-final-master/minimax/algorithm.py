from copy import deepcopy
import pygame
import random
import sys

WIDTH = 520
HEIGHT = 540


def minimax(position, depth, max_player, game, ai_player, other_player):
    """
    Minimax complete algorithm, it receives:
        - position: the board with all the details of pieces
        - depth: how many positions to consider 
        - max_player: true if we are looking to maximize the score
    """
    # If there is no depth or a winner we don't need to evaluate more
    if depth == 0 or position.winner() is not None:
        return position.evaluate(ai_player), position
    
    # If there is a max_player we are going to maximize
    if max_player:
        # With no evaluations we set it to the worst case
        max_eval = float('-inf')

        # Store the best move we can make
        best_move = None

        # Iterate to all moves that player can do
        for move in get_all_moves(position, ai_player, game):
            # Recursive call to calculate the evaluation
            evaluation = minimax(move, depth - 1, False, game, ai_player, other_player)[0]
            # Update the max evaluation
            max_eval = max(max_eval, evaluation)
            # If the current max eval is equal to the last evaluation, save the move as best move
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move

    else:
        # With no evaluations we set it to the worst case
        min_eval = float('inf')
        
        # Store the best move we can make
        best_move = None
        # Iterate to all moves that player can do
        for move in get_all_moves(position, other_player, game):
            # Recursive call to calculate the evaluation
            evaluation = minimax(move, depth - 1, True, game, ai_player, other_player)[0]
            # Update the min evaluation
            min_eval = min(min_eval, evaluation)
            # If the current max eval is equal to the last evaluation, save the move as best move
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move


def negamax(position, depth, max_player, game, ai_player, other_player):
    """
    Negamax complete algorithm
    """
    # If there is no depth or a winner we don't need to evaluate more
    if depth == 0 or position.winner() is not None:
        return position.evaluate(ai_player), position

    # With no evaluations we set it to the worst case
    best_value = -float("inf")

    # Store the best move we can make
    best_move = None

    # If the player is the AI player, we are going to maximize
    if max_player:
        # Iterate to all moves that player can do
        for move in get_all_moves(position, ai_player, game):
            # Recursive call to calculate the evaluation
            evaluation = negamax(move, depth - 1, False, game, ai_player, other_player)[0]
            if evaluation != 0:
                neg_ev = -evaluation
            else:
                neg_ev = evaluation
        
            best_value = max(best_value, neg_ev)
            if best_value == -evaluation:
                best_move = move
    # If the player is the other player, we are going to minimize
    else:
        for move in get_all_moves(position, other_player, game):
            evaluation = negamax(move, depth - 1, True, game, ai_player, other_player)[0]
            if evaluation != 0:
                neg_ev = -evaluation
            else:
                neg_ev = evaluation
    
            best_value = max(best_value, neg_ev)

            if best_value == -evaluation:
                best_move = move

    return best_value, best_move


def simulate_move(bee, move, board, skip):
    """
    Simulate a move a return the board after that move
    """
    if skip:
        board.remove(skip)
    board.move(bee, move[0], move[1])

    return board


def get_all_moves(board, owner, game):
    """
    Return all the posible moves that a player can do in a given game state
    """

    # List that represents all the list [board, piece] in which board is the new board after moving that piece
    moves = []

    # Iterate through all the pieces of the owner
    for bee in board.get_all_bees(owner):
        # Get the valid moves of the board
        valid_moves = board.get_valid_moves(bee)

        # move: position of the move -> (row,col) skip: pieces that are eliminated in that process -> [pieces]
        for move, skip in valid_moves.items():
            # Draw the moves that the AI is calculating
            if (len(sys.argv) == 9 and sys.argv[7] == "t") or (len(sys.argv) == 6 and sys.argv[5] == "t"):
                draw_moves(game, board, bee)
            # Deepcopy board to simulate move
            temp_board = deepcopy(board)
            # Auxiliar bee/piece
            temp_bee = temp_board.get_piece(bee.row, bee.col)
            # Simulate the move with auxiliar variables
            new_board = simulate_move(temp_bee, move, temp_board, skip)
            # Add the board after the simulated move
            moves.append(new_board)
    
    random.shuffle(moves)
    return moves


def draw_moves(game, board, piece):
    """
    Draw the moves that the AI is calculating
    """
    valid_moves = board.get_valid_moves(piece)
    coord_list = []
    
    for i in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        coord_list.append([x, y])
    
    board.draw(game.screen, coord_list)
    pygame.draw.circle(game.screen, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    
    pygame.time.delay(100)
