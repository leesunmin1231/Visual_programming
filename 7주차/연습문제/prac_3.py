'''
입력된 문자열을 역순으로 출력하는 print_reverse 함수를 만드시오.
실행 예)
print_reverse(“python”)
nohtyp
'''

def print_reverse(word):
    for i in range(len(word)):
        print(word[-(i+1)],end="")
print_reverse("python")