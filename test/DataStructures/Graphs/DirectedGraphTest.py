import random
import unittest

from src.DataStructures.Graphs.DirectedGraph import DirectedGraph


class DirectedGraphTest(unittest.TestCase):

    def test_get_vertex(self):

        g = DirectedGraph(vertices={0, 1, 2, 3})
        self.assertEqual(g.get_vertices(), {0, 1, 2, 3})

        g = DirectedGraph(set())
        self.assertEqual(g.get_vertices(), set())

        v = set([random.randint(-100, 100) for r in range(100)])
        g = DirectedGraph(v)
        self.assertEqual(g.get_vertices(), v)

    def test_add_vertex(self):

        g = DirectedGraph(set())
        g.add_vertex(3)
        self.assertEqual(g.get_vertices(), {3})

        v = set([random.randint(-100, 100) for r in range(100)])
        g = DirectedGraph(v)
        g.add_vertex(200)
        v.add(200)
        self.assertEqual(g.get_vertices(), v)

    def test_get_edges(self):

        edges = dict()
        g = DirectedGraph(vertices=set())
        self.assertEqual(g.get_edges(), edges)

        edges = {1: {(2, 4), (1, 1), (3, 2)}, 2: {(2, 1)}, 3: {(1, 2), (2, 1), (3, 2)}}
        g = DirectedGraph({1, 2, 3})

        g.add_edge(1, 2, 4)
        g.add_edge(1, 1, 1)
        g.add_edge(1, 3, 2)
        g.add_edge(2, 2, 1)
        g.add_edge(3, 1, 2)
        g.add_edge(3, 2, 1)
        g.add_edge(3, 3, 2)

        self.assertEqual(g.get_edges(), edges)

    def test_add_edge(self):

        g = DirectedGraph({1, 2, 3})
        g.add_edge(1, 2, 5)
        self.assertEqual(g.get_edges(), {1: {(2, 5)}, 2: set(), 3: set()})

    def test_outward_vertices(self):

        g = DirectedGraph({1, 2, 3})

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

        g = DirectedGraph({1, 2, 3})

        g.add_edge(1, 2)
        self.assertEqual(g.get_inwards_vertices(2), {1})

        g.add_edge(3, 2)
        self.assertEqual(g.get_inwards_vertices(2), {1, 3})

        g.add_edge(2, 2)
        self.assertEqual(g.get_inwards_vertices(2), {1, 2, 3})

if __name__ == '__main__':
    unittest.main()
