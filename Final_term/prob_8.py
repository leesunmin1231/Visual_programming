while True:
    lst=[]
    sum=0
    data=input()
    for i in data:
        lst.append(int(i))
    q=len(lst)//2
    for i in range(q):
        sum+=lst[i]*lst[-(i+1)]
    if (len(lst)%2==1):
        sum+=lst[q]
    print(sum)
        