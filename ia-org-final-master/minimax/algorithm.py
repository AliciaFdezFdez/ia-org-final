from copy import deepcopy
import pygame

def minimax(position, depth, max_player, game, AIplayer, otherPlayer, alpha, beta):
    if depth == 0 or position.winner() != None:
        return position.evaluate(AIplayer), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, AIplayer, game):
            evaluation = minimax(move, depth-1, False, game, AIplayer, otherPlayer, alpha, beta)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, otherPlayer, game):
            evaluation = minimax(move, depth-1, True, game, AIplayer, otherPlayer, alpha, beta)[0]
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def simulate_move(bee, move, board, game, skip):
    if skip:
        board.remove(skip)
    board.move(bee, move[0], move[1])
    return board

def get_all_moves(board, owner, game):
    moves = []
    for bee in board.get_all_bees(owner):
        valid_moves = board.get_valid_moves(bee)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_bee = temp_board.get_piece(bee.row, bee.col)
            new_board = simulate_move(temp_bee, move, temp_board, game, skip)
            moves.append(new_board)
    return moves