from models.vertex import Vertex
from models.edge import Edge

vert1 = Vertex(10)
vert2 = Vertex(50)
edge = Edge(vert2, 0)

vert1.append_edge(edge)
print(vert1.get_linked_vertex(50))