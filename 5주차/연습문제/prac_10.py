N=int(input("n= ? "))
lst=[]
for k in range(N):
    lst.append(k+1)
lst.remove(1)
i=3
while i<N:
    i+=1
    j=2
    while j<i:
        if i%j==0:
            lst.remove(i)
            break
        j+=1
print(len(lst))
print("{}은 첫번째 소수, {}은 마지막 소수".format(lst[0],lst[-1]))

    
    
