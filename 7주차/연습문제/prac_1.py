'''
공백없이 입력하는 숫자 각 자리의 합을 구하는 프로그램을 작성하시오.
실행 예)
54321
15 (5+4+3+2+1=15)
7000000000000000000000000
7 (7+0+0+0+0+…+0 = 7)
'''

num=input()
sum=0
for i in num:
    sum+=int(i)
print(sum)
