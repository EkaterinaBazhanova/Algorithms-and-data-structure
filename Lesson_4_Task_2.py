'''
Задача 2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''
import cProfile

# Первый алгоритм
def sieve(n, m = 1000): #m -- до какого натурального числа ищем простые числа
    sieve = [i for i in range(m)]
    sieve[1] = 0
    for i in range(2, m):
        if sieve[i] != 0:
            j = i * 2
            while j < m:
                sieve[j] = 0
                j += i
        result = [i for i in sieve if i != 0]
    return result[n-1]

#Второй алгоритм
def prime(n):
    prime_num_series = []
    num_series = [i for i in range(2,1001)]
    for num in num_series:
        div_series = [i for i in range(num-1,1,-1) if num % i == 0] #список собственных делителей
        if div_series == []:
            prime_num_series.append(num)
    return prime_num_series[n-1]

'''
Результаты анализа скорости и сложности алгоритмов
   msec -- миллисекунда 10^{-3} секунды

Анализ алгоритма sieve.
№1. с помощью timeit (python -m timeit -n 1000 -s "import task_2" "task_2.sieve(n)): 
    task_2.sieve(2)
    1000 loops, best of 5: 31 msec per loop
    task_2.sieve(3)
    1000 loops, best of 5: 30.9 msec per loop
    task_2.sieve(4)
    1000 loops, best of 5: 30.8 msec per loop
    task_2.sieve(5)
    1000 loops, best of 5: 30.9 msec per loop
    task_2.sieve(10)
    1000 loops, best of 5: 30.7 msec per loop
    task_2.sieve(20)
    1000 loops, best of 5: 30.9 msec per loop
    Алгоритм имеет постоянную сложность
№2. с помощью cProfile (cProfile.run('sieve(num)')):
    1003 function calls in 0.032 seconds
    1    0.001    0.001    0.032    0.032 task_2.py:12(sieve)  #2, 4, 5, 10, 20 
    1003 function calls in 0.033 seconds
    1    0.001    0.001    0.033    0.033 task_2.py:12(sieve)   #3
    В алгоритме нет вложенных функций
    

Анализ алгоритма prime.
№1. с помощью timeit (python -m timeit -n 1000 -s "import task_2" "task_2.prime(n))::
    task_2.prime(2)
    1000 loops, best of 5: 27.5 msec per loop
    task_2.prime(3)
    1000 loops, best of 5: 27.1 msec per loop
    task_2.prime(4)
    1000 loops, best of 5: 27 msec per loop
    task_2.prime(5)
    1000 loops, best of 5: 27.2 msec per loop
    task_2.prime(10)
    1000 loops, best of 5: 27.1 msec per loop
    task_2.prime(20)
    1000 loops, best of 5: 27.2 msec per loop
    Алгоритм имеет постоянную сложность
№2. с помощью cProfile (cProfile.run('prime(num)')):
    1172 function calls in 0.028 seconds
    1    0.001    0.001    0.028    0.028 task_2.py:25(prime) #2, 3, 10, 20
    1172 function calls in 0.029 seconds
    1    0.001    0.001    0.029    0.029 task_2.py:25(prime) #4, 5
    В алгоритме нет вложенных функций


ВЫВОД:
1. Все алгоритмы имеют постоянную сложность. 
2. Алгоритмы 1 и 2 имеют примерно одинаковую скорость работы (алгоритм 2 чуть быстрее).

ИТОГО: Лучшим алгоритмом по скорости работы является алгоритм prime.

'''