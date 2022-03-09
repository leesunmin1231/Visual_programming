#6
mylist = [ [1,2], [3,4,5], [6,7,8,9], [10,11,12,13,14] ]
a=0
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        a+=mylist[i][j]
print(a)
