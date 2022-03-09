f=open('input.txt','w')
while True:
    sen=input()
    if sen=="end":
        break
    sen=sen+'\n'
    f.write(sen)
f.close
