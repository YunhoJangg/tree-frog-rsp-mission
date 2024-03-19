import random #random 모듈 임포트
import time #time 모듈 임포트

class CPU_RSP: #컴퓨터의 값 처리
    def __init__(self):
        self.choice_list = ['가위', '바위', '보']  #컴퓨터가 낼 세 개의 값의 리스트 설정

    def choice(self):
        computer_choice = random.choice(self.choice_list) #랜덤으로 위의 리스트에 있는 값 세 개 중 하나 선택
        return computer_choice #고른 값 반환

class Player_RSP: #플레이어의 값 처리
    def choice(self, player_choice, computer_choice): #가위바위보 계산 함수
        print("상대는 [" + computer_choice + "] 를 냈습니다. : ")
        if player_choice == computer_choice:
            start_time = time.time()
            draw_word = input()
            stop_time = time.time()
            if (stop_time - start_time <= 3) and (draw_word == "개굴"):
                self.win_or_lose(1)
            else:
                self.win_or_lose(0)
        elif (player_choice == "가위" and computer_choice == "보") or (player_choice == "바위" and computer_choice == "가위") or (player_choice == "보" and computer_choice == "바위"):
            lose_word = input()
            if lose_word == "졌다":
                self.win_or_lose(1)
            else:
                self.win_or_lose(0)
        elif (player_choice == "보" and computer_choice == "가위") or (player_choice == "가위" and computer_choice == "바위") or (player_choice == "바위" and computer_choice == "보"):
            win_word = input()
            if win_word == "이겼다":
                self.win_or_lose(1)
            else:
                self.win_or_lose(0)

    def win_or_lose(self, detect_value): #게임 승 패 판단 함수
        if detect_value == 0:
            print("게임에 패배하셨습니다!")
        elif detect_value == 1:
            print("게임에 승리하셨습니다!")

class GAME: #본 게임
    def run(self):
        cpu = CPU_RSP()
        player = Player_RSP()
        print("청개구리 가위, 바위, 보를 시작합니다.")
        player_choice = input("가위, 바위, 보를 입력해주세요 : ")
        computer_choice = cpu.choice() #컴퓨터 값 불러오기
        player.choice(player_choice, computer_choice)
        self.retry()

    def retry(self): #다시 하기 문구 표시 함수
        player_input = input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
        if player_input == "1":
            self.run()
        elif player_input == "2":
            pass

game = GAME()
game.run() #프로그램 실행
