import random

class Dokuz_Tas_Tahta():

  def __init__(self):
    self.current_board = ["", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]

  def print_tahta(self):
    print("Current Picture of the Board:\n")
    print(self.current_board[1]+"---------"+self.current_board[2]+"---------"+self.current_board[3])
    print("|                   |")
    print("|  "+self.current_board[4]+"------"+self.current_board[5]+"------"+self.current_board[6]+"  |")
    print("|  |             |  |")
    print("|  |  "+self.current_board[7]+"---"+self.current_board[8]+"---"+self.current_board[9]+"  |  |")
    print("|  |  |       |  |  |")
    print(self.current_board[10]+"  "+self.current_board[11]+"  "+self.current_board[12]+"       "+self.current_board[13]+"  "+self.current_board[14]+"  "+self.current_board[15])
    print("|  |  |       |  |  |")
    print("|  |  "+self.current_board[16]+"---"+self.current_board[17]+"---"+self.current_board[18]+"  |  |")
    print("|  |             |  |")
    print("|  "+self.current_board[19]+"------"+self.current_board[20]+"------"+self.current_board[21]+"  |")
    print("|                   |")
    print(self.current_board[22]+"---------"+self.current_board[23]+"---------"+self.current_board[24])
	
  def is_triple(self,player):
  	if (self.current_board[1] == player and self.current_board[2] == player and self.current_board[3] == player) or \
  		(self.current_board[4] == player and self.current_board[5] == player and self.current_board[6] == player) or \
  		(self.current_board[7] == player and self.current_board[8] == player and self.current_board[9] == player) or \
  		(self.current_board[16] == player and self.current_board[17] == player and self.current_board[18] == player) or \
  		(self.current_board[19] == player and self.current_board[20] == player and self.current_board[21] == player) or \
  		(self.current_board[22] == player and self.current_board[23] == player and self.current_board[24] == player) or \
  		(self.current_board[1] == player and self.current_board[10] == player and self.current_board[22] == player) or \
  		(self.current_board[3] == player and self.current_board[15] == player and self.current_board[24] == player) or \
      (self.current_board[4] == player and self.current_board[11] == player and self.current_board[19] == player) or \
      (self.current_board[6] == player and self.current_board[14] == player and self.current_board[21] == player) or \
      (self.current_board[7] == player and self.current_board[12] == player and self.current_board[16] == player) or \
      (self.current_board[9] == player and self.current_board[13] == player and self.current_board[18] == player)or \
      (self.current_board[2] == player and self.current_board[5] == player and self.current_board[8] == player) or \
      (self.current_board[17] == player and self.current_board[20] == player and self.current_board[23] == player) or \
      (self.current_board[1] == player and self.current_board[4] == player and self.current_board[7] == player) or \
      (self.current_board[3] == player and self.current_board[6] == player and self.current_board[9] == player) or \
      (self.current_board[16] == player and self.current_board[19] == player and self.current_board[22] == player) or \
      (self.current_board[18] == player and self.current_board[21] == player and self.current_board[24] == player) :
  		return True
  	else:
  		return False
  		
  def is_board_full(self):
  	if "*" in self.current_board:
  		return False
  	else:
  		return True

  def is_valid_move(self,move):
  	if self.current_board[move] == "*":
  		return True
  	else:
  		return False  

  def changePlayer(self,player):
    if player == "M":
        return "S"
    else:
        return "M"

  def makeMove(self, position, player):
    self.current_board[position] = player

  def availableMoves(self):
    moves = []
    for i in range(0, len(self.current_board)):
      if self.current_board[i] == "*":
        moves.append(i)
    return moves

  def get_computer_move(self, player):
    if self.current_board[5] == " ":
      return 5

    while True:
      move = random.randint(1,24)
      if self.current_board[move] == "*":
        return move
        break
        
    return 5

