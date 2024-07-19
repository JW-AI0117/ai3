
member1 = [1,2,3,4,2,2,2,2,2,2]
member1.remove(2)
print(member1)

member1.pop(2)
print(member1)

member1.clear()
print(member1)
p1 = [1,3,5]
p2 = [1,6,7]
print(p1,p2)
print()

p4 = list(range(1,11))
print(p4)
sm = sum(p4)
print(sm)       #for i in p4:
                # sum +=i print(sum)
avg = sm/len(p4)
print(avg)     

# p4max = max(p4)
# print(p4max)
# p5 = [1,2,3,4]
# p5.remove()
# print(p5)
p6 = ['apple','apple','banana','orange']
print(p6,'!')
p6Copy = p6.copy()
print(p6Copy)
p6.remove('apple')
print(p6)
p6.pop(0)
print(p6)
p6Copy[3]  = 'manggo'
print(p6Copy)

print('=====')
#p7하고 p77은 같은 주소를 쓴다(같은 메모리),(얕은 복사)
p7 = ['apple','apple','banana','orange']
p77 = p7
print(p77)
print(p7)
p7.remove('apple')
print(p7)
#p7에 있는 에플 삭제
print('====!')
p77[2] = 'mango'
#p77 에있는 오렌지 망고 교체
print(p77)
print('=====')
p7.append('bear')
#bear 추가
print(p7)
