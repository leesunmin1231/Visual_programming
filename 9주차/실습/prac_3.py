f=open("score.csv",'r',encoding='utf-8')
total={}
v=f.readline()
while True:
    v=f.readline()
    if v=='':
        break
    if v[-1]=='\n':
        v=v[:-1]
    s=v.split(",")
    total[s[0]]=int(s[1])+int(s[2])+int(s[3])
for iD,score in total.items():
    print("{}의 총 점수는 {}이다. 평균은 {}이다.".format(iD,score,score/3))

