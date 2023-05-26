'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
'''
nam=int(input('Введите число '))
degree_2=0
flag=True
while flag:
    print(2**degree_2)
    if 2**degree_2>nam:
        flag=False
    degree_2+=1

