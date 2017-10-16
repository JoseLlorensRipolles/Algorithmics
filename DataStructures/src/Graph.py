from collections import defaultdict


class Graph:
    def __init__(self, vertices=set()):
        self.vertices = vertices

        self.edges = dict()
        for vertex in vertices:
            self.edges[vertex] = set()

    def get_vertices(self):
        return self.vertices

    def add_vertex(self, v):
        self.vertices.add(v)

    def get_edges(self):
        return self.edges

    def add_edge(self, v_origin, v_destination, weight):
        self.edges[v_origin].add((v_destination, weight))
        pass
