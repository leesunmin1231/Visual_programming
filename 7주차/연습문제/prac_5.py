'''
문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하는 프로그램을 작성하시오.
실행 예)
make_list(“abcd”)
[‘a’, ‘b’, ‘c’, ‘d’]
'''
def make_list(word):
    lst=list(word)
    print(lst)
    return(lst)
make_list("abcd")
