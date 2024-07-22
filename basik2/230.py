animals = ('토끼','거북아','사자','여우')
print(animals)
numbers = tuple(range(10))
print(numbers)

print (animals[1:])
print(numbers[:3])

# animals[2] = '항아리'#튜플은 수정이 안된다.
n = tuple(range(10,21))
print(n)

t = animals+numbers
print(t)

n2 = tuple(range(101))
sum = 0
for i in n2 :
    sum = sum+i

print(sum)

dans = (2,3,4,5,6,7,8,9)

for i  in dans:
    print(str(i)+'단')
    for j in range(1,10):
        print("%d x %d = %d"%(i,j,i*j))

words = {'door':'문','chair':'의자','table':'책상','house':'집'}
print(words)
words['table'] = '테이블'
print(words)

words['house']= '하우스'
print(words)

car = {'brand':'현대','model':'현대','start':'1990','year':'2021'}

print(car)

x= car.pop('start')
print(x)
print(car)

area_code = {'서울':'02','부산':'051','대구':'503','광주':'062'}
for i  in area_code:
    print('%s 지역번호 %s'%(i,area_code[i]))
