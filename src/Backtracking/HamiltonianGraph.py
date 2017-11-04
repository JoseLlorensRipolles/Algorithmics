import src.DataStructures.Graphs.DirectedGraph as Graph


def is_promising(sequence):
    return sequence[-1] not in sequence[:-1]


class HamiltonianGraphSolver:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = self.graph.get_vertices()

    def is_complete(self, sequence):
        return len(sequence) == len(self.vertices)

    def is_feasible(self, sequence):
        return sequence[0] in self.graph.get_outward_vertices(sequence[-1])

    def branch(self, sequence):
        children = []
        for vertex in self.graph.get_outward_vertices(sequence[-1]):
            aux = sequence + [vertex]
            children.append(aux)
        return children

    def backtracking(self, sequence):

        if self.is_complete(sequence):
            if self.is_feasible(sequence):
                return sequence

        else:
            for child in self.branch(sequence):
                if is_promising(child):
                    found = self.backtracking(child)
                    if found is not None:
                        return found

        return None

    def solve(self, v):
        return self.backtracking([v])
