# z = int(input("시작 수는?"))
# y = int(input("끝수는?"))
# j = int(input("정수를 입력하세요"))


# if j >=z and j <= y :
#     result = "%d는%d~%d사이에 있다"%(j,z,y)
# if j <z or j > y :
#     result = "%d는 %d~%d사이에 없다."%(j,z,y)
# print(result)
# 툭정범위에 있는수 판별10
#
#
# month1 = int(input("월을 숫자로 입력하세요"))
# if  3<= month1 <=5 :
#     print("%d는 봄입니다."%month1)
# if  6<= month1 <=8 :
#     print("%d는 여름입니다."%month1)
# if  9<= month1 <=11 :
#     print("%d는 가을니다."%month1)
# if   month1==12 or month1 == 1 or month1==2:
#     print("%s는 겨울입니다."%month1)
#월 입력받아서 계절 판별

ju = int(input("주민번호 뒷자리 첫번째 수자를 입력해주세요:"))

if ju == 1 or ju == 3 :
    print("남성입니다.")
if ju == 2 or ju == 4 : 
    print("여성입니다.")
else : print("외계인?")











