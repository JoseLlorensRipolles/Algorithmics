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
        solution = solver.solve(1)
        self.check(solution, graph)

        graph = Graph.DirectedGraph({1, 2, 3})
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        solver = HamiltonianGraphSolver.HamiltonianGraphSolver(graph)
        solution = solver.solve(1)
        self.assertEqual(solution, None)

        graph = Graph.DirectedGraph({1, 2, 3, 4})
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 2)
        solver = HamiltonianGraphSolver.HamiltonianGraphSolver(graph)
        solution = solver.solve(1)
        self.assertEqual(solution, None)

        graph = Graph.DirectedGraph({1, 2, 3, 4})
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(4, 2)
        graph.add_edge(4, 1)

        solver = HamiltonianGraphSolver.HamiltonianGraphSolver(graph)
        solution = solver.solve(1)
        self.check(solution, graph)

    def check(self, solution, graph):
        for i in range(len(solution) - 1):
            self.assertTrue(solution[i] in graph.get_inwards_vertices(solution[i + 1]))
        self.assertTrue(solution[0] in graph.get_outward_vertices(solution[-1]))
        self.assertEqual(len(solution), len(graph.get_vertices()))
        self.assertEqual(set(solution), graph.get_vertices())


if __name__ == '__main__':
    unittest.main()
