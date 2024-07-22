def add(a,b):
    c =a+b
    print('%d +%d =%d'%(a,b,c))
add(12,15)
add(245,300)
add(-38,-12)

def sum_int(start,end):
    sum = 0
    for i in range(start,end+1):
        sum +=i
    print('%d ~%d의 합계 : %d'%(start,end,sum))

start = int(input('첫번째 정수'))
end = int(input("마지막 정수"))
sum_int(start,end)

def member(*args):
    result =""
    for i in args in args:
        result = result+args + ''
    print('가입회원 : %s' %result)
member('이재율','이재율')