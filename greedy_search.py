from graph_utils import get_first_node, generate_vertices_list
from models.tree import Tree

class Problem:
    def __init__(self, k):
        self.k = k
        self.solution = []
    
    def goal(self, node):
        for tree in self.solution:
            if tree.id == node.id:
                return False
            
        if len(self.solution) < self.k:
            self.solution.append(node)
            return False

        for tree in self.solution:
            if tree.value < node.value:
                self.solution.remove(tree)
                self.solution.append(node)
                return False

        return True

    def child_node(self, node):
        highest = node.children[0]
        for child in node.children:
            if highest.value < child.value:
                highest = child
        return highest                        
  
def search(problem, heuristic):
    tree = build_initial_tree(get_first_node(), heuristic)
    build_childs(tree, heuristic)

    frontier = [tree]
    explored = set()

    while True:
        if not frontier:
            raise Exception("Fronteira vazia!")
        tree = frontier.pop()
        if problem.goal(tree):
            return sorted(problem.solution, key=lambda tree: tree.value, reverse=True)
        explored.add(tree.id)

        for child in tree.children:
            if not (child.id in explored or child in frontier):
                build_childs(child, heuristic)
                frontier.append(child)
            elif frontier[len(frontier) - 1].value < child.value:
                frontier.remove(frontier[len(frontier) - 1])
                frontier.append(child)

def build_initial_tree(node, heuristic):
    tree = Tree(0)
    tree.set_tree_by_vertex(node, None)
    tree.value = heuristic(tree.vertex)
    return tree

def build_childs(tree, heuristc):
    for edge in tree.vertex.edges:
        tree.add_child_by_vertex(edge.destiny, heuristc(edge.destiny))

#h1
def heuristic_1(node):
    sum = 0
    for e in node.edges:
        sum = sum + e.cost
    return sum

#h2
def heuristic_2(node):
    return node.value

# #UNCOMMENT TO TEST HEURISTIC SEARCH
# [print(str(tree.name) + " " + str(tree.value)) for tree in search(Problem(20), heuristic_1)]
# print("------")
# [print(str(tree.name) + " " + str(tree.value)) for tree in search(Problem(20), heuristic_2)]