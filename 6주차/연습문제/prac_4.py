# 최소공배수

data=list(map(int,input().split(' ')))
num1=set(range(0,10000,data[0]))
num2=set(range(0,10000,data[1]))
result=list(num1&num2)
result.sort()
print(result[1])

# !!!!!!!!!!! set은 순서가 없다. 정렬 필수!!!!!!!!!
