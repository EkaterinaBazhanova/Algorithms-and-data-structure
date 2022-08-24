"""
Задача 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque


print('Введите два числа в 16-й системе счисления')

n_1 = input('введите первое число: ')
n_1 = deque(n_1)
n_2 = input('введите второе число: ')
n_2 = deque(n_2)

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
     'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def summa(n_1, n_2):
    summ = deque()

    max_l = max(len(n_1), len(n_2))
    n1 = list(reversed(n_1))
    n1.extend(['0']*(max_l-len(n_1)))
    n2 = list(reversed(n_2))
    n2.extend(['0']*(max_l-len(n_2)))

    dvs = 0
    for i in range(max_l):
        dvs, rmnd = divmod(d[n1[i]] + d[n2[i]] + dvs, 16)
        summ.appendleft(get_key(d,rmnd))
    if dvs != 0:
        summ.appendleft(get_key(d, dvs))
    return "".join(list(summ))


def prod(n_1, n_2):
    rows = []
    n1 = list(reversed(n_1))
    n2 = list(reversed(n_2))
    
    for i in range(len(n1)):
        dvs = 0
        deq = deque()
        for j in range(len(n2)):
            dvs, rmnd = divmod(d[n1[i]] * d[n2[j]] + dvs, 16)
            deq.appendleft(get_key(d, rmnd))
        if dvs != 0:
            deq.appendleft(get_key(d, dvs))
        deq.extend(['0']*i)
        n = "".join(list(deq))
        rows.append(n)
    prd = '0'
    for i in range(len(rows)):
        prd = summa(prd,rows[i])
    return prd

print(f'Cумма указанных чисел: {summa(n_1,n_2)}')
print(f'Произведение указанных чисел: {prod(n_1,n_2)}')