num_lst=["이","삼","사","오","육","칠","팔","구"]
unit_lst=["십","백","천","만"]
num=input("숫자는? ")
if len(num)>3:
    money=num[:len(num)-3]+','+num[len(num)-3:]
    print("{}원".format(money))
else:
    print("{}원".format(num))
for i in range(len(num)):
    if num[i]=='0':
        continue
    for j in range(8):
        if int(num[i])==j+2:
            print(num_lst[j],end="")
    for k in range(4):
        if len(num)-i==k+2:
            print(unit_lst[k],end="")
            continue
print(" 원")