# char = int(input("수를 입력하세요"))

# if char ==0 or char <=9 :
#     print("%d는 한자리 숫자이다."%char)
# elif char ==10 or char <=99 :
#     print("%d는 두자리숫자이다."%char)
# elif char ==100 or char <=999 :
#     print("%d는 세자리숫자이다."%char)
# else :
#     print("%d는 범위 이외의 숫자이다."%char)



# x = input("문자열을 입력하세요:")
# y = len(x)
# if len(x) %2 ==0 :
#     print("문자열의 개수 %d"%y)
#     print("문자열의 갯수는 짝")
# else :
#     print("문자열의 갯수 %d"%y)
#     print("문자열의 갯수는 홀수이다.") 

char = int(input("첫번째 숫자를 입력하세요."))
num2 = int(input("두번재 숫자를 입력하세요"))
print("1= + 2= - 3= * 4= /")
x = int(input("1,2,3,4 중 고르세요:"))

if x == 1 :
    print("%d + %d = %d"%(char,num2,char+num2))
elif x == 2 :
    print("%d - %d = %d"%(char,num2,char-num2))
elif x == 3 :
    print("%d * %d = %d"%(char,num2,char*num2))
elif x == 4 :
    print("%d / %d = %d"%(char,num2,char/num2))
else :
    print("다시 선택해주세요")


    