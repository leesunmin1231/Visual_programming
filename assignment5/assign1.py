import pylightxl as xl
import matplotlib.pyplot as plt
import numpy as np
# 표 그리기 
while True:
    db = xl.readxl(fn='elec.xlsx')
    data=[]
    for row in db.ws(ws='Sheet1').rows:
        data.append(row)
    labels=data[0]
    values=data[1]
    explode=[0.01,0.01,0.01,0.01,0.01]
    legend_labels=[]

    total = np.sum(values) ## 빈도수 합
    upper_limit = 5 ## 상한선 비율

    # values 값 퍼센트로 바꾸기. 
    for i in range(len(values)):
        values[i]=values[i]/total*100
        
    for i in range(len(labels)): # 범례에 적어줄 라벨 만들기. 
        text = f'{values[i]:.1f}%'
        legend_labels.append(f'NO.{i+1} '+labels[i]+": "+text) # (라벨: 퍼센트)
        
    # 표 그리기.
    fig = plt.figure(figsize=(10,8)) ## 캔버스 생성
    fig.set_facecolor('white') ## 캔버스 배경색을 하얀색으로 설정
    ax = fig.add_subplot() ## 프레임 생성

    pie=ax.pie(values, explode=explode, startangle =45, textprops = {'fontsize':8})
    
    # 주석 설정.
    for i,l in enumerate(labels):
        ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2 
        ## value[i]에 해당하는 파이의 시작 각도와 끝 각도
        center, r = ax.patches[i].center, ax.patches[i].r ## 원의 중심 좌표와 반지름길이
        text = f'{values[i]:.1f}%' # 적어줄 퍼센트 값
        ang = (ang1+ang2)/2 ## value[i]에 해당하는 부채꼴 중심각.
        ## 비율 상한선보다 작은 것들은 주석으로 따로 적어준다. (글자가 겹쳐서 안보임.)
        if values[i] < upper_limit:
            x = r*np.cos(np.radians(ang)) ## Annotation의 끝점에 해당하는 x좌표
            if values[i] <=0.30: # 퍼센트가 너무 작아서 글자 겹침. y좌표는 또 따로 분리해줌.
                y = r*np.sin(np.radians(ang))+0.01 ## Annotation의 끝점에 해당하는 y좌표
            else:
                y = r*np.sin(np.radians(ang))-0.02 ## Annotation의 끝점에 해당하는 y좌표
            
            ax.annotate(labels[i]+": "+text, xy=(x, y), xytext=(2*x, 1.2*y), arrowprops=dict(arrowstyle='-')) 
            # 주석으로 비율 적어줌.
        
        else: # 비율이 큰 것 들은 부채꼴 안에 적어줌.
            x = (r/2)*np.cos(np.radians(ang)) + center[0] ## 텍스트 x좌표
            y = (r/2)*np.sin(np.radians(ang)) + center[1] ## 텍스트 y좌표
            ax.text(x,y,labels[i]+": "+text,ha='center',va='center',fontsize=12)

    plt.legend(labels=legend_labels, loc=(-0.3,-0.1)) # 범례 적어줌. (라벨: 퍼센트)
    plt.title('20th electron') # 표 제목
    plt.show(block=False) # 그리기
    plt.pause(10) # 잠시 기다리기
    plt.close() # figure 지우기
