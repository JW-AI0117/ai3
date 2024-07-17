# n =1
# count = 0
# sum = 0
# while n <=100:

#     if n %2 ==1 :
#         sum = sum+n
#         print('%6d'%sum,end="")
#         count = count+1

#         if count %10 ==0:
#             print()

#     n = n+1
#++++++++++++++++++++++++++++++++++++++++++++++

# print("-"*40)
# print('%4s  %4s   %4s'%('달러','원화','유로'))
# print("-"*40)
# d = 10
# while d <=100:
#     won = d * 1080
#     e = d * 0.81
#     print('%7d %8d %7.1f'%(d,won,e))
#     d += 10
# print("-"*40)
#++++++++++++++++++++++++++++++++++++++++++++++
# x = input("문장을 입력해주세요")
# i = len(x)-1
# while i>=0:
#     if x[i] == " ":
#         print('-',end="")
#     else :
#         print('%s'%x[i],end="")
#     i = i-1

'''
x=0
for i in range(1,11,1):
    if i%2 == 1:
        print(i)
print()
x = 0
for x in range(1,101,1):
    if x %5 == 0 :
        print(x,end=" ")
print()
x = 0
sum = 0
for x in range(1,101,1):
    if x %3==0:
       sum = sum+x
       
print("3의 배수의 합계 %d"%sum,end=" ")
print()
x=0
cnt =0
for x in range(1,101,1):
    if x %5 ==0:
        print(x,end=" ")
        cnt = cnt+1
        if cnt %5 == 0:
            print()
'''
'''
x =0
y = 0
for x in range(1,101,1):
    if x %4 ==0:
      y = x+y
      print('%d -->%d'%(x,y))
print()

x = 1
for i in range(1,11):
    x=x*i
print("10!=%.0f"%x)

x = 1
i = 1
while i<10:
   i = i+1
   x  = x*i
print(x)
'''

# print('-'*40)
# print('%5s,%5s,%5s,%5s'%('cm','mm','m','inch'))
# mm = 0
# m = 0.0
# inch = 0
# for cm in range(1,51,1):
#     mm = mm +10
#     m = m +0.01
#     inch = inch +0.3937
#     print('%4d %4d %.2f %.2f'%(cm,mm,m,inch))
'''
print()
print('-'*40)
print('%5s,%5s,%5s,%5s'%('cm','mm','m','inch'))
mm = 0
m = 0.0
inch = 0
cm = 0
while cm <50:
    cm = cm +1
    mm = mm +10
    m = m +0.01
    inch = inch +0.3937
    
    print('%4d %4d %.2f %.2f'%(cm,mm,m,inch))
print()
'''
x = 1
cnt = 0
while x<=1000 :
    
    if x %3!=0:
        print(x,end=' ')
        x = x+1
        cnt = cnt+1
    else :
        x = x+1
    if cnt %10 == 0:
        print()
        
    
         
