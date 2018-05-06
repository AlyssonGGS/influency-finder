from models.edge import Edge

class Vertex():
    def __init__(self, id = None, name = None, value = None):
        self.id = id
        self.name = name
        self.value = value
        self.edges = []

    def add_edge(self, destiny, cost):
        edge = Edge(destiny, cost)
        self.edges.append(edge)

    def append_edge(self, edge):
        self.edges.append(edge)

    def get_linked_vertex(self, vert_id):
        for edge in self.edges:
            if(edge.get_destiny_value()) == vert_id:
                return edge.destiny
<<<<<<< HEAD
        return None
=======


>>>>>>> 1f31c4dc6693b48ae8408f506841ea36bad04583
