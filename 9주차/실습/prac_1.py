file=open('data.txt','w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    file.write(data)
file.close()