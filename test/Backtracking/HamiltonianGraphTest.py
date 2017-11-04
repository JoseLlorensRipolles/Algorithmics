import unittest
import src.DataStructures.Graphs.DirectedGraph as Graph
import src.Backtracking.HamiltonianGraph as HamiltonianGraphSolver


class HamiltonianGraphTest(unittest.TestCase):

    def test_recursive_solution(self):
        graph = Graph.DirectedGraph({1, 2, 3})
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(3, 2)
        graph.add_edge(2, 1)

        solver = HamiltonianGraphSolver.HamiltonianGraphSolver(graph)
        print(solver.solve(1))

if __name__ == '__main__':
    unittest.main()