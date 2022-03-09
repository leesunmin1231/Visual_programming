def print_dan(x):
    for i in range (9):
        print("{} * {} = {}".format(x,i+1,x*(i+1)))
    return()
for i in range(2,10):
    print_dan(i)