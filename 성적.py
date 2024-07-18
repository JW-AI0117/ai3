'''
---------------------
성적관리 프로그램
---------------------

1. 학생 이름 삽입하기
   이름? 
2. 성적 입력하기
    누구의 성적 입력하래요? 홍길동
    국어점수 ?
    영어점수 ?
    수학점수 ?
3. 통계자료 보기
   1) 반 전체 통계
   2) 학생 통계 
4. 학생 자료 삭제하기
   삭제하려는 학생이름 ? 
5. 프로그램 종료하기 

==> 메뉴를 선택하세요(1/2/3/4/5)

'''
name = []
kor = []
eng = []
math = []
menu ='0'
while menu != '5':
    print('-'*40)
    print('성적관리 프로그램')
    print('-'*40)

    print('1. 학생 이름 삽입하기')
   
    
    print('2. 성적 입력하기')
    
    print('3. 통계자료 보기')
    
    print('4. 학생 자료 삭제하기')
   
    print('5. 프로그램 종료하기')
    menu =input('==> 메뉴를 선택하세요(1/2/3/4/5)')

    if menu == '1':
        hong = input("학생이름은?")
        name.append(hong)
        print(name)
    elif menu == '2':
        try:
            k = int(input("국어점수?"))
            e = int(input("영어점수?"))
            m = int(input("수학점수?"))
            kor.append(k)
            eng.append(e)
            math.append(m)
            print(kor,eng,math)
        except: print("점수는 숫자")
    elif  menu == '3':
        print('1학생통계')
        print('2통계자료')
        print('3통계자료 나가기')
        menu1 = (input("번호를 선택하세요(1,2,3)"))
        if menu1 == '1':
            for x in range(len(name)):
                
                print('%s %d %d %d'%(name[x],kor[x],eng[x],math[x]))
       
        elif menu1 =='2' :
    
           oknamm = -77 
           name2 = input("통계룰 볼 학생은?")
        try :
                sindex = name.index(name2)
                print('%s %d %d %d'%(name[sindex],kor[sindex],eng[sindex],math[sindex]))
        except ValueError :
                print('%s는 우리반 학생이 아닙니다.'%name2)
                print('문장을입력')
                

           
        '''
            for y in range(len(name)):
              if name2 == name[y]:
                  oknamm = y
                  break
            if oknamm == -77:
                print('%s는 우리반이 아닙니다.'%name2)
            else : 
                print('%s %d %d %d'%(name[oknamm],kor[oknamm],eng[oknamm],math[oknamm]))
        '''
            
    elif  menu == '4':
        delname =input('삭제하려는 학생의 이름은?')
        try : 
             sindex = name.index(delname)
             name.pop(sindex)
             kor.pop(sindex)
             eng.pop(sindex)
             math.pop(sindex)
             print("삭제 되었습니다.%s"%sindex)
        except ValueError:
             print('%s 우리반 학생 아님'%delname)
 
        

       
