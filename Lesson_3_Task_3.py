"""
3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
"""
import random
num_list = [random.randint(0,100) for _ in range(10)]
print(f'Исходный массив: {num_list}')

replace = {'min': [0, num_list[0]], 'max' : [0, num_list[0]]}

for i, num in enumerate(num_list):
    if (num < replace['min'][1]) or (num == replace['min'][1]):
        replace['min'][1] = num
        replace['min'][0] = i
    if (num > replace['max'][1]) or (num == replace['max'][1]):
        replace['max'][1] = num
        replace['max'][0] = i

print(f'Минимальный элемент {replace["min"][1]} на месте с индексом {replace["min"][0]}')
print(f'Максимальный элемент {replace["max"][1]} на месте с индексом {replace["max"][0]}')

num_list[replace['min'][0]] = replace['max'][1]
num_list[replace['max'][0]] = replace['min'][1]
print(f'Массив с переставленными минимальным и максимальным элементами: \n{num_list}')

