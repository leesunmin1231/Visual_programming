money=int(input("원금을 입력하세요(원)."))
rate=int(input("금리를 입력하세요(%). "))
print("원금 {}원 금리{}%입니다.".format(money,rate))
print("기간    합계")
for i in range(20):
    money=money+(money*rate/100)
    print("{}년   {:.2f}".format(i+1,money))
