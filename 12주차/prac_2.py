class Calculator:
    def __init__(self):
        self.result = 0
    def adder(self, num):
        self.result = self.result + num;
        return self.result
    def print(self):
        print(self.result)
        return self.result
cal1 = Calculator()
cal1.adder(int(input()))
cal1.print()
cal1.result += int(input())
cal1.print()