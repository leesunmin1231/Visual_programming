import random
comwin=0
userwin=0
round=1
print("가위바위보 게임")
print("컴퓨터 : {}승 {}패, 당신: {}승 {}패".format(comwin,round-comwin,userwin,round-userwin))
while True:
    print("\n(라운드 {})".format(round))
    data=random.randint(1,3)
    if data==1:
        com="가위"
    elif data==2:
        com="바위"
    else:
        com="보"
    print("컴퓨터가 결정했습니다.")
    user=input("무엇을 내시겠습니까? (가위,바위,보) ")
    print("컴퓨터는 {}, 당신은 {}".format(com,user),end=", ")
    if com==user:
        print("")
        continue
    elif com=="바위" and user=="가위":
        comwin+=1
        print("컴퓨터가 이겼습니다.")
        print("컴퓨터 : {}승 {}패, 당신: {}승 {}패".format(comwin,round-comwin,userwin,round-userwin))

    elif com=="보" and user=="바위":
        comwin+=1
        print("컴퓨터가 이겼습니다.")
        print("컴퓨터 : {}승 {}패, 당신: {}승 {}패".format(comwin,round-comwin,userwin,round-userwin))

    elif com=="가위" and user=="보":
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

    
