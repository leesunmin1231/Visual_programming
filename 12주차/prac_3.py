'''
강의 자료에 있는 UltraSuperCalculator 까지 입력한 후, 사용자가 입력한 2개의 값을 각각 더하고, 빼
고, 곱한 결과를 화면에 표시하는 프로그램을 작성하라.
'''
class Calculator:
    def __init__(self):
        self.result = 0
        
    def adder(self, num):
        self.result = self.result + num;
        return self.result
    
    def __str__(self):
        return str(self.result)

class SuperCalculator(Calculator):
    def subtractor(self,num):
        self.result=self.result-num
        return self.result

class UltraSuperCalculator(SuperCalculator):
    def multiplier(self,num):
        self.result=self.result*num
        return self.result
    
cal=UltraSuperCalculator()
cal.adder(3)
print(cal)
cal.subtractor(1)
print(cal)
cal.multiplier(6)
print(cal)