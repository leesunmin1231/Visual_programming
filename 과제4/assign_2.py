from random import randint
import sys

class Player: # player 정보 담은 class
    def __init__(self,name):
        self.name=name # player 이름
        self.location="START" # 현재 위치한 도시
        self.bought_city=[] # 이 플레이어가 구매한 도시
        self.money=5000 # 플레이어가 현재 지닌 돈
    def getname(self):
        return self.name
    def getlocation(self):
        return self.location
    def getbount_city(self):
        return self.bought_city
    def getmoney(self):
        return self.money
    def setlocation(self,now): # 현재 위치를 매개변수로 받는다.
        self.location=now
    def setbought_city(self,buy): # 새롭게 구매한 도시를 메개변수로 받는다.
        self.bought_city.append(buy)
    def setmoney(self,m):
        self.money=m    
        
class Draw_board: # 게임판 그려줌
    def __init__(self,city): # 도시 상태 입력받기.
        self.citydown=city[:5]
        self.cityup=city[5:]   
        self.citydown.reverse()
    def draw(self):
        print("\n")
        for i in self.cityup:
            if "Paris" in i:
                print("  {0: <20}  ".format(i))
                break
            print("  {0: <20}->".format(i),end="")
        print("")
        for j in self.citydown:
            if "START" in j:
                print("  {0: <20}  ".format(j))
                break
            print("  {0: <20}<-".format(j),end="")
        print("\n")

