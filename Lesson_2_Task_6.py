"""
Задача 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.

P.S. Пользователь вводит только верные данные,
 которые требует программа (только натуральные)
"""
import random
num = random.randint(0, 100)
for i in range(10):
    n = int(input('Введите число: '))
    if n == num:
        print(f'Число угадано c {i+1} попытки!')
        break
    elif n < num:
        print(f'Попытка #{i+1} неудачная. Ваше число меньше задуманного.')
    else:
        print(f'Попытка #{i+1} неудачная. Ваше число больше задуманного.')
print(f'Было задумано число {num}')
