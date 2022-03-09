sen=input("검색할 문장: ")
while True:
    word=input("찾을 문자: ")
    if word=="end":
        break
    lst=sen.split(" ")
    for i in range(len(lst)):
        if word in lst[i]:
            lst[i]="("+lst[i]+")"
    for j in lst:
        print(j,end=" ")
    print("")

