import numpy as np
import random as rd
import time

from collections import deque

from lab3 import Queue


def beautiful_print(result):
    for i in range(len(result)):
        print(f"Посетили узеле: {result[i]}")
    


def bfs_1(matrix, start):
    n = len(matrix)          
    visited = set()
    queue = deque([start])   
    result = []             
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Проверяем всех соседей текущей вершины
        for neighbor in range(n):
            # Если есть ребро и вершина не посещена
            if matrix[vertex][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # beautiful_print(result)


def bfs_2(adj_list, start):
    # n = len(adj_list)
    visited = set()
    queue = Queue()
    result = []

    queue.append(start)
    visited.add(start)

    while not queue.is_empty():
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # beautiful_print(result)



def bfs_3(matrix, start):
    n = len(matrix)          
    visited = set()
    queue = Queue()   
    result = []             
    
    queue.append(start)
    visited.add(start)
    
    while not queue.is_empty():

        vertex = queue.popleft()
        result.append(vertex)
        
        # Проверяем всех соседей текущей вершины
        for neighbor in range(n):
            # Если есть ребро и вершина не посещена
            if matrix[vertex][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # beautiful_print(result)


def bfs_4(adj_list, start):
    # n = len(adj_list)
    visited = set()
    queue = deque([start])
    result = []

    queue.append(start)
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # beautiful_print(result)



def generator_smezh(razm):
    matr_sm = np.matrix(np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm))

    for i in range(razm):
        matr_sm[i, i] = 0
        for j in range(razm):
            if i<=j:
                matr_sm[i,j] = matr_sm[j, i]

    # print(matr_sm)
    return matr_sm.tolist()


def matrix_to_adj_list(matrix):
    return [
        [j for j in range(len(matrix)) if matrix[i][j] != 0]
        for i in range(len(matrix))
    ]



def main(razm):
    
    G = generator_smezh(razm)

    
    nach_1 = nach_2 =  0

    start_1 = time.time()
    bfs_1(G, nach_1)
    end_1 = time.time()
    
    print(f"Время работы на основе библиотечной очереди: {end_1 - start_1}")

    

    start_2 = time.time()
    bfs_3(G, nach_2)
    end_2 = time.time()

    print(f"Время работы на основе самописной очереди: {end_2 - start_2}")
    diff = ((end_2 - start_2) - (end_1 - start_1))
    print(f"разница: {diff}")
    G = matrix_to_adj_list(G)
    # nach_1 = int(input("Введите вершину с которой хотите начать:\t"))

    start = time.time()
    bfs_2(G, nach_1)
    end = time.time()

    print(f"Время работы на основе самописной очереди для списков смежности: {end - start}")
    
    # nach_1 = int(input("Введите вершину с которой хотите начать:\t"))
    start = time.time()
    bfs_4(G, nach_1)
    end = time.time()
    print(f"Время работы на основе библиотечной очереди для списков смежности: {end - start}")

def test():
    pass

if __name__ == "__main__":
    lst = [10, 100, 200, 300, 400, 500, 1000, 10000]
    for i in lst:
        print(f"Кол-во верши графа {i}:")
        main(i)
