from random import *
N=int(input("N = ? "))
sum=0
print("랜덤한 숫자 %d개: "%(N),end="")
for i in range(N):
    data=randint(1,100)
    sum+=data
    if i==N-1:
        print(data)
    else: 
        print(data,end=",")
print("합계 : %d"%(sum))
print("평균 : {}".format(round((sum/N),2)))
