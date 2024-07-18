# list1 = [3,15,-12.5,'사과','딸기',True,False]
# list = list(range(1,21,2))
# print(list1,list) 
# print(list1[1])
# for i in range(7):
#     print(list1[6-i], end=" ")
# print()
# print(list[0::2])
# print(list[-1::-2])

#응용문제 100 110 120 ...200
list3 = list(range(100,201,10))
print(list3)
cnt = 0 
sum =0
for list3 in list3:
    cnt +=1
    sum = sum+list3
print('갯수는 %d개'%cnt)
print('합계는 %d'%sum)
print(len(list3))


   

