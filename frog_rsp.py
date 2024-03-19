import random

class CPU_RSP: #컴퓨터의 값 처리
  def __init__ (self):
    self.choice_list = ['가위','바위','보']
  
  def choice (self):
    computer_choice = random.choice(self.choice_list)
    return computer_choice
