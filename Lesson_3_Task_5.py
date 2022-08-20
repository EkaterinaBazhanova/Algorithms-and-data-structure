"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random
num_list = [random.randint(-10,10) for _ in range(10)]
print(f'Исходный массив: {num_list}')

max_neg  = [] #idx,num
for i, num in enumerate(num_list):
    if num < 0:
        max_neg.append(i)
        max_neg.append(num)
        break


if len(max_neg) == 0:
    print('Массив не содержит отрицательных элементов')
else:
    for i, num in enumerate(num_list):
        if num < 0:
            if (num > max_neg[1]) or (num == max_neg[1]):
                max_neg[1] = num
                max_neg[0] = i
    print(f'Максимальный отрицательный элемент {max_neg[1]} находится на месте с индексом {max_neg[0]}')
