from graph_utils import get_first_node, generate_vertices_list
from models.tree import Tree

class Problem:
    def __init__(self, k):
        self.k = k
        self.solution = []
    
    def goal(self, node):
        # verifica se o no ja esta na solucao
        for tree in self.solution:
            if tree.id == node.id:
                return False
        
        #caso a solucao nao esteja com a contagem completa, adiciona o no na solucao
        if len(self.solution) < self.k:
            self.solution.append(node)
            return False

        #se a solucao esta completa e o node analisado possui maior valor que algum no da solucao, remove o no da solucao e adiciona o no analisado
        #apos isso continua a procura
        for tree in self.solution:
            if tree.value < node.value:
                self.solution.remove(tree)
                self.solution.append(node)
                return False

        #retorna verdadeiro caso o no analisado nao seja maior que nenhum que ja esteja contido na lista,
        #sendo que esta ja esta completa
        return True

    def child_node(self, node, explored):
        (id, highest) = self.__get_first_no_explored_child(node, explored)
        #procura pelo maior filho
        for child in node.children[id:]:
            if highest.value < child.value and not child.id in explored:
                highest = child
        return highest                        

    def __get_first_no_explored_child(self, tree, explored):
        i = 0
        for child in tree.children:
            if not child.id in explored:
                return (i, child)
            i = i + 1
        
  
def search(problem, heuristic):
    #Adiciona o primeiro no na arvore que será utilizada
    frontier = [build_initial_tree(get_first_node(), heuristic)]

    #Cria conjunto de nós explorados
    explored = set()

    while True:
        if not frontier:
            raise Exception("Fronteira vazia!")
        
        #Recupera o no que será analisado
        tree = frontier.pop()
        
        #verifica se o no resolve o problema
        #ver goal da classe Problem
        if problem.goal(tree):
            #retorna uma lista ordenada com a solução
            return sorted(problem.solution, key=lambda tree: tree.value, reverse=True)
        
        #Expande a árvore a partir das arestas do grafo
        tree = build_childs(tree, heuristic)

        #marca o no como explorado
        explored.add(tree.id)

        #busca pelo nó com maior valor da heuristica dada
        destiny = problem.child_node(tree, explored)

        #adiciona este nó na lista analisada
        frontier.append(destiny)
            

def build_initial_tree(node, heuristic):
    tree = Tree(0)
    tree.set_tree_by_vertex(node, None)
    tree.value = heuristic(tree.vertex)
    return tree

def build_childs(tree, heuristc):
    for edge in tree.vertex.edges:
        tree.add_child_by_vertex(edge.destiny, heuristc(edge.destiny))
    return tree

#h1
def heuristic_1(node):
    sum = 0
    for e in node.edges:
        sum = sum + e.cost
    return sum

#h2
def heuristic_2(node):
    return node.value

#UNCOMMENT TO TEST HEURISTIC SEARCH
[print(str(tree.name) + " " + str(tree.value)) for tree in search(Problem(20), heuristic_1)]
print("------")
[print(str(tree.name) + " " + str(tree.value)) for tree in search(Problem(20), heuristic_2)]