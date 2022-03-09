f=open('dict_test_utf8.TXT','r',encoding='utf-8')
book=f.readlines()
f.close()
for i in range(len(book)):
    book[i]=book[i].split(" : ")
while True:
    word=input("단어? ")
    for i in range(len(book)):
        if book[i][0]==word:
            print(book[i][0],book[i][1])
            break
