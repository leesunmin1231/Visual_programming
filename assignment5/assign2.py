import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

f=open('owid-covid-data.csv','r')
full_data=f.readlines()
f.close()

title=full_data[0].split(",") # 목록 제목
title[-1]=title[-1][:-1] # 마지막 데이터 \n제거

fully_idx=title.index("people_fully_vaccinated_per_hundred")
part_idx=title.index("people_vaccinated_per_hundred")

for i in range(len(full_data)):
    full_data[i]=full_data[i].split(",") # 데이터 
    full_data[i][-1]=full_data[i][-1][:-1] # 마지막 데이터 \n제거

location=["location"]
vaccin_data=[]
full_data.reverse()
for data in full_data:
    if data[fully_idx]=="":
        continue
    elif data[part_idx] == "":
        continue
    else:
        if data[2] in location: # 중복 데이터 검사.
            continue
        location.append(data[2])
        vaccin_data.append([data[2],float(data[fully_idx]),float(data[part_idx])]) # [국가, full, part]

vaccin_data=sorted(vaccin_data, key=lambda x: x[1]+x[2])
vaccin_data=vaccin_data[-20:]
location_list=[]
full_list=[]
part_list=[]
totalsum_list=[]
for data in vaccin_data:
    location_list.append(data[0])
    full_list.append(data[1])
    part_list.append(data[2])
    totalsum_list.append((data[1]+data[2])/2)
# plot
fig, ax = plt.subplots(figsize=(13,6))
plt.subplots_adjust(left=.20, bottom=.15)
plt.barh(location_list,totalsum_list,color='#28BB14')
plt.barh(location_list,full_list,color='green')
plt.ylabel('Location',fontsize=15)
plt.xlabel('Data',fontsize=15)
plt.xlim(0,130)
plt.xticks(fontsize=10)
plt.yticks(location_list)
plt.legend(labels=["People only partly vaccinated against","People fully vaccinated against"], loc=(-0.2,-0.15)) 
# 범례 적어줌. 
for i,data in enumerate(totalsum_list):
    plt.text(data+1, (i+1)*1-1.15, f'{int(data)}'+'%')
plt.show() # 그리기

    
