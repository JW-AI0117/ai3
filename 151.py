# for word in range(5):
#     print()
#     phone = input("하이픈을 포함한 휴대폰번호를 입력하세요")
    
#     for x in phone:
#             if  x != "1" :
#                 print('%s'%x,end="")

hp = input("핸드폰 번호를 입력해주세요")    
for i in hp :
    if not( 'A'<=i<='Z'or 'a'<=i<='z' or '0'<=i<='9'or '가'<=i<='힣'):
        print("%s"%i, end="")
    