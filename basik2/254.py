def hello():
    print('hello')
for i in range(20):
    hello()

def jj():
    sum = 0
    for i in range(1,101):
        sum +=i 
    print(sum)
jj()
jj()#함수 호출

def k():
    print('-'*50)

def j(uStart,uEnd):
    sum = 0
    for i in range(uStart,uEnd +1):
        sum = sum +i
    print('%2d부터 %2d의 합은 %5d'%(x,y,sum))
x=int(input("시작수를 입력"))
y = int(input("끝수를 입력"))
k()#함수 호출
j(x,y)
    