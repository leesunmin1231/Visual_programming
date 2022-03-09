mylist = [ 23,78,43,11,94,73,13,87,67,16,8]
mid_index=len(mylist)//2
middle=mylist[mid_index]
mylist.sort()
avg=(mylist[0]+mylist[-1])/2
if middle>avg:
    print(middle)
else:
    print(avg)
