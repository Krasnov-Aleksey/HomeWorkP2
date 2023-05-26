'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

from random import randint

count_coin=int(input('Введите количество монет '))
count_eagle=0
count_tails=0

for i in range(count_coin):
    coin=randint(0,1)
    print(coin)
    if coin==0:
        count_eagle+=1
    else:
        count_tails+=1
        
if count_eagle<count_tails:
    print(f'Минимальное количество монет, которые нужно перевернуть {count_eagle}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть {count_tails}')



