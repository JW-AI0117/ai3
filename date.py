# import requests as req
# url = "https://search.naver.com/search.naver"
# rdate =req.get(url,params={'query':'백일해 증상'})
# print(rdate.text)

names = ['a','b','c']
x = '/'.join(names)
print(x)
numbers = [[10,20,30],[40,50,60],[70,80,90,100]]
print(numbers[1][1])
print(numbers[2])
print(numbers[2][0])
print('!')
i = 0
for i in range(len(numbers[0])):

    for j in range(0,len(numbers[i])):
        print(numbers[i][j],end=" ")
    print()
list3D = []

x = [[1,2,3,4],[5,6]]
for i in range(len(x)):
    for j in range(len(x[i])):
        print('%d'%x[i][j])
print()
list3D = [[[1,2,3],[4,5]],[[6,7],[8]]]
print(list3D[1][1][0])
print(list3D[0][0][2])

ok = ['s_hool','compu_er','deco_ation','windo_','hi_tory']
pw = ['c','d','r','w','d']

# for i in range(len(ok)):#ok 변수 길이만큼 반복이니싼 5번반복

    
#     q ='%s 의 들어갈 영어단어는?'%ok[i]
#     k =input(q)
#     if k == pw[i]:
#             print('맞음')
#     else:
#             print('틀림')

# sc = []
# while True:
#      x = int(input('성적을 입력하세요(종료시-1입력)'))
#      if x == -1:
#         break
#      else :
#           sc.append(x)
# sum = 0
# avg = 0
# for i in sc :
#      sum = sum+i
#      avg = sum/len(sc)
# print('합계%d, 평균 %.0f'%(sum,avg))
# print()

# s = [64,89,100,85,77,58,79,67,96,87,\
#      87,66,82,98,94,76,63,69,63,22]
# soo = 0
# woo =0
# mi =0
# y = 0
# ga = 0

# i = 0
# while i <len(s):
#     if s[i] >= 90 and s[i]<=100:
#         soo = soo+1
#     if s[i]>=80 and s[i]<=89:
#         woo +=1
#     if s[i]>=70 and s[i]<=79:
#         mi +=1
#     if s[i]>=60 and s[i]<=69:
#         y +=1
#     if s[i]>=0 and s[i]<=59:
#         ga +=1
#     i +=1
# print('수 %d명'%soo)
# print('우 %d명'%woo)
# print('미 %d명'%mi)
# print('양 %d명'%y)
# print('가 %d명'%ga)

sit =[[0,0,0,0,0,0,0,0,0,0],\
      [0,0,0,0,0,0,0,0,0,0],\
      [0,0,0,0,0,0,0,0,0,0],\
      [1,1,1,0,0,0,0,0,1,0],\
      [0,0,0,0,0,1,0,0,0,0],\
      [0,1,0,0,0,1,0,1,0,0],\
      [0,0,0,0,0,0,1,0,0,0],\
      [1,0,1,0,0,0,0,0,0,1]]

for i in range(len(sit)):
    for j in range(len(sit[i])):
        if sit[i][j]==0:
            print('%3s'%'□',end="")
        else:
            print('%3s'%'■',end="")
    print()

list1 = [[1,2,3,4],[5,6,7]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j])

file_name = ['file1.py','file2.txt','file3.pptx','file4.doc']
list2 = []
for i in file_name:
    x = i.split('.')
       
    print('%s => 파이명:%s,확장자%s:'%(i,x['0'],x))    
    
