# print('@')
# print('@', '@')
# print('@', '@', '@')
# print('@', '@', '@', '@')
# print('@','@', '@', '@', '@')

# print('1')
# print('2', '2')
# print('3', '3', '3')
# print('4', '4', '4', '4')
# print('5', '5', '5', '5', '5')
# print('6', '6' ,'6' , '6')
# print('7', '7', '7')
# print('8', '8')
# print('9')


# x = int(input('Введите число таблицу умножения которого хотите узнать '))
# y = 1
# while y<=9:
    # print(x,'*',y,'=', x*y)
    # y+=1

# cube1 = int(input('Число на первом кубике '))
# cube2 = int(input('Число на втором кубике '))
# cube = [1,2,3,4,5,6]
# 
# if  cube1 in cube:
    # if cube2 in cube:
        # Sum_cubs = cube1+cube2
        # if Sum_cubs == 7 or Sum_cubs == 11:
            # print('Я победил!!!')
        # elif Sum_cubs == 2 or Sum_cubs == 3 or Sum_cubs == 12:
            # print('Я проиграл :(')
        # else:
            # print(Sum_cubs)
    # else:
        # print('Ошибка! Значение на кубике 2 не входит в интервал [1, 6], вставьте подходящее значение!')
# else:
    # print('Ошибка! Значение на кубике 1 не входит в интервал [1, 6], вставьте подходящее значение!')




# for i in range(3000,4300):
    # Delimost5 = i % 5
    # Delimost11 = i % 11
    # if Delimost11 == 0 and Delimost5 != 0 :
        # print(i)
        # i +=1
    # else:
        # i +=1


sample_list = ['мандаринки', 'киви', 'лимон']
n = int(input('Введите произвольное целое число '))
x = str(n)
x1 = x - (x - 1)
i = 1
i_int = 1
n2 = (int(n)) - ((int(n))-1)
while i_int <= n:
    while n2 <= n:
        for i in x:
            sample_list.append = sample_list[0] +'_'+n2
            print(sample_list[i_int] )
            i_int = i_int + 1
sample_list[0]= sample_list[0]+'_'+n
sample_list[1]= sample_list[1]+'_'+n
sample_list[2]= sample_list[2]+'_'+n
    