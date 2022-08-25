"""
Задача 1. Отсортируйте по убыванию методом пузырька
одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции,
которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните,
что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random


size = 10
array = [random.randint(-100,99) for _ in range(size)]
print(f'Исходный массив:\n{array}')

def bouble_sort(array):
    for i in range(0, len(array)-1):   #len(array)-1 итераций
        for j in range(0, len(array)-1-i):   # -i потому что "вспыл пузырь" (сортируем часть без пузырька)
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(f'Отсортированный массив:\n{bouble_sort(array)}')