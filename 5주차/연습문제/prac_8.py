import sys
data=int(input("초를 입력하세요: "))
if data==0:
    sys.exit()
sec=data%60
data=data//60
minu=data%60
data=data//60
hour=data%24
data=data//24


date=data%30
data=data//30
month=data%12
year=data//12

if year==0:
    pass
else:
    print("{} 년".format(year),end=" ")
if month==0:
    pass
else:
    print("{} 월".format(month),end=" ")
if date==0:
    pass
else:
    print("{} 일".format(date),end=" ")
if hour==0:
    pass
else:
    print("{} 시간".format(hour),end=" ")
if minu==0:
    pass
else:
    print("{}분".format(minu),end=" ")
if sec==0:
    pass
else:
    print("{}초".format(sec),end=" ")
