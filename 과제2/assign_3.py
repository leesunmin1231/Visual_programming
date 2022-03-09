seque=input("수식을 입력하세요 : ")
seque=seque.split("+")
sum=0
lst2=[]
for i in seque:
    if "-" in i:
        lst=list(map(int,i.split("-")))
        minus=lst[0]
        for num in lst:
            minus=minus-num
        minus+=lst[0]
        lst2.append(minus)
    else:
        lst2.append(int(i))
for j in lst2:
    sum+=j
print("= {}".format(sum))
