def sunc(c):
    x = c+5
    return x
r = sunc(100)
print(r)

def i(inch):
    cm = []
    for i in range(inch,31,10):
        k =i*2.54
        cm.append(k)
    return cm
list1 = [10,20,30]


result = i(10)
print(result)
# num = int(input("인치를 입력하세여"))
# result = i(num)
# print('%d inch == %.2f cm'%(num,result))

def pak(n):
    k= []
    answer = 1
    for i in range(n,0,-1):
        e = answer*i
    k.append(e)
    answer=0
    for i in range(1,n+1):
        e = answer+i
    k.append(e)
    for i in range(1,n+1):
        e = answer+1
    k.append(e)
    
    return k



print(pak(5))

def p(x) :
    a = 1
    b = 0
    cnt=0
    for i in range (x,0,-1) :
        a = a * i
        b += i
        cnt+=1
    list1 = [a,b,cnt]
    return list1

print(p(6))
        
        
