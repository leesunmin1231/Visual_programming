from random import *
num=randint(1,20)
expact=0
count=0
while expact!=num:
    expact=int(input("숫자 입력: "))
    count+=1
    if expact==num:
        print("%d회 만에 맞추셨습니다. 정답은 %d 입니다."%(count,num))
    elif expact>num:
        print("더 작은 숫자를 입력하세요")
    else:
        print("더 큰 숫자를 입력하세요")
        
    
