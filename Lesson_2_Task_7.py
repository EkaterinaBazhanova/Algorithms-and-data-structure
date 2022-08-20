'''
Задача 7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''
import random
num_list = [random.randint(0,100) for _ in range(10)]
print(f'Исходный массив: {num_list}')

min_1 = num_list[0]
min_2 = None

for num in num_list[1:]:
    if num <= min_1:
        min_1, min_2 = num, min_1
    elif min_2 == None or num <= min_2:
        min_2 = num
print(f'Минимальные элементы массива {min_1} и {min_2}')