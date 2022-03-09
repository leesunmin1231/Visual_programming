'''
import numpy as np
a = np.array( [20, 30, 40, 50 ] )
b = np.arange(4) # 0부터 3까지의 배열.
print(b)
c = a-b
print(c)
print(10 * np.sin(a))
print(a < 35)

[0 1 2 3]
[20 29 38 47]
[ 9.12945251 -9.88031624  7.4511316  -2.62374854]
[ True  True False False]
'''
import math
a=[20,30,40,50]
b=list(range(4))
print(b)
c=[]
for i in range(4):
    c.append(a[i]-b[i])
print(c)
data=[]
for i in range(4):
    data.append(round(10*math.sin(a[i]),8))
    if a[i] < 35:
        a[i]=True
    else:
        a[i]=False
print(data)
print(a)
