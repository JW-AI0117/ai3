''' nameList = ['a','b']
    nolist = list(range(241001,241021))
    print(nolist)
    print(nameList[1])
    for i in nolist:
    
        print(i,end=" ")
    print()
    print('='*40)
    x =0
    while x <len(nolist):
        print(nolist[x],end=" ")
        x +=1
    name = ['이순신','홍길동','박수연']
    name[2] = '박수형'
    print(name)
    for i in name:
        print(i,end=" ")
    name.append('이재율')
    print(name,end=" ")
    print()
    name.insert(1,'이정후')
    print(name)
    for i in name:
        print(i,end=" ")
    print()

    try:
        name = ['박수형','이순신', '이승후', '홍길동', '박수현', '정현희']
        x=name.index('박수형',0,10)
        print(x)
        y=name.index('이수형',1,10)
        print(y)
    except ValueError : 
        print("이수형은 없습니다")
'''  






