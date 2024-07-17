
'''year = input("년은?")
month = input("월은?")
day = input("일은?")
print (year,month,day,sep=".")

width = int (input("사각형의 너비는?"))
height = int(input("사각형의 높이는?"))
leght = 2* width + 2*height
area = width*height
print ("사각형의 너비 : %dcm"  %width)
print ("사각형의 높이 : %dcm " %height)
print("둘레길이 : %dcm " %leght)
print("면적 : %dcm2" %area)

r= float(input('반지름을 입력하세요 :'))
leght = 2 * 5.3 * 3.14
area = 5.3**2 *3.14

print("반지름 : %.2f cm "%r)
print("원의 둘레: %dcm " %leght)
print("원의 면적 : %.2fcm2" %area)
'''

inch = float(input("인치는?"))
cm = inch *2.54
print("%.1f inch ,%.1f cm"%(inch,cm))

price = int(input("책 값은?"))
discount = int(input("할인률은?"))
delivery = int(input("배송료는?"))

pay = price - (price*(discount/100))+delivery

print("책값 : %d" %price)
print("할인율 : %d" %discount)
print("배송료 %d" %delivery)

print("결제금액 %0f원 "%pay)



