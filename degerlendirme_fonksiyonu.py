import os
import time
import random

def basit_degerlendirme_fonksiyonu(tahta_):
  if tahta_.is_triple("M"):
    return 0
  elif tahta_.is_triple("S"):
    return 10
  else:
    return 5
