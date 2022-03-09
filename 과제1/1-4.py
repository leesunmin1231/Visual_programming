num=1
lst=[]
print("데이터를 입력하세요. (입력을 마치려면 0을 입력하세요)")
while num!=0:
    num=int(input())
    if num!=0:
        lst.append(num)
lst.sort()
print("결과 : ",end="")
for i in lst:
    print(i,end=" ")
print("(%d개)"%(len(lst)))
