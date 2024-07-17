# word = "i am Happy"
# for i in word :
#     print(i,end="")

# phone = "010-8744-3334"

# print(phone)
# for i in phone:
#     if i =="5":
#         print("있어요")
#     else:
#         print("없어요")
#         break

# x = input("!!")
# flag =0
# for i in x:
#     if i =="5" :
        
#         flag = 1
# if flag == 0:
#     print("없어요")
# else:
#     print("있어요")

for j in range(0,3):

    x = input("영어를 입력")
    flag = 0
    for i in x:
        if i == 'a':
            flag += 1

    if flag == 0:
        print("업굥")
    else:
        print("%d개 있어요"%flag)
