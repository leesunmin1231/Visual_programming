# 파스칼 삼각형

lst=[1]
answer=[1,1]
line=0
n=int(input("몇번째 줄까지 출력 하시겠습니까? "))
print(1)
while n!=line:
    for a in answer:
        print(a,end=" ")
    print("")
    lst=[num for num in answer]
    answer=[1,1]
    for i in range(len(lst)-1):
        answer.insert(i+1,lst[i]+lst[i+1])
    line+=1

