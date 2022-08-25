"""
Массив размером 2m + 1, где m — натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""
import random
from collections import deque


m = 3
size = 2*m + 1
array = [random.randint(0,10) for _ in range(size)]
print(f'Исходный числовой ряд:\n{array}')

def median(array):
    deq = deque(array)
    if len(deq) == 1:
        return(deq[0])

    max_el = max(deq)
    min_el = min(deq)
    deq.remove(max_el)
    deq.remove(min_el)
    return median(list(deq))

print(f'Медиана ряда: {median(array)}')

import statistics
print(f'Проверка модулем statistics: {statistics.median(array)}')