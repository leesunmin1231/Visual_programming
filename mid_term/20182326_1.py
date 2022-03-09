import math
answer={}
while True:
    r=float(input())
    if r==0:
        break
    answer[r]=round(r**2*math.pi,3)
for rad,result in answer.items():
    print("{} : {}".format(rad,result))
