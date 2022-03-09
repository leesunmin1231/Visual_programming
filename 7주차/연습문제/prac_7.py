'''
콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하는 프로그램을 작성하시오.
실행 예)
a = convert_int(“1,234,567”)
print(a)
print(a+1)
1234567
1234568
'''
def convert_int(num):
    data=num.split(",")
    result=""
    for i in data:
        result+=i
    return(int(result))

a = convert_int("1,234,567")
print(a)
print(a+1)