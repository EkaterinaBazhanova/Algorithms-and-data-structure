"""
1. В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
 Примечание: 8 разных ответов.
"""
divisors = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0,'9':0}
num_list = [i for i in range(2, 100)]
print(num_list)

for num in num_list:
    for d, _ in divisors.items():
        if num % int(d) == 0:
            divisors[f'{d}'] += 1

print('В указанном списке')
for d, n_d in divisors.items():
    print(f'количество чисел, кратных {d}: {n_d}')

