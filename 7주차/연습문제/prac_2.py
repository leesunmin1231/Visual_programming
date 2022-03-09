'''
단어를 입력하면 단어에서 가장 많이 사용된 알파벳이 무엇인지 출력하는 프로그램을 작성하시오. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력합니다.
실행 예)
mississipi
?
orthodox
o
'''

def count(word):
    lst=[0]
    result=[]
    for i in word:
        if i in result:
            continue
        num=word.count(i)
        if num>=lst[-1]:
            lst.append(num)
            result.append(i)
    if lst[-1]==lst[-2]:
        return("?")
    return(result[-1])

word=input()
print(count(word))
