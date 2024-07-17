
# yn = 'y'
# while yn == 'y':
#     n1 = int(input("숫자1 : "))
#     n2 = int(input("숫자 2 :"))
#     sum = n1+n2
#     print("합계는 %d"%sum)
#     yn = input("계속 하시겠습니까 y or n")
#----------------------------------------------
# a = 2 
# for b in range(1,10):
#     print('%dx%d = %d'%(a,b,a*b))


# for a in range(2,10):
#     for b in range(1,10):
#         print('%dx%d = %d'%(a,b,a*b), end="")
#         print()
# yn = 'y'
# while(yn == "y"):
#     he = input("문자:")
#     love = input("문자 2:")
#     ws = ''
    
#     for i in range(len(he) + len(love)):
#         if i <= len(he)-1: #i<=4 0, 1, 2, 3, 4
#             ws = ws +he[i]
#         if i <= len(love)-1 : # i<=3 0,1,2,3
#             ws = ws +love[i]
        
#     print(ws , end="") 
#     print()
#     yn = input("계속할래요?")   

# yn = 'y'
# while True :
#     he = input("문자:")
#     love = input("문자 2:")
#     ws = ''
    
#     for i in range(len(he) + len(love)):
#         if i <= len(he)-1: #i<=4 0, 1, 2, 3, 4
#             ws = ws +he[i]
#         if i <= len(love)-1 : # i<=3 0,1,2,3
#             ws = ws +love[i]
        
#     print(ws , end="") 
#     print()
#     yn = input("계속할래요?") 
#     if yn == 'n':
#         break

i=1
for i in range(1,201,1):
    if i ==100 :
        continue

    print(i,end=" ")
    
print()
print('-'*40)
i=0
while i<200:
    i =i+1
    if i ==100:
        continue
    print(i,end=" ")
   
   

    
        
            
    


