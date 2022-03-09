Students = ['20200000chungangkim', '20201111chunganglee', '20202222chungangpark']
st={}
result=[]
for i in range(len(Students)):
    st['id']=Students[i][:8]
    st['name']=Students[i][8:]
    result.append(st)
print(result)
    
