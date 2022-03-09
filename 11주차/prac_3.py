'''
텍스트 파일 이름을 입력 받아 그 파일의 내용을 화면에 출력하는 프로그램을 작성하라작성하라.
단, 파일이 존재하지 않으면 오류라고 표시하고 다시 이름을 입력 받아라받아라.
실행 예)
파일 이름? test.csv
...... 파일의 내용이 표시됨
실행
예예)
파일 이름? abc.txt
해당
파일이 없습니다. 다시 입력하세요.
파일 이름?
'''
while True:
    file=input("파일 이름? ")
    try:
        f=open(file,'r',encoding="utf-8")
        v=f.readlines()
        f.close()
        for i in v:
            print(i)
    except IOError:
        print("파일이 없습니다. 다시 입력하세요.")