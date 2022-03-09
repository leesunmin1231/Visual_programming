# 1
lst=[]
Sat_0301 = [(100, 98), (97, 95), (88, 90), (50, 58), (100, 100), (97, 100), (100, 98), (97, 95), (88, 90), (50, 58) ]

lst=list(map(int,input().split(' ')))


index=0
avg_lst=[]
for score1,score2 in Sat_0301:
    avg=(score1+score2+lst[index])
    index+=1
    avg_lst.append(avg)
print(avg_lst)
