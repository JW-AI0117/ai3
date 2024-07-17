age = int(input("당신의 나이는?"))
ticket = 2000

if age>= 50 :
    ticket = 0

if age >=10 and age <=20 :
    print("입장료1500원")
elif age>=5 and age<=9:
    print("입장료 1200원")
elif age>=0 and age<=4  : 
    print("입장료 :1000원")    
else : print("%d원"%ticket)
