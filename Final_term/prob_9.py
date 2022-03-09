class bus:
    def __init__(self,num):
        self.number=num
        self.dest="없음"
        self.fuel=0
    def get_status(self):
        return("{}번 버스: 연료{}리터, 목적지{}".format(
            self.number,self.fuel,self.dest))
    def move(self):
        print("{}로 이동합니다.".format(self.dest))
        self.fuel=self.fuel/2
    def add_fuel(self,fuel):
        self.fuel+=fuel
        print("기름을 {}넣었음.".format(fuel))
b=bus(2018)
print(b.get_status())
b.add_fuel(10)
print(b.get_status())
b.dest="대구"
print(b.get_status())
b.move()
print(b.get_status())