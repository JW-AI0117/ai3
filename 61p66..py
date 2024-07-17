score =80
print("성적"+ str(score))

x = "토끼" *10
print(x)

n=100
print(str(n))
n = str(n)
print(type(n))
print(n*10)

n200 =200
print(str(n200))
n200 = str(n200) #print (str(n200)*15)
print(n200* 10)

y= 80
str(y)
y =str(y)
print(type(y))

date = "20220301"
year = date[0:4]
month = date[4:6]
day = date[6:]
date2 = year+"-"+month+"-"+ day
print(date2)

x = "ㄴㅇㅁㄴ"
n = len(x)
print (str(n))

x = "이재율"
y = "01031415126"
index =  y [10]
print(index)
print(int(index))
print("이재율" * int(index))

phone1 = '82-10-3141-516'
phone2 = '82-10-4141-2222'
'''
if len(phone1)== 15 : print("phone1은 폰번호")
else : print("phone2 는 집번호") 

if len(phone2)== 14 : print("phone2은 집번호")
else : print("phone1 는 폰번호")

'''

if len(phone1) == 15 and len(phone2) == 15 : 
    print("phone1은 핸드폰번호 입니다.")
    print("phone2는 핸드폰번호입니다.")
elif len(phone1) == 15 and len(phone2) == 14:
    print("phone1은 핸드폰번호 입니다.")            #and 이프문 입니다.
    print("phone2는 집번호입니다.")

if len(phone1) == 14 and len(phone2) == 15 : 
    print("phone1은 집번호 입니다.")
    print("phone2는 핸드폰번호입니다.")
elif len(phone1) == 14 and len(phone2) == 14:
    print("phone1은 집번호 입니다.")
    print("phone2는 집번호입니다.")

    

        









