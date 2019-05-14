
def minimax(tahta_, depth, player):

  if depth == 0:
    if tahta_.is_triple("M"):
      return 0
    elif tahta_.is_triple("S"):
      return 100
    else:
      return 50

  if player == "S":
    bestValue = 0
    for move in tahta_.availableMoves():
      tahta_.makeMove(move, player)
      moveValue = minimax(tahta_, depth-1, tahta_.changePlayer(player))
      tahta_.makeMove(move, "*")
      bestValue = max(bestValue, moveValue)
    return bestValue
        
  if player == "M":
    bestValue = 100
    for move in tahta_.availableMoves():
      tahta_.makeMove(move, player)
      moveValue = minimax(tahta_, depth-1, tahta_.changePlayer(player))
      tahta_.makeMove(move, "*")
      bestValue = min(bestValue, moveValue)
    return bestValue
