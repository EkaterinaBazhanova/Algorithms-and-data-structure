"""
Задача 2. Отсортируйте по возрастанию методом слияния
одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random


size = 10
array = [random.uniform(0,50) for _ in range(size)]
print(f'Исходный массив:\n{array}')

# функция слияния двух отсортированных списков
def merge_list(a, b):
    c = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c

# функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(array):
    N1 = len(array) // 2
    a1 = array[:N1]     # деление массива на два примерно равной длины
    a2 = array[N1:]

    if len(a1) > 1: # если длина 1-го списка больше 1, то делим дальше
        a1 = split_and_merge_list(a1)
    if len(a2) > 1: # если длина 2-го списка больше 1, то делим дальше
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)   # слияние двух отсортированных списков в один

print(f'Отсортированный список:\n{split_and_merge_list(array)}')