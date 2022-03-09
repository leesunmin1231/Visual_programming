menu={"noodle":500, "ham":200, "egg":100, "spaghetti":900}
print("안녕하세요 다음의 메뉴 중 원하는 메뉴를 선택하세요.")
request=input("(noodle, ham, egg, spaghetti) ")
if request in menu:
    print("{}원 입니다.".format(menu[request]))
else:
    print("그런 메뉴는 없습니다.")
