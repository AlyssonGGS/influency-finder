from  models.vertex import Vertex
from pathlib import Path
import os
file_dir = "files/"

class Graph():
    #Legibilidade
    def to_dict(self, vertex_file_name, edge_file_name):
        return convert_to_dict(vertex_file_name, edge_file_name)

def generate_standard_archives(file_name):
    edges = open(file_dir+"graph_edge1.net", "w")       #arquivo onde serao guardados as linhas
    vertex = open(file_dir+"graph_vertex1.net", "w")    #arquvo onde serao guardados os vertices
    arq = open(file_dir + file_name, "r")      #arquivo de leitura

    arq.readline()                             #primeira leitura: uma linha que indica a leitura de vertices

    while True:
        itens = arq.readline().split("\"")        #separa a linha em 3 itens : numero, nome e qtd de artigos
        if(len(itens) == 1):            #para na leitura que indica edges
            break
        else:
            vertex.write(itens[0].replace(" ", "/")+itens[1]+itens[2].replace(" ", "/")) #escreve cada separando com o "/
    while True:
        line = line = arq.readline()
        itens = line.split(" ")
        if (len(itens) == 1):           #para na leitura que indica triangle
            break
        else:
            edges.write(line.replace(" ", "/"))
    arq.close()
    vertex.close()
    edges.close()





def generate_vertices_list(file_name, separator = "/"):
    vertices = []
    with open(file_dir + file_name, "r") as arq:
        line = arq.readline()
        while line:
            info = line.replace("\n","").split(separator)
            vertex = Vertex(int(info[0]), info[1], int(info[2]))
            vertices.append(vertex)
            line = arq.readline()
    return vertices

def add_edges_to_vertices(file_name, vertices, separator = "/"):
    with open(file_dir + file_name, "r") as arq:
        line = arq.readline()
        while line:
            info = line.replace("\n","").split(separator)
            #modifica a lista de vertices na memoria
            create_edges(info, vertices)
            line = arq.readline()
    return vertices

#Cria uma aresta de ligação entre cada coautor com o mesmo custo
def create_edges(info, vertices):
    vertex_id_first = int(info[0])
    vertex_id_second = int(info[1])
    colaborations = int(info[2])
    #O -1 é usado para transformar o id usado no arquivo(começa em 1) para o id de lista(começa em 0)
    #cria uma aresta do primeiro coautor para o segundo
    vertices[vertex_id_first - 1].add_edge(vertices[vertex_id_second - 1], colaborations)
    #cria uma aresta do segundo coautor para o primerio
    vertices[vertex_id_second - 1].add_edge(vertices[vertex_id_first - 1], colaborations)

def get_maximum_vertice(vertices):
    return sorted(vertices, key = lambda vertex: vertex.value, reverse = True)[0]

def get_first_node():
    vertices = generate_vertices_list("graph_vertex.net")
    add_edges_to_vertices("graph_edge.net",vertices)
    return "print"

#Converte um grafo para dicionário do tipo {string: string}
def convert_to_dict(vertex_file_name, edge_file_name):
    graph = {}
    vertices = generate_vertices_list(vertex_file_name)
    vertices = add_edges_to_vertices(edge_file_name, vertices)
    for vertex in vertices:
        s = set()
        for edges in vertex.edges:
            s.add(edges.destiny.id.__str__())
        graph[vertex.id] = s
    return graph

# Depth-First Search ou Busca em profundidade, usando o método da pilha.
# A partir de um grafo no formato de dicionário '{string: string}',
# retorna todos os vértices alcançáveis a partir desse vértice
# em uma estrutura set/conjunto.

def dfs(graph, begin):
    # Começo da pilha: nó que se deseja começar a busca.
    stack = [begin]

    # Conjunto de nós visitados
    visited = set()

    while stack:
        vertex = stack.pop(0)
        if vertex not in visited:
            # Se ainda não visitou esse nó, adiciona à lista de visitados
            visited.add(vertex)
            # Prepara a pilha para explorar os nós ligados ao recém-visitado
            stack.extend(graph[vertex] - visited)
            # print(stack)
    return visited



# UNCOMMENT BELOW TO TEST GRAPH-TO-DICT AND DEPTH-FIRST SEARCH

# graph = Graph().to_dict("graph_vertex.net","graph_edge.net")
# pretty_print(graph)
# result = dfs(graph,'1')
# print(result)



# Não sei se será necessário, mas precisaria de uma função
# para achar o caminho entre dois nós
# Função que soma o custo total entre dois nós.
# TODO def total_cost(graph,path):


generate_standard_archives("graph-T107_sub1.net")