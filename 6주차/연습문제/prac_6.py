'''
lecture_1 = [{'id':'20200000', 'name':'김중앙', 'attendance':0}, {'id':'20201111', 'name':'이중앙', 'attendance':1}, {'id':'20200000', 'name':'박중앙', 'attendance':2}]
(0: 결석, 1: 출석, 2: 지각)
실행 예)
조회할 학번: 20200000
학번: 20200000 이름: 김중앙 출석

'''

lecture_1 = [{'id':'20200900', 'name':'김중앙', 'attendance':0}, {'id':'20201111', 'name':'이중앙', 'attendance':1}, {'id':'20200000', 'name':'박중앙', 'attendance':2}]

stu_id=input("조회할 학번: ")
for item in lecture_1:
    if item['id']==stu_id:
        if item['attendance']==0:
            attend='결석'
        elif item['attendance']==1:
            attend='출석'
        else:
            attend='지각'
        print("학번: {} 이름: {} 출석: {}".format(item['id'],item['name'],attend))
    else:
        continue
