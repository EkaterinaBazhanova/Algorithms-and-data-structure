"""
Задача 4. Определить, какое число в массиве встречается чаще всего.
"""
import random
num_list = [random.randint(0,5) for _ in range(10)]
print(f'Исходный массив: {num_list}')

n_num = {f'{num}': 0 for num in list(set(num_list))}

for num in num_list:
    for key, _ in n_num.items():
        if num == int(key):
            n_num[f'{key}'] +=1
print(f'Количество чисел в массиве: {n_num}')

mostly_num = [0, 0]  #количество раз, элемент
for key, n in n_num.items():
    if n > mostly_num[0]:
        mostly_num[0] = n
        mostly_num[1] = int(key)
print(f'Чаще всего встречается число {mostly_num[1]} ({mostly_num[0]} раз(a))')