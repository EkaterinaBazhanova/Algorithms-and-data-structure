"""
9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
P.S. Пользователь вводит только верные данные,
 которые требует программа (только натуральные)
"""
n = int(input('Укажите количество натуральных чисел: '))

max_sum_digits = 0
num_max_digits = 0

def sum_digits(num):
    sd = 0
    while num // 10 != 0:
        sd += num % 10
        num = num // 10
    sd += num
    return sd

for i in range(1, n+1):
    num = int(input(f'Введите {i}-ое число: '))
    sd = sum_digits(num)
    if sd > max_sum_digits:
        max_sum_digits = sd
        num_max_digits = num

print(f'Из введенных чисел число {num_max_digits} имеет наибольшую сумму цифр {max_sum_digits}')

