'''
7. 사용자에게 [1, 10000] 구간 안에 존재하는 실수를 입력하고 합산하여 소숫점 이하 4자리까지 반올림하여 출력하시오.
실행 예)
[1, 10000] 구간 안에 존재하는 실수를 입력하세요: 37
37 = 37.0000
[1, 10000] 구간 안에 존재하는 실수를 입력하세요: 187.4
37 + 187.4 = 224.4000
'''
sum=0
lst=[]
while True:
    data=input("[1, 10000] 구간 안에 존재하는 실수를 입력하세요: ")
    num=float(data)
    sum+=num
    lst.append(data)
    for n in lst:
        print("{} ".format(n),end="")
        if lst.index(n)==len(lst)-1:
            print("= ",end="")
        else:
            print("+ ",end="")
    print("{:.4f}".format(sum))

