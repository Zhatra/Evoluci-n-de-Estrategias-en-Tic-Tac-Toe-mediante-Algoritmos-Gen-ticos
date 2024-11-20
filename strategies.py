# strategies.py

import random

def random_strategy(game, player):
    return random.choice(game.available_moves())

def minimax_strategy(game, player):
    opponent = 'O' if player == 'X' else 'X'
    best_score = -float('inf')
    best_move = None

    for move in game.available_moves():
        game.make_move(move, player)
        score = minimax(game, False, player, opponent)
        game.make_move(move, ' ')
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax(game, is_maximizing, player, opponent):
    if game.check_winner(player):
        return 1
    elif game.check_winner(opponent):
        return -1
    elif game.is_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in game.available_moves():
            game.make_move(move, player)
            score = minimax(game, False, player, opponent)
            game.make_move(move, ' ')
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in game.available_moves():
            game.make_move(move, opponent)
            score = minimax(game, True, player, opponent)
            game.make_move(move, ' ')
            best_score = min(score, best_score)
        return best_score

def heuristic_strategy(game, player):
    # Estrategia simple que prioriza centro, esquinas y laterales
    center = 4
    corners = [0, 2, 6, 8]
    sides = [1, 3, 5, 7]
    for move in [center] + corners + sides:
        if move in game.available_moves():
            return move
    return random.choice(game.available_moves())
