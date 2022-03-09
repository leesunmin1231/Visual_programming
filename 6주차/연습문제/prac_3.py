refrigerator = [0, 1, 2, 3, 4, 5, 6]
Dic={'달걀': 0, '양파': 1, '당근': 2, '감자': 3, '두부': 4, '버섯': 9, '소고기': 6, '참기름': 7, '미역': 8}

data=input()
put_data=[]
j=0
for i in range(len(data)):
    if data[i]==" ":
        put_data.append(data[j:i])
        j=i+1
    if i==len(data)-1:
        put_data.append(data[j:])

for it in put_data:
    if it in Dic:
        index=Dic.get(it)
        if index in refrigerator:
            pass
        else:
            print(it,end=' ')
            
