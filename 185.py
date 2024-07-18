'''
ccolors = ['빨강','파랑','노랑','초록']
for color in ccolors:
    print('나는%s을 좋아한다'%color ,end="  ")
print()
n = len(ccolors)
for i in range(0,n):
    print('나는 %s를 좋아한다'%ccolors[i])

animals = ['코끼리','호랑이','사자','펭귄','코알라']
i = 1
while i<len(animals):
    print(animals[len(animals)-i],end=" ")
    i+=1

sum = int(input("1"))
sum2 = int(input("2"))
list5 = [sum,sum2,sum+sum2,(sum2+sum)%2]
print(list5)
'''

list1 = ['홍길동',70,80]
list2 = ['이순신',90,75]
list3 = ['최경미',50,100]

print('이름','국어점수', '수학점수','합계','평균')

print(list1[0],'',list1[1],'   ',list1[2],'    ',(list1[1]+list1[2]),' ',(list1[1]+list1[2])/2)
print(list2[0],'',list2[1],'   ',list2[2],'    ',(list2[1]+list2[2]),' ',(list2[1]+list2[2])/2)
print(list3[0],'',list3[1],'   ',list3[2],'    ',(list3[1]+list3[2]),' ',(list3[1]+list3[2])/2)

list4 = ['홍길동','이순신','최경미']

print('우리반 이름%s'%list4)

#print("우리반 국어점수 합계: %d"%(list1[1]+list2[1]+list3[1]))
#print("우리반 영어점수 합계: %d"%(list1[2]+list2[2]+list3[2]))
'''
if list3[1]<list2[1]<list1[1] or list2[1]<list3[1]<list1[1]:
    print("우리반 에서 국어점수 가장높은사람: %s"%list1[0])
elif list1[1]<list3[1]<list2[1] or list3[1]<list1[1]<list2[1]:
    print("우리반 에서 국어점수 가장높은사람: %s"%list2[0])
elif list2[1]<list1[1]<list3[1] or list1[1]<list2[1]<list3[1]:
    print("우리반 에서 국어점수 가장높은사람: %s"%list3[0])


x = input("찾고싶은사람")
if x == list1[0] or x == list2[0] or x == list3[0]:
    print('우리반에 %s가 있어요'%x)
else :
    print("우리반에 %s가 없어요"%x)
'''





