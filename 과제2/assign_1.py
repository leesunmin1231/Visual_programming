tup=("가위","바위","보")
import random
comwin=0
userwin=0
round=1
print("가위바위보 게임")
print("컴퓨터 : {}승 {}패, 당신: {}승 {}패".format(comwin,round-comwin,userwin,round-userwin))
while True:
    print("\n(라운드 {})".format(round))
    com=random.randint(0,2)
    # 0은 가위, 1은 바위, 2는 보
    print("컴퓨터가 결정했습니다.")
    user=input("무엇을 내시겠습니까? {} ".format(tup))
    print("컴퓨터는 {}, 당신은 {}".format(tup[com],user),end=", ")
    if tup[com]==user:
        print("")
        continue
    elif (com==tup.index(user)+1) or (com+2==tup.index(user)):
        comwin+=1
        print("컴퓨터가 이겼습니다.")
        print("컴퓨터 : {}승 {}패, 당신: {}승 {}패".format(comwin,round-comwin,userwin,round-userwin))
    else:
        userwin+=1
        print("당신이 이겼습니다.")
        print("컴퓨터 : {}승 {}패, 당신: {}승 {}패".format(comwin,round-comwin,userwin,round-userwin))
    round+=1
    if comwin==3 or userwin==3:
        break
