"""
Задача 1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""
n = int(input('Введите количество друзей: '))
graph = [[1]*n for _ in range(n)]
for i in range(len(graph)):
    graph[i][i] = 0
print(f'Матрица смежности графа:')
print(*graph, sep='\n')

#составим список ребер
def get_edges(graph):
    edges = []
    for i in range(len(graph)):
         for j in range(len(graph)):
             if graph[i][j] == 1:
                 edges.append((i,j))  #добавляем ребро в список ребер
                 graph[j][i] = 0      #убираем это же ребро (из другой вершины)
    return edges
print(f'{n} друзей сделали {len(get_edges(graph))} рукопожатий:')
print(*get_edges(graph), sep='\n')

