import src.DataStructures.Graphs.DirectedGraph as Graph


class HamiltonianGraphSolverNotOptimal:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = self.graph.get_vertices()

    def is_complete(self, sequence):
        return len(sequence) == len(self.vertices)

    def is_promising(self, sequence):
        return sequence[-1] not in sequence[:-1]

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
                if self.is_promising(child):
                    found = self.backtracking(child)
                    if found is not None:
                        return found

        return None

    def solve(self, v):
        return self.backtracking([v])


class HamiltonianGraphSolver:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = self.graph.get_vertices()
        self.visited = set()
        self.path = []
        for i in range(len(self.vertices)):
            self.path.append(None)

    def is_complete(self, sequence):
        return len(sequence) == len(self.vertices)

    def is_promising(self, child):
        return child not in self.visited

    def is_feasible(self):
        sequence = self.path
        return sequence[0] in self.graph.get_outward_vertices(sequence[-1])

    def branch(self, index):
        return self.graph.get_outward_vertices(self.path[index])

    def backtracking(self, index):

        if index == len(self.vertices)-1:
            if self.is_feasible():
                return self.path

        else:
            for child in self.branch(index):
                if self.is_promising(child):
                    self.visited.add(child)
                    self.path[index+1] = child
                    found = self.backtracking(index+1)
                    if found is not None:
                        return found
                    self.visited.remove(child)

        return None

    def solve(self, v):
        self.path[0] = v
        self.visited.add(v)
        return self.backtracking(0)
