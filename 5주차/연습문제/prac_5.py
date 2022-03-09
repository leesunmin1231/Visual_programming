import sys
score=int(input("점수: "))
if score==0:
    sys.exit()
if score>=95:
    grade='A+'
elif score>=90:
    grade='A0'
elif score>=85:
    grade='B+'
elif score>=80:
    grade='B0'
elif score>=75:
    grade='C+'
elif score>=70:
    grade='C0'
elif score>=65:
    grade='D+'
else:
    grade='F'
print(grade)
    
