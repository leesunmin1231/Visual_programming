while True:
    name=input("파일 이름을 입력하세요: ")
    try:
        f=open(name,'r',encoding='utf-8')
    except IOError:
        print("파일을 찾지 못했습니다.")
        continue
    else:
        mlines=f.readlines()
        for line in mlines:
            print(line,end='')
        f.close()
        break