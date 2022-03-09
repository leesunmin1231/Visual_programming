sum=1
lstA=[]
lstB=[]
lstsum=[]
while sum!=0:
    A=int(input("A = ? "))
    B=int(input("B = ? "))
    sum=A+B
    if sum!=0:
        lstA.append(A)
        lstB.append(B)
        lstsum.append(sum)
        continue
    else:
        for i in range(len(lstsum)):
            print("%d + %d = %d"%(lstA[i],lstB[i],lstsum[i]))
    
        
