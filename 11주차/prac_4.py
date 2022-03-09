'''
“개”, “고양이” 문자열을 반환하는 함수(get_dog( ), get_cat( ))가 있는 동물 모듈(animal.py)을 만들 고고,
“dog”를 입력하면 “개개”를를, “cat”을 입력하면 “고양이고양이”를 화면에 표시하는 프로그램프로그램(myprog.py)을 작성
하라하라. 프로그램은 animal.py 와 myprog.py 두 개로 구성되어야 한다한다.
함수
작성의 예예)
def get_dog( ) :
return “개개”
myprog.py의 예
import animal
name = input(“단어를 입력하시오입력하시오”)
if name == “dog” :
print( get_dog( ) )
… 이후 생략

'''
from animal import get_dog,get_cat
name = input("단어를 입력하세요: ")
if name == "dog":
    print(get_dog())
elif name == "cat":
    print(get_cat())