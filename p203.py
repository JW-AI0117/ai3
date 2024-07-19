date = [12,6,3,5,9,22,99,82,1]
print(date)
date.sort()
print(date)

date2 = ['a','ㅅ','*','ㄴㄴ','123','tt']
print(date2)
date2.sort()#유니 코드 순서대로 정렬된다.
print(date2)
date2.sort(reverse=True)
print(date2)
#오름차순
date2.sort(reverse=False)
print(date2)
strung1 = ['사과는 맛있다 나는 사과를 제일 좋아한다 사과']
print()

x = strung1[0].replace('사과','딸기',2)

print(x)
strung1 =[x]
print(strung1)

hello = 'have-a-nice-day'
print(hello)

list1 = hello.split('-')
print(list1)
print(type(list1))

for i in range(0,len(list1)):
    print('list1[%d]: %s' %(i,list1[i]))

list2 = 'a,b,c,d,w,s,dh,h'
x = list2.split(',')
list22 =[]
for y in range(0,len(x)):#나누어버린 값의 길이를 구하기
    print('[%d] [%s]'%(y,x[y]))
    for j in x :
        list22.append(j)
print(list22)


# list4 = '이재율:100:20','홍길동:60:70'
# k = list4.split(',')
# print(list3)
# print(type(list3))

# for j in range(0,len(list3)):
#     print('[%d] [%s]'%(j,list3[j]))
list= ['kbs-사장-200','mbc-부장-100','kbs-사원-200','mbc-대리-100']
for i in range(0,len(list)):
    list2 =i.split('-')