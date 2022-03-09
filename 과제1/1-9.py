N=int(input("2에서 9사이의 숫자를 입력하시오. "))
M=int(input("N보다 크거나 같은 2에서 9사이의 숫자를 입력하시오.(단.M-N은 3를 넘지 않는다.) "))

empty=(80-(M-N+1)*5)//(M-N+2)
for i in range(9):
    print("")
    j=N
    print(" "*(empty-1),end="")
    while j<M+1:
        print("{}*{}={}".format(j,i+1,j*(i+1)),end="")
        if j*(i+1)>=10:
            print(" "*(empty-1),end="")
        else:
            print(" "*empty,end="")
        j+=1
        
