import random
import unittest

from DataStructures.src.Graphs.DirectedGraph import Graph


class GraphTest(unittest.TestCase):

    def test_get_vertex(self):

        g = Graph(vertices={0, 1, 2, 3})
        self.assertEqual(g.get_vertices(), {0, 1, 2, 3})

        g = Graph(set())
        self.assertEqual(g.get_vertices(), set())

        v = set([random.randint(-100, 100) for r in range(100)])
        g = Graph(v)
        self.assertEqual(g.get_vertices(), v)

    def test_add_vertex(self):

        g = Graph(set())
        g.add_vertex(3)
        self.assertEqual(g.get_vertices(), {3})

        v = set([random.randint(-100, 100) for r in range(100)])
        g = Graph(v)
        g.add_vertex(200)
        v.add(200)
        self.assertEqual(g.get_vertices(), v)

    def test_get_edges(self):

        edges = dict()
        g = Graph(vertices=set())
        self.assertEqual(g.get_edges(), edges)

        edges = {1: {(2, 4), (1, 1), (3, 2)}, 2: {(2, 1)}, 3: {(1, 2), (2, 1), (3, 2)}}
        g = Graph({1, 2, 3})

        g.add_edge(1, 2, 4)
        g.add_edge(1, 1, 1)
        g.add_edge(1, 3, 2)
        g.add_edge(2, 2, 1)
        g.add_edge(3, 1, 2)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 3, 2)

        self.assertEqual(g.get_edges(), edges)

    def test_add_edge(self):

        g = Graph({1, 2, 3})
        g.add_edge(1, 2, 5)
        self.assertEqual(g.get_edges(), {1: {(2, 5)}, 2: set(), 3: set()})

    def test_outward_vertices(self):

        g = Graph({1, 2, 3})

        g.add_edge(1, 2)
        g.add_edge(2, 3)
        self.assertEqual(g.get_outward_vertices(1), {2})
        self.assertEqual(g.get_outward_vertices(2), {3})

        g.add_edge(1, 3)
        self.assertEqual(g.get_outward_vertices(1), {2, 3})
        self.assertEqual(g.get_outward_vertices(1), {3, 2})

        g.add_edge(1, 1)
        self.assertEqual(g.get_outward_vertices(1), {1, 2, 3})

    def test_inwards_vertices(self):

        g = Graph({1, 2, 3})

        g.add_edge(1, 2)
        self.assertEqual(g.get_inwards_vertices(2), {1})

        g.add_edge(3, 2)
        self.assertEqual(g.get_inwards_vertices(2), {1, 3})

        g.add_edge(2, 2)
        self.assertEqual(g.get_inwards_vertices(2), {1, 2, 3})

if __name__ == '__main__':
    unittest.main()
