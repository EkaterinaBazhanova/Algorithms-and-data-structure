"""
Задача 3. Написать программу, которая обходит
не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции,
которая принимает на вход число вершин.
"""
import random

#функция генерации графа
def get_graph(n):
    graph = []
    for i in range(n):
        graph.append([random.randint(0,n-1) for _ in range(n)])
        graph[i] = set(graph[i])-{i}
    return graph

print('Создаем связный ориентированный граф без петель')
n = int(input('Введите количество вершин графа: '))
print()

graph = {i : ver for i, ver in enumerate(get_graph(n))}
print(f'Списки смежности сгенерированого не взвешенного ориентированного графа без петель с {n} вершинами:')
print(graph)
print()

def dfs(graph, start, finish, visited = None):
    if visited is None:
        visited = []
    visited.append(start)

    if finish in graph[start]:
        visited.append(finish)
        return visited

    for vertex in graph[start]:
        if vertex not in visited:
            dfs(graph, vertex, finish, visited)
        return visited
    return visited

print(f'Найдем путь в графе, для этого')
s = int(input("укажите вершину начала: "))
f = int(input("укажите вершину конца: "))
print(f'Путь из вершины {s} в вершину {f} в графе: {dfs(graph, s, f)}')