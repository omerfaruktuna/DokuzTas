import os
import time
import random

def get_player_move(tahta_):
  
  choice = input("Please choose an empty space for X. ")
  choice = int(choice)
	
  if tahta_.current_board[choice] == "*":
    tahta_.current_board[choice] = "M"
  else:
    print("Sorry, that space is not empty!")
    time.sleep(1)
    return "not empty"
    
