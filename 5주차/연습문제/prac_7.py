N=int(input("N = ? "))
for i in range(N):
    fac=1
    for j in range(i+1):
        fac=(j+1)*fac
    print("{}! = {}".format(i+1,fac))
