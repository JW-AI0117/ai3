#배수 구하는 코딩
'''3
num = int(input("양의 정수를 입력하세요"))
result = "3의 배수도 4의 배수도 아니다." # 아닐경우는 이 문장 출력

if num%3 ==0:
    result = "3의 배수이다"
if num %4 ==0:
    result = "4의 배수이다."
if num%3 == 0 and num%4==0 :
    result='3의 배수이면서 4의 배수이다.'
   
print("%d는 %s"%(num,result))
'''


num = int(input("양의 정수를 입력하세요"))

if num%2 == 0 or num%4==0 :
    print("행운의수")
else  : 
    print("%d입니다"%num) 

