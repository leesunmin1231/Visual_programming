'''
숫자로 구성된 하나의 리스트를 입력 받아, 
짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하는 프로그램을 작성하시오.
실행 예)
a = pickup_even([3, 4, 5, 6, 7, 8])
print(a)
[4, 6, 8]
'''
def pickup_even(lst):
    result=[]
    for i in lst:
        if i%2==0:
            result.append(i)
    return(result)
a = pickup_even([3, 4, 5, 6, 7, 8])
print(a)