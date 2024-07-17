animai =  '고양이'
catname = '로드'
x = '나는 %s%s 좋아합니다.' %(animai,catname) 
print(x)

age=20
print('내 나이는 %d 입니다.' %age)

pay =10000000
print('내나이는 %d 이고 연봉은 %d입니다.'%(age,pay))

kor = 70
eng = 57
math= 10
sum = kor + eng+ math
avg = sum/3
print('합계 : %d 평균 : %.5f'%(sum,avg))


'''
person = input('이름을 입력하세요')
print(person+'님 안녕하세요')

a = input("첫 번째 정수를 입력하세요")
b = input("두번째도 입력")
c = a+b
print(c)


age = input("당신의 나이는 몇살인가요")
print('당신의 나이는 %s입니다.'%age)

year = input("당신이 태어난 년도")
avg = 2024-int(year)
print('당신의 나이는 %s 입니다.'%age)


a = int(input('첫번째 정수를 입력하세여'))
b = int (input('두번째 정수를 입력하세요'))
if a>b : print(a)
elif a==b : print(a,b)
else : print(b)
'''

a = int(input('첫번째 정수를 입력하세여'))
b = int (input('두번째 정수를 입력하세요'))
c = int (input('세번째 정수 입력'))
'''
if a>b>c or a>c>b or a>c>=b: print(a)
elif b>c>a or b>a>c or b>c>=a : print(b)
else  : print(c)
'''
if a>b and a>c : print(a)
elif b>a and b>c : 
    print(b)
elif c>a and c>b :
    print(c)
