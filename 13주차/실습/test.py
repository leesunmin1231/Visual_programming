import numpy as np
data=np.random.randn(2,3) # 배열 랜덤 생성
print(data)
draws=np.random.randint(0,2,1000)
steps=draws*2
walk=steps.cumsum()
