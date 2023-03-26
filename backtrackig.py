matrix_of_coherence = [[0, 1, 0],  # матрица связности
                       [1, 0, 0],
                       [0, 0, 0]]

ex = set()  # множество посещенных вершин


def dfs(node):  # start - начальная вершина

    ex.add(node)
    for coherence in range(len(matrix_of_coherence)):
        if matrix_of_coherence[node][coherence] == 1 and coherence not in ex:
            print(coherence)
            dfs(coherence)


# 2. Список смежности.'''Полужирное начертание'''
list_of_adjacencies = [[1, 3], [0], [3], [2, 0], []]
vladimir = [False for enotu in range(len(list_of_adjacencies))]


def dfs(vovanissimo):
    vladimir[vovanissimo] = True
    for vovochka in list_of_adjacencies[vovanissimo]:
        if not vladimir[vovochka]:
            dfs(vovochka)


for cotiki in range(len(list_of_adjacencies)):
    if not vladimir[cotiki]:
        dfs(cotiki)
# Так и не смог исправить. Функции перекрывают друг друга. Исправил только названия переменных которые понял.  
            
                
            
            
            
            
        
    



