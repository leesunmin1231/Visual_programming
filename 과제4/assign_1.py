class Calc:
    def __init__(self,num=0):
        self.num=num
    def print(self):
        print(self.num)
    def setvalue(self,n):
        self.num=n
        return(self.num)
    def getvalue(self):
        return(self.num)
    def add(self,adder):
        self.num+=adder
        return(self.num)
    def minus(self,m):
        self.num-=m
        return(self.num)
    
cal1 = Calc () # 객체 생성
cal2 = Calc (5) # 5 를 초기화하여 객체 생성
cal1.setvalue(10) # 10설정
cal1.add(20) # 20더하기
cal1.minus(5) # 5빼기
cal1.print() # 값 표시하기
cal2.add(cal1.getvalue() ) # cal1의 값을 cal2 에 더하기
cal2.print() #값 표시하기