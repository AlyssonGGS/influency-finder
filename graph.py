from graph_utils import *
from pathlib import Path
import os
file_dir = os.path.abspath('files')
os.chdir(file_dir)


def pretty_print(graph = Graph()):
    for i in graph:
        print("Vertex : ")
        print(i)
        print("Edges")
        for j in i:
            print(j)

#Depth-First Search ou Busca em profundidade, usando o método da pilha.
#A partir de um grafo no formato de dicionário '{string: string}',
#retorna todos os vértices alcançáveis a partir desse vértice
#em uma estrutura set/conjunto.

def dfs(graph, begin):
    #Começo da pilha: nó que se deseja começar a busca.
    stack = [begin]

    #Conjunto de nós visitados
    visited = set()

    while stack:
        vertex = stack.pop(0)
        if vertex not in visited:
            #Se ainda não visitou esse nó, adiciona à lista de visitados
            visited.add(vertex)
            #Prepara a pilha para explorar os nós ligados ao recém-visitado
            stack.extend(graph[vertex] - visited)
            #print(stack)
    return visited

vertices = generate_vertices_list('graph_vertex.net')
#graph = Graph().to_dict("graph_vertex.net","graph_edge.net")
#pretty_print(graph)
#result = dfs(graph,'1')




#Não sei se será necessário, mas precisaria de uma função para achar o caminho entre dois nós
#Função que soma o custo total entre dois nós
#TODO def total_cost(graph,path):



