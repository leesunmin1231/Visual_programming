sen=input().split(".")
first=sen[0]
if first[:2]=="저는":
    index=3
    while True:
        if first[index:]=="입니다" or first[index:index+3]=="이라고":
            break
        index+=1
    name=first[3:index]
    print("이름 : {}".format(name))
else:
    index=6
    while True:
        if first[index:]=="입니다":
            break
        index+=1
    name=first[6:index]
    print("이름 : {}".format(name))