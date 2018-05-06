from graph_utils import *
from models.vertex import Vertex
from models.edge import Edge
from greedy_search import *
import time

#MAIN FUNCTION
def software_engineering():
    menu = 0
    opcao = 0
    while (menu != -1):
        print("*******************************************************************************************")
        print("Menu inicial")
        print("1. Imprimir grafo.")
        print("2. Busca em profundidade a partir de um nó.")
        print("3. Busca gulosa no grafo usando primeira heurística.")
        print("4. Busca gulosa no grafo usando segunda heurística. ")
        print("-1. Sair")
        print("*******************************************************************************************")

        menu = eval(input("Escolha a opção desejada: "))
        print("")
        if(menu == 1):
            pretty_print(dict_graph)
        if(menu == 2):
            node = eval(input("Digite o id do nó de partida: "))
            result = dfs(dict_graph, str(node))
            print(result)
        if(menu == 3):
            k = eval(input("Digite k (quantidade de usuários mais influentes): "))
            tree = search(Problem(k), heuristic_1)
            for node in tree:
                print(str(node.name) + " " + str(node.value))
                DFS = dfs(dict_graph, str(node.id))
                print("DFS de " + node.name + ", tamanho " + str(len(DFS)) + ": ")
                print(DFS)
        if(menu == 4):
            k = eval(input("Digite k (quantidade de usuários mais influentes): "))
            tree = search(Problem(k), heuristic_2)
            for node in tree:
                print(str(node.name) + " " + str(node.value))
                DFS = dfs(dict_graph, str(node.id))
                print("DFS de " + node.name + ", tamanho " + str(len(DFS)) + ": ")
                print(DFS)
        if(menu == -1):
            time.sleep(0.5)
            print("Saindo do programa!")
            print("Obrigado e volte sempre~~")
            time.sleep(0.7)
            exit(0)


dict_graph = Graph().to_dict("graph_vertex.net","graph_edge.net")
actual_graph = build_graph("graph_vertex.net","graph_edge.net")

software_engineering()