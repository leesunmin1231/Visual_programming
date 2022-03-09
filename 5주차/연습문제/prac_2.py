N=int(input("N = ? "))
answer=[]
x=int(input("x = ? "))
for i in range(N):
    data=int(input(""))
    if data<x:
        answer.append(data)
    else:
        continue
for i in answer:
    print(i,end=" ")
