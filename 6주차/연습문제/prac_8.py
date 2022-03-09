'''
문장을 입력하고 입력한 문장에서 공백을 이용해 단어들을 구분하고, 중복된 단어 없이 콤마(,)로 구분해 알파벳 출력하시오.
실행 예)
Grief is the agony of an instant the indulgence of grief the blunder of a life
Grief, a, agony, an, blunder, grief, indulgence, instant, is, life, of, the

'''

sen=input().split(" ")
sen=list(set(sen))
for word in sen:
    if sen.index(word)==len(sen)-1:
        print(word)
    else:
        print(word, end=", ")
