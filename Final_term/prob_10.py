while True:
    name=input()
    try:
        f=open(name,'r')
    except FileNotFoundError:
        print("다시 입력하세요")
        continue
    line=f.readlines()
    count=len(line)
    print(count)