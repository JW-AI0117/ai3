# x  = int(input("점수를 입력하세요:"))

# if not x <100 :
#     print("입력오류!")
# elif x >=90 and x <=100 : 
#     print("-성적%d점,등급:수"%x)
# elif x >=80 and x <=89 : 
#     print("-성적%d점,등급:우"%x)
# elif x >=70 and x <=79 : 
#     print("-성적%d점,등급:미"%x)
# elif x >=60 and x <=69 : 
#     print("-성적%d점,등급:양"%x)
# elif x >=0 and x <=59 : 
#     print("-성적%d점,등급:가"%x)
#==========================================================================
# x = int(input("첫번째 시간을 입력하세요"))
# y = int(input("첫번째 시간의 분을 입력하세요"))
# x2 = int(input("두번재 시간의 시를 입력하세요"))
# y2 = int(input("두번재 시간의 분을 입력하세요"))

# if not (x<24 and x>0 and y <59 and y>0 )or not (x2<24 and x2>0 and y2 <59 and y2>0 ):
#     print("시간과 분을 다시 입력해주세요")
# elif x >=0 or x<=24  and  y>=0 or y<=59:
#     print("-빠른시간 : %d시:%d분"%(x,y))
# if x2 >=0 and x2<=24  and  y2>=0 and y2<=59:
#     print("-늦은시간 : %d시:%d분"%(x2,y2))


# name = input("이름을 입력하세요")
# time  = int(input("일주일간 일한 시간을 입력하세요 :"))
# print("="*40)
# overtime = time - 40 
# x = 12000
# pay  = (time-overtime) *x
# pay2  = overtime*(x*1.5)
# result = pay+pay2
# print("이름:%s"%name)
# if  not time >0  :
#     print("오류입니다. 다시 입력해주세요")
# if time <=40 and time > 0  :
#     print("일주일간 일한시간: %d"%time)
#     print("주급은 %d원 입니다."%pay)
# elif time>=41  :
#     print("일주일간 일한시간: %d"%time)
#     print("-오버타임: %d"%overtime)
#     print("총 수당 : %d "%result)
# print("수고하셨습니다.")

test = input("등급을 입력해주세요(A+,A,B+,B,C+,C,D+,D,F)")
if  not (test == "A+" or test == "A" or test == "B+" or test == "B" or test == "C+" or test == "C" or test == "D+" or test == "D" or test == "F"):
    print("다시입력해주세요") 

elif test == 'A+' :
    print("등급:A+,평점:4.5")

elif test == 'A' :
    print("등급:A,평점:4.0")

elif test == 'B+' :
    print("등급:B+,평점:3.5")

elif test == 'B' :
    print("등급:B,평점:3.0")

elif test == 'C+' :
    print("등급:C+,평점:2.5")

elif test == 'C' :
    print("등급:C,평점:2.0")

elif test == 'D+' :
    print("등급:D+,평점1:.5")

elif test == 'D' :
    print("등급:D,평점:1.0")

elif test == 'F' :
    print("등급:F,평점:0")
    print("재수강")


    

     