list= ['kbs-사장-200','mbc-부장-100','kbs-사원-200','mbc-대리-100']
list2 =[]
list3  = []
for i in list:
    list2 =i.split('-')
    print(list2, end=" ") 
    
    print('!!!')
    print()
    for j in list2:
        list3.append(j)
print(list3)

list4 = ['안녕하세요+','반갑습니다+','200']
list5 =[]
list6 = []
list7 = []
for i in list4:
    list5= i.split('+')
    for j in list5:
         list7 =j.split(',')
         for k in list7:
             list6.append(k)
print(list6)