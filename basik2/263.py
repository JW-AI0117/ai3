def average(*args):
    num_args = len(args)
    sum = 0
    for i in range(num_args):
        sum = sum + args[i]

    avg = sum/num_args
    print('%d 과목평균 %.1f'%(num_args,avg))

average(85,77,88)
average(88,11,22,44,59)

def func(food):
    for x in food:
        print(x)

fruits = ['사과','오렌지','바나나']

func(fruits)

def func(food):
    food.append()

