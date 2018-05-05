from  models.vertex import Vertex

file_dir = "files/"

def generate_vertices_list(file_name, separator = "/"):
    vertices = []
    with open(file_dir + file_name, "r") as arq:
        line = arq.readline()
        while line:
            info = line.replace("\n","").split(separator)
            vertex = Vertex(info[1], int(info[2]))
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
    return get_maximum_vertice(vertices)

print(get_first_node().name)