"""
Задача 1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple


features = ['name', 'profit_1', 'profit_2', 'profit_3', 'profit_4', 'sum_profit']
Company = namedtuple('Company', features, rename=True)

comps = []
n = int(input('Введите количество предприятий: '))
for i in range(n):
    print(f'Введите данные {i+1}-ой компании: ')
    name_comp = [input('Название: ')]
    profit = [float(prof) for prof in input('Прибыль за 1, 2, 3 и 4 кварталы через пробел: ').split()]
    sum_profit = [sum(profit)]
    comp = Company._make(name_comp + profit + sum_profit)
    comps.append(comp)

average_profit = sum([comp.sum_profit for comp in comps]) / len(comps)

comp_above_aver = []
comp_below_aver = []
for comp in comps:
    if comp.sum_profit > average_profit:
        comp_above_aver.append(comp.name)
    else:
        if comp.sum_profit < average_profit:
            comp_below_aver.append(comp.name)

print('Компании, чья прибыль выше среднего: ')
for i in comp_above_aver:
    print(i)
print('Компании, чья прибыль ниже среднего: ')
for i in comp_below_aver:
    print(i)
