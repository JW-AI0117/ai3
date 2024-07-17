s= "안녕하세요. 반갑습니다."
print(s)
print(s[0] + s[1])
print(s[ 7 : 117 ])
string = "쥐 구멍에 볕들날 있다."
print(string[2:8])
animal = "tiger"
print(animal[0:2])

jumin = "991013-3012585"
print(jumin[0:2] +"년" ,jumin[2:4]+"월" ,jumin[4:6]+"일")
sex= (jumin[7])
print(sex)
if sex == '1' or sex == '3' : #문자형으로 해줘야한다 
    print("남자")
else :
    print("여자")

a = jumin[-1]
print(a)
print(int (a))
a = int(a)
if a % 2 == 0 :
    print('맞는 주민번호')
else :
    print('틀린 주민번호')

x = "12345"

b = x[4]
print(b)
print (int(b))
bint = int(b)
if bint % 2 ==0 :
    print("짝수")
else :
    print("홀수")


 


