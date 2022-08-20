'''
Задача 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
import random

n_rows = 5
n_columns = 4

matrix = [[random.randint(0, 10) for _ in range(n_columns)] for _ in range(n_rows)]

min_el_columns = [matrix[0][j] for j in range(n_columns)]
for j in range(n_columns):
    for i in range(n_rows):
        if matrix[i][j] <= min_el_columns[j]:
            min_el_columns[j] = matrix[i][j]

print('Исходная матрица:')
for line in matrix:
    for item in line:
        print(f'{item:>6}', end='')
    print()

print('Минимальные элементы столбцов:')
max_min_el = min_el_columns[0]
for el in min_el_columns:
    if el >= max_min_el:
        max_min_el = el
    print(f'{el:>6}', end='')

print()
print(f'Максимальный минимальный элемент: {max_min_el}')