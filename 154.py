# count = 0
# for x in range(200,801,1):

#     if x %5!=0  :
#         print('%d'%x, end=" ")
#         count=count+1
#         if count %10 == 0 :
#          print()

# print("-"*40)
# print(' cm      mm      m       inch')
# print("-"*40)

# for cm in range(1,101,1):
#     mm = cm*10.0
#     m = cm*0.01
#     inch = cm*0.3937
#     print("%5d       %5d      %.2f      %.1f"%(cm,mm,m,inch))

# print('-'*40)

# for i in range(1,11):
#         print('*'*i ,end="")
#         print()
# for i in range(1,11):
#         print('*'*(10-i) ,end="")
#         print()

# num1 = input("숫자를 입력하세요")
# x = 0
# for i in num1 :
#    i = int(i)
#    if not(i %2 == 0):
#       x +=1 
# print('홀수의 갯수 %d개'%x)

print("-"*40)
print("킬로그램     파운드      온스")
print("-"*40)
for kg in range(100,201,2):
    pound = kg*2.204623
    ons = kg*35.273962

    print("%5d      %.01f       %0.01f"%(kg,pound,ons))
    

