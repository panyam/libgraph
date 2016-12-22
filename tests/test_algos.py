
import ipdb
import unittest
from libgraph import graphs, traversals, algorithms

class Tests(unittest.TestCase):
    def test_basic(self):
        g = graphs.Graph()
        g.add_edges((1,2), (1,3), (1,4), (2,5), (5, 6))

        comps = algorithms.connected_components(g)
        self.assertEqual(len(set(comps.values())), 1)

    def test_no_edges(self):
        g = graphs.Graph()
        g.add_nodes(1,2,3,4,5)

        comps = algorithms.connected_components(g)
        self.assertEqual(len(set(comps.values())), 5)

    def test_islands(self):
        g = graphs.Graph()
        g.add_edges((1,2), (2,3), (3,4))
        g.add_edges((10,20), (20,30), (30,40))
        g.add_edges((100,200), (200,300), (300,400))

        comps = algorithms.connected_components(g)
        self.assertEqual(len(set(comps.values())), 3)