class main: # main 게임 진행 클래스
    def __init__(self):
        self.round=0
        # 도시 리스트
        self.city=["START","Seoul","Tokyo","Sydney","LA","Cairo","Phuket","New delhi","Hanoi","Paris"] 
        # 게임판 표시용 리스트
        self.board_city=["START(1)(2)","Seoul","Tokyo","Sydney","LA","Cairo","Phuket","New delhi","Hanoi","Paris"] 
        self.player1=Player("player1") # 플레이어 생성
        self.player2=Player("player2")
        self.board=Draw_board(self.board_city) # 게임판 생성
    def game_start(self):
        print("\n"+"-"*48+"GAME START!!"+"-"*54+"\n")
        self.board.draw() # 게임판 그리기.
        self.main_game() # 메인 게임 진행
        
    def main_game(self):
        while self.round<30: # 30라운드까지 진행되면 종료.
            self.round+=1
            print("\n\n"+"-"*50+"Round {}".format(self.round)+"-"*56)
            for i in range(2):
                if i==0: # 현재 플레이어 = player1
                    player=self.player1 # player는 현재 플레이어, other_player는 상대방.
                    other_player=self.player2
                elif i==1: # 현재 플레이어 = player2
                    player=self.player2
                    other_player=self.player1
                
                # player의 차례 
                print("\n\n{}의 차례입니다. {}이(가) 주사위를 굴립니다.".format(player.name,player.name))
                dice_num=randint(1,6)
                print("주사위 값이 {}이(가) 나왔습니다. {}칸 이동합니다.".format(dice_num,dice_num))
                
                idx=self.city.index(player.getlocation()) # player 현재 위치한 도시를 찾는다.
                if i==0:
                    self.board_city[idx]=self.board_city[idx].replace("(1)","") # player 위치 표시 수정해준다.
                elif i==1:
                    self.board_city[idx]=self.board_city[idx].replace("(2)","") # player 위치 표시 수정해준다.
                if (idx+dice_num)>=10: 
                    idx=idx+dice_num-10 
                else:
                    idx=idx+dice_num
                    
                try: # 리스트 인덱스 에러 예외 처리
                    player.setlocation(self.city[idx]) # player 현재 위치한 도시 바꿔준다.
                    if i==0:
                        self.board_city[idx]+="(1)" # player위치 표시 수정.
                    elif i==1:
                        self.board_city[idx]+="(2)"
                except IndexError:
                    print("리스트 인덱스 에러발생.")
                    sys.exit()
                    
                self.board=Draw_board(self.board_city) # player위치 표시 수정한 정보 업데이트.
                self.board.draw() # 새로운 정보 갱신한 게임판 그려줌
                
                if player.getlocation()=="START": # 플레이어 현재 위치가 시작 지점(START)인 경우
                    print("\n{}이(가) 시작 지점으로 왔습니다.".format(player.getname()))
                    if self.round!=30:
                        print("다음 턴으로 넘어갑니다.")
                    pass
                elif player.getlocation() in player.getbount_city(): # 본인이 구매한 도시에 온 경우
                    print("\n{}이(가) 본인의 도시로 왔습니다.".format(player.getname()))
                    if self.round!=30:
                        print("다음 턴으로 넘어갑니다.")
                    pass
                elif player.getlocation() in other_player.getbount_city(): # 상대방 도시에 온 경우
                    print("\n{}이(가) 상대방의 도시로 왔습니다. 통행료 600원을 지불해야합니다.".format(player.getname()))
                    
                    if player.getmoney()>=600: # 통행료 지불 가능할 때
                        player.setmoney(player.getmoney()-600) # 통행료 지불
                        other_player.setmoney(other_player.getmoney()+600) # 지불한 통행료 ohter_player에게 감.
                        print("통행료 지불이 완료되었습니다. 현재 {}이(가) 지닌 현금은 {}, {}이(가) 지닌 현금은 {}입니다."\
                            .format(player.getname(),player.getmoney(),other_player.getname(),other_player.getmoney()))

                    else: # 통행료 지불 불가능 할때. -> 게임종료.
                        print("잔액이 부족하여 통행료를 지불할 수 없습니다. 게임을 종료합니다.")
                        player.setmoney(0)
                        print("\n\n승리: {}, 현금 잔액: {: >5}, 구매한 도시: {}".format(other_player.getname(),\
                            other_player.getmoney(),other_player.getbount_city()))
                        print("패배: {}, 현금 잔액: {: >5}, 구매한 도시: {}".format(player.getname(),\
                            player.getmoney(),player.getbount_city()))
                        print("\nGAME OVER")
                        return
                    
                else: # 비어있는 도시. -> 구매.
                    print("\n비어있는 도시입니다. 도시를 구매합니다.")
                    if player.getmoney()>=300: # 가진 돈이 넉넉한 경우
                        player.setmoney(player.getmoney()-300) # 도시 구매 돈 지불
                        ix=self.city.index(player.getlocation()) 
                        if i==0:
                            self.board_city[ix]="Buyer:[1] "+self.board_city[ix] # 도시 구매했다고 게임판에 표시
                        elif i==1:
                            self.board_city[ix]="Buyer:[2] "+self.board_city[ix] # 도시 구매했다고 게임판에 표시
                        player.setbought_city(player.getlocation()) # 구매한 도시 player 구매 목록에 추가.
                        print("도시 구매를 완료하였습니다. 현재 {}의 현금 잔액은 {}입니다.".format(player.getname(),player.getmoney()))
                        print("현재 소유하고 계신 도시는 {}입니다.".format(player.getbount_city()))
                        self.board=Draw_board(self.board_city)
                        self.board.draw() # 새로운 정보 갱신한 게임판 그려줌
                    else: # 가진돈이 부족하여 도시 구매를 진행할 수 없을 때.
                        print("잔액이 부족하여 도시를 구매할 수 없습니다.")
                        if self.round!=30:
                            print("다음 턴으로 넘어갑니다.")
                            
        print("\n\n30라운드가 모두 종료 되었습니다.")
        print("[{}] -> 현금 잔액: {}, 구매한 도시: {}".format(self.player1.getname(),\
            self.player1.getmoney(),self.player1.getbount_city()))
        print("[{}] -> 현금 잔액: {}, 구매한 도시: {}".format(self.player2.getname(),\
            self.player2.getmoney(),self.player2.getbount_city()))
        return   

game=main()
game.game_start()