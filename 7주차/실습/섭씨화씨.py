'''
화씨 = 9/5*섭씨 +32
섭씨 = 5/9*(화씨-32)
'''

# 섭씨에서 화씨 
def celtofah(num):
    result=9/5*num+32
    return (result)

# 화씨에서 섭씨
def fahtocel(num):
    result=5/9*(num-32)
    return(result)

num=float(input("온도는? "))
print('섭씨 {}도는 화씨 {}도 이다.'.format(num,celtofah(num)))
print('화씨 {}도는 섭씨 {}도 이다.'.format(num,fahtocel(num)))