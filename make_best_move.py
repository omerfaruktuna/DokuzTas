import random
from minimax import minimax

from Dokuz_Tas_Tahta import Dokuz_Tas_Tahta

def make_best_move(board, depth, player):

    neutralValue = 50
    choices = []
    for move in board.availableMoves():
        board.makeMove(move, player)
        moveValue = minimax(board, depth-1, changePlayer(player))
        board.makeMove(move, "*")

        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    print("choices: ", choices)

    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.availableMoves())
        
