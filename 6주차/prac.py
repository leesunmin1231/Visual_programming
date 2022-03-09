line=input("수식을 입력하세요: ")
i=0
lst=[]
sum=0
index=0
while i<(len(line)):
    while line[i]!='+':
        if i==len(line)-1:
            i+=1
            break
        i+=1
    lst.append(int(line[index:i]))
    index=i+1
    i+=1
for num in lst:
    sum+=num
print (sum)
