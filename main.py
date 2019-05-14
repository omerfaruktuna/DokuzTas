from Dokuz_Tas_Tahta import Dokuz_Tas_Tahta
from player_move import get_player_move
from computer_move2 import get_computer_move2
from minimax import minimax
from degerlendirme_fonksiyonu import basit_degerlendirme_fonksiyonu
import os
import time
import random

def print_header():
	print("9 Tas Game\n")

def print_guide():
  print("Playing Guide:\n")
  print(" 1"+"---------"+"2"+"---------"+"3")
  print(" |                   |")
  print(" |  "+"4"+"------"+"5"+"------"+"6"+"  |")
  print(" |  |             |  |")
  print(" |  |  "+"7"+"---"+"8"+"---"+"9"+"  |  |")
  print(" |  |  |       |  |  |")
  print("10"+" "+"11"+" "+"12"+"      "+"13"+"  "+"14"+" "+"15")
  print(" |  |  |       |  |  |")
  print(" |  |  "+"16"+"--"+"17"+"--"+"18"+" |  |")
  print(" |  |             |  |")
  print(" |  "+"19"+"-----"+"20"+"-----"+"21"+" |")
  print(" |                   |")
  print("22"+"--------"+"23"+"--------"+"24")

oyun_tahtasi= Dokuz_Tas_Tahta()
	
while True:
  os.system("clear")
  print_header()
  print_guide()
  print("\n")
  oyun_tahtasi.print_tahta()

  player_result = get_player_move(oyun_tahtasi)
  if player_result == "not empty":
    continue

  if oyun_tahtasi.is_triple("M"):
    os.system("clear")
    print_header()
    oyun_tahtasi.print_tahta()
    print("User wins! Congratulations")
    break
  
  os.system("clear")

  oyun_tahtasi.print_tahta()
	

  if oyun_tahtasi.is_board_full():
    print("Tie!")
    break
	

  choice = get_computer_move2( oyun_tahtasi)


  if oyun_tahtasi.current_board[choice] == "*":
    oyun_tahtasi.current_board[choice] = "S"
  else:
    print("Sorry, that space is not empty!")
    time.sleep(1)
		

  if oyun_tahtasi.is_triple("S"):
    os.system("clear")

    oyun_tahtasi.print_tahta()
    print("Computer wins! Congratulations")
    break
		

  if oyun_tahtasi.is_board_full():
    print("Tie!")
    break
