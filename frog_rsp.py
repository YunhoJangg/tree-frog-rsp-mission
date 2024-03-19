import random #random 모듈 임포트

class CPU_RSP: #컴퓨터의 값 처리
  def __init__ (self):
    self.choice_list = ['가위','바위','보'] #컴퓨터가 낼 세 개의 값의 리스트 설정
  
  def choice (self):
    computer_choice = random.choice(self.choice_list) #랜덤으로 위의 리스트에 있는 값 세 개 중 하나 선택
    return computer_choice #고른 값 반환

class Player_RSP: #플레이어의 값 처리
  def __init__ (self):
    self.choice_list = ['가위','바위','보'] #플레이어가 낼 세 개의 값의 리스트 설정

  def choice (self):
    player_choice = random.choice(self.choice_list) #랜덤으로 위의 리스트에 있는 값 세 개 중 하나 선택
    return player_choice #고른 값 반환

class Main: #본 게임
  def __init__ (self):
    print("청개구리 가위, 바위, 보를 시작합니다.")
    cpu = CPU_RSP()
    player = Player_RSP()
