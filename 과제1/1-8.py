# 반복문을 2중으로 쓰지 않고 표현할 수 있습니다. 이를 해결할 방법을 생각해보시기 바랍니다."
import math

angular=0
for i in range(38):
    value=math.sin(math.radians(angular))
    print(" "*(int(value*10)+10),end="")
    print("*")
    angular+=10




