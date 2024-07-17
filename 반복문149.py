# x = 0
# sum = 0
# for i in range(20,51,2) :
#     print(i,end=" ")
#     x = x+1
#     sum = sum + i

# print()
# print("갯수는 %d " %x)
# print("갯수의 합은 %d" %sum)
# sum =0
# cnt = 0
# for i in range(100,-1,-5):
#     print(i,end=" ")  
#     cnt = cnt+1
#     sum = sum+i
#     p = sum / cnt
# print()
# print("평균은 %.0f"%p)
# print("평균 : %.01f"%(sum//cnt))   
# print("갯수는 %d"%cnt)
# print("합은 %d"%sum)
# sum = 0
# for i in range(1,101,1):
#     sum = sum+i
#     if  sum >= 400 :
#         print("합계가 400이 넘는 순간 %d"%i)
#         break
        
# print(sum)
# cnt = 0
# for i in range(200,500,3):
#     print(i,end=" ")
#     cnt = cnt+1
#     if cnt ==20 :
#         break
# print()
# print("20개일때 i값은 %d 입니다."%i)
# cnt = 0
# sum = 0
# for i in range(5,501,5):
#     cnt = cnt+1
#     sum = sum+i
#     if cnt ==30 or sum>=1000:
#         break
#     print(i ,end=" " )
# print()
# print("갯수의 값은 %d"%cnt)
# print("합계의 값은 %d"%sum)    

# cnt = 0
# sum = 0

# for x in range(3,101,3):
#     cnt = cnt +1
#     sum = sum+x
#     print(x,end=" ")
#     if cnt == 20 or sum>=200 :
#         break
# print()
# print("갯수가 20개이상이나 총수가 200개 이상이떄 값은 %d,%d,%d"%(x,sum,cnt))

count = 0
tt = 0
for h in range(200,1000,10):
    count+=1
    tt = tt+h
    print(h , end=" ")
    if count >= 40 or tt >=5000 :
        break
print()
print("40번째 값은 %d 이고 총합은 %d이다."%(count,tt))
print("평균은 %.0f"%(tt//count))



        


    