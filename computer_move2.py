import random
from Dokuz_Tas_Tahta import Dokuz_Tas_Tahta
from minimax import minimax
from Dokuz_Tas_Tahta import Dokuz_Tas_Tahta

def make_best_move(board, depth, player):

    neutralValue = 50
    choices = []
    for move in board.availableMoves():
        board.makeMove(move, player)
        moveValue = minimax(board, depth-1, board.changePlayer(player))
        board.makeMove(move, "*")


        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    
    #print("choices: ", choices)

    if len(choices) > 0:
        return random.choice(choices)
    else:
        return random.choice(board.availableMoves())

def get_computer_move2(tahta_):

  while True:
    move = make_best_move(tahta_,4,"S")
    if tahta_.is_valid_move(move):
      return move

