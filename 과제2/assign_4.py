phonebook={"홍길동":"010-4444-5555","김중앙":"010-9191-8181","심청":"010-3232-5454"}
while True:
    check=0
    data=input("이름>> ")
    if data=="add":
        name=input("이름은? ")
        number=input("전화번호는? ")
        phonebook[name]=number
        print("{} 전화번호가 추가되었습니다.".format(name))
        continue
    for name,number in phonebook.items():
        if data in name:
            print("{} {}".format(name,number))
            check+=1
    if check==0:
        print("찾을 수 없습니다.")
    