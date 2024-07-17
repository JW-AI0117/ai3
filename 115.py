# pilgi = int(input("필기 시험 점수는?"))
# silgi = int(input("실시 시험 점수는?"))

# if pilgi >=80 and silgi>= 80:
#     result = "합격"
# else:
#     result = "불합격"
# print("-필기시험 점수 : %d"%pilgi) 
# print("-실기시험 점수 : %d"%silgi) 
# print("-판정 : %s"%result) 

#-------------------------------------------

# char = input("영문 소문자 하나를 입력")

# if char == 'a'or char =='e'or char == 'i'or char == 'o' or char == 'u' :
#     print("%s는 모음이다."%char)
# else : 
#     print("%s는 자음이다."%char) 

#-------------------------------------

# char  = input("영문 대문자 또는 소문자하나를 입력하세요:")
# char = char.upper()

# if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' :
#     print("%s는 모음"%char)
# else : 
#     print("%s는 자음"%char)

#======================================

# height = int(input("키는?"))
# weight = int(input("몸무게는?"))

# s = (height-100)*0.9

# print("="*50)
# print("키는:",height)
# print("몸무게는:",weight)

# if weight>s : 
#     print("건강을 위해 다이어트")
# else : 
#     print("표준또는 마름체형입니다.")

#======================================

print("아르바이트 급여 계산 프로그램")
print("&시급&")
print("주간근무 : 9500원")
print("-야간근무 : 주간급무 *1.5")
print()

hour_pay = 9500

a = int(input("시작시간 "))
work_time = int(input("끝난시간을 입력"))

if a >= 6 or  a<=22 and work_time : 
    day_night = '주간'
    pay = hour_pay*work_time
else : 
    day_night ="야간"
    pay = hour_pay*work_time*1.5
print("%d 동안 일한 %s 급여는 %.0f원입니다."%(work_time,day_night,pay))


