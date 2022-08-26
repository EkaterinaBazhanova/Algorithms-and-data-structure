'''
Задача 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
'''
from collections import deque
#матрица смежности взвешенного графа
graph = [
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,7,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]

def dijkotra(graph, start):
    length = len(graph)
    is_visited = [False] * length   # были ли в вершинах
    cost = [float('inf')] * length  # стоимость пути до вершин
    parent = [-1]*length  #родители вершин
    cost[start] = 0  #стоимость старта
    min_cost = 0 #минимальная стоимость
    ways = []
    start_way = start

    while min_cost<float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):  #проходимся в матрице смежности по строке start

            if vertex != 0 and not is_visited[i]:  #если вершина не 0 (есть ребро) и ее не посещали
                if cost[i] > vertex + cost[start]: #проверяем расстояние
                    cost[i] = vertex + cost[start] #записываем вершине короткое расстояние
                    parent[i] = start              #указываем родительскую вершину

        min_cost = float('inf')  #меняем минимальную стоимость
        for i in range(length): #цикл по всем вершинам графа
            if min_cost > cost[i] and not is_visited[i]:  #если минимальная стоимость больше стоимости вершиныи ее не посещали
                min_cost = cost[i]
                start = i

    for i in range(length):
        way = deque()
        if i == start_way:
            way.append(i)
        elif parent[i] == -1:
            way = deque()
        else:
            x = parent[i]
            while x != -1:
                way.appendleft(x)
                x = parent[x]
            way.append(i)
        ways.append(list(way))

    return cost, ways #стоимость путей и пути из start до каждой вершины

n = int(input('Введите стартовую вершину: '))
print()
cost, way = dijkotra(graph, n)
print(f'Кратчайшие расстояния от вершины {n} до остальных вершин графа и их стоимости')
print()
for i in range(len(graph)):
    print(f'Пути из вершины {n} до вершины {i} стоимостью {cost[i]}:')
    print(way[i])
    print()