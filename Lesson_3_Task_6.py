'''
Задача 6. В одномерном массиве найти сумму элементов,
 находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
import random
num_list = [random.randint(0,100) for _ in range(10)]
print(f'Исходный массив: {num_list}')

min_max = {'min': [0, num_list[0]], 'max' : [0, num_list[0]]}

for i, num in enumerate(num_list):
    if (num < min_max['min'][1]) or (num == min_max['min'][1]):
        min_max['min'][1] = num
        min_max['min'][0] = i
    if (num > min_max['max'][1]) or (num == min_max['max'][1]):
        min_max['max'][1] = num
        min_max['max'][0] = i

print(f'Минимальный элемент {min_max["min"][1]} на месте с индексом {min_max["min"][0]}')
print(f'Максимальный элемент {min_max["max"][1]} на месте с индексом {min_max["max"][0]}')

if (min_max['min'][0] == min_max['max'][0]) or (abs(min_max['min'][0] - min_max['max'][0]) == 1):
    print('Сумма чисел между минимальным и максимальным элементом 0')
elif min_max['min'][0] < min_max['max'][0]:
    sum_num = sum(num_list[min_max['min'][0] + 1 : min_max['max'][0]])
    print(f'Сумма чисел между минимальным и максимальным элементами: {sum_num}')
else:
    sum_num = sum(num_list[min_max['max'][0] + 1: min_max['min'][0]])
    print(f'Сумма чисел между минимальным и максимальным элементами: {sum_num}')



