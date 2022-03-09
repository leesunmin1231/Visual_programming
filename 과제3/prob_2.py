f=open('dict_test_utf8.TXT','r',encoding='utf-8')
book=f.readlines()
f.close()
dictionary=[]
for i in range(len(book)):
    book[i]=book[i].split(" : ")
    dictionary.append(book[i][0])
lst=["apple"]
score=0
round_score=0
while True:
    print(lst[-1],end=" ")
    word=input("끝말 잇기? ")
    if len(word)<3 or len(word)>10:
        print("3자리 이상, 10자리 이하 글자의 영어단어를 입력하시오.")
        continue
    if word in lst:
        print("이미 나온 단어입니다.")
        continue
    if word not in dictionary:
        print("사전에 없는 단어입니다.")
        continue
    if word[0]==lst[-1][-2] and word[1]==lst[-1][-1]:
        round_score=(len(word))*2
        score+=(len(word))*2 
    elif word[0]==lst[-1][-1]:
        round_score=len(word)
        score+=len(word)
    else:
        print("끝말이 이어지지 않습니다.")
        continue
    lst.append(word)
    print("{}점. 총점: {}점".format(round_score,score))
