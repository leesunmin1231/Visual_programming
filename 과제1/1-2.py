lst=['흑석동','사당동','상도동','노량진동','규동']
while True:
    new=input("동을 입력하세요. ")
    if new in lst:
        inx=lst.index(new)
        print("%d번째 동입니다."%(inx+1))
    else:
        print("새로운 동명입니다. %d번째 동으로 등록합니다."%(len(lst)+1))
        lst.append(new)
