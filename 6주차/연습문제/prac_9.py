'''
수식을 입력하고 입력한 수식의 계산한 결과를 출력하시오. (단, 덧셈, 뺄셈, 곱셈만 가능하고, 수식에 있는 연산자는 모두 같다.)
실행 예)
12+345+6789
12 + 345 + 6789 = 7146
'''
eq=input()
result=0
if '+' in eq:
    eq=list(map(int,eq.split("+")))
    for num in eq:
        result+=num
        print(num,end="")
        if eq.index(num)==len(eq)-1:
            print(" = ",end="")
        else:
            print(" + ",end="")
    print(result)
elif '-' in eq:
    eq=list(map(int,eq.split("-")))
    result=eq[0]
    for num in eq:
        result-=num
        print(num,end="")
        if eq.index(num)==len(eq)-1:
            print(" = ",end="")
        else:
            print(" - ",end="")
    print(result+eq[0])
elif '*' in eq:
    eq=list(map(int,eq.split("*")))
    result=eq[0]
    for num in eq:
        result*=num
        print(num,end="")
        if eq.index(num)==len(eq)-1:
            print(" = ",end="")
        else:
            print(" x ",end="")
    print(int(result/eq[0]))
