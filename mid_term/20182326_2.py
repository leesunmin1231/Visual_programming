while True:
    n=input("N = ? ")
    if int(n)==0:
        break
    elif int(n)%2==1:
        for i in range(len(n)):
            print(" "*(len(n)-i-1),end="")
            for j in range(i+1):
                print(n[j],end="")
            print("")
    else:
        for i in range(len(n)):
            print(" "*i,end="")
            for j in range(len(n)-i):
                print(n[i+j],end="")
            print("")
