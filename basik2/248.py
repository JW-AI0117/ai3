year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}

for key in year_sale:
    if year_sale['2017'] == year_sale[key] :
        print('%s 년 자동차판매량 : %d '%(key,year_sale[key]))
print('!!!!!!!!!!!!')

year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}

sm = 0
for i in year_sale:
    if year_sale['2018'] == year_sale[i] or year_sale['2019'] == year_sale[i]:
        print('%s년 자동차 판매량 : %d'%(i,year_sale[i]))
        sm = sm + year_sale[i]
print('2년간 자동차 판매량 : %d대'%sm)

sm1 = 0
for i in year_sale:
    sm = sm + year_sale[i]
avg = sm/len(year_sale)

print('5년간 총 판매량 %d'%sm)
print('5년간 평균 판매량 %d'%avg)

year_sale = {'2016':237,'2017':300,'2018':158,'2019':233,'2020':120}
big_year = 2016
buggest = year_sale['2018']
for j in year_sale:
    if year_sale[j]>buggest:
        big_year = j
        buggest = year_sale[j]
print('판매량이 가장 많은 해 : %s년'%big_year)
print('판매량 : %d대'%buggest)


person = {'name':'홍길동','age':'30','family':5,'children':['선미','성진','소영'],
          'pets':['강아지','고양이','이구아나']}
for key in person:
    if key == 'pets':
        for name in person[key]:
            print(name)
for key in person:
    if key == 'children':
        for name in range(len(person[key])):
            print(name)

temp = {'월': 15.5,'화':17.0,'수':16.2,'목':12.9,'금':11.0,'토':10.5,'일':9.3}

print('-'*60)
for i in temp:
    print(i,end=" ")
print()
print('-'*60)
for j in temp:
    print(temp[j],end=" ")
print()
print('-'*60)

sum = 0 
for x in (temp):
    sum = sum+temp[x]
    avg = sum/len(temp)
print('일주일간 기온 평균 :%.1f'%avg)
low = temp['월'] # 15.5
low2 = '월'
for i in  temp:
    if temp[i]<temp[low2]:
        low2 = i
        low = temp[low2]
print('요일:%s'%low2)
print("최저 기온 %s"%low)



        

