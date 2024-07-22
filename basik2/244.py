score = {'김채린':85,'박수정':98,'함소희':94,'안예린':90,'연수진':93}
sum = 0
for i  in score:
    sum = sum + score[i]
    print('%s : %d'%(i,score[i]))
age = sum/len(score)
print('합계 : %d 평균 : %.2f '%(sum,age))

admin_id = {'id':'admin','pw':'12345'}

input_id = input("아이디를 입력:")
input_pw = input('비밀번호를 입력')

if input_id == admin_id['id'] and input_pw == admin_id['pw']:
    print('정보에 접근권한이  있습니다.')
else :
    print('접근 권한이 없습니다.')

words = {'꽃':'flower','나비':'butterfly','학교':'school','자동차':'car','비행기':'airplane'}

print('<영어단어 맞추기>')

for i in words:
    input_word = input("%s 해당영어단어를 입력해주세요"%i)

    if input_word == words[i] :
        print('정답입니다.')
    else:
        print('땡 틀렸습니다.')
        
