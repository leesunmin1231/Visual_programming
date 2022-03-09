lst=["apple"]
score=0
round=0
while round!=10:
    round+=1
    print(round)
    word=input("단어({}): ".format(lst[-1]))
    if word in lst:
        score-=1
        print("이미 나온 단어입니다. 1점 차감. 현재 점수 {}점".format(score))
    else:
        if lst[-1][-1]==word[0]:
            score+=1
            lst.append(word)
            print("1점 획득. 현재 점수 {}점".format(score))
        else:
            score-=1
            print("끝말잇기가 안됩니다. 1점 차감. 현재 점수 {}점".format(score))