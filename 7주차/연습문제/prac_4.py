'''
입력된 문자열을 역순으로 돌려주는 reverse_str 함수를 만드시오.
실행 예)
a = reverse_str(“python”)
print(a)
nohtyp
'''
def reverse_str(word):
    result=""
    for i in range(len(word)):
        result+=word[-(i+1)]
    return(result)
a = reverse_str("python")
print(a)