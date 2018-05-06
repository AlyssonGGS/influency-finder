from graph_utils import get_first_node
from models.tree import Tree

class Problem:
    def __init__(self, k):
        self.k = k
        self.tree = Tree(0)
    
    def goal(self, node):
        return False
    
    def actions(self, tree):
        return []

def search(problem, heuristic):
    node = get_first_node()

    tree = problem.tree
    tree.set_node_by_vertex(node, None)

    frontier = [tree]
    explored = set()

    while True:
        if not frontier:
             raise Exception("Fronteira vazia!")
        node = frontier.pop()
        if problem.goal(node):
            return problem.most_influents
        explored.add(node.id)
        for action in problem.actions(tree):
            (node, child) = (node, tree)
            if not (child.id in explored or child.id in frontier):
                frontier.add(child)
            elif frontier[0].value < heuristc(node):
                frontier.pop()
                frontier.add(tree)
        return

#h1
def heuristc(edge):
    sum = 0
    for e in edge.destiny.edges:
        sum = sum + e.cost
    return sum 

search(Problem(0), heuristc)