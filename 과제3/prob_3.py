f=open('owid-covid-data.csv','r')
data=f.readlines()
f.close()
kor_data=[]
kor_vaccine={}

title=data[0].split(",") # 목록 제목
title[-1]=title[-1][:-1] # 마지막 데이터 \n제거

for i in range(len(data)):
    data[i]=data[i].split(",") # 데이터 
    data[i][-1]=data[i][-1][:-1] # 마지막 데이터 \n제거
    if data[i][0]=="KOR": 
        kor_data.append(data[i]) # 한국 데이터만 모으기
kor_data.reverse()
for i in range(len(title)):
    if kor_data[0][i]=='': # 최근 데이터에 데이터가 없을 경우,
        for da in kor_data:
            if da[i]!='':
                print("{0: <40} : {1: <65}".format(title[i],"No data. 데이터가 있는 최근 날짜: "+da[3]\
                    +", Data: "+da[i]))
                if "vaccin" in title[i]:
                    kor_vaccine[title[i]]=[da[3],da[i]] # 한국 백신 현황 데이터 따로 모으기.
                break
        continue
    print("{0: <40} : {1: <65}".format(title[i],kor_data[0][i])) # 가장 최근 날짜에 있는 데이터들 출력
print("-"*111)
print("한국 최근 백신 현황") # 최근 백신 현황만 모아서 출력
for key,value in kor_vaccine.items():
    print("{0: <40} : {1: <50}".format(key,"날짜: "+value[0]+", Data: "+value[1]))
    