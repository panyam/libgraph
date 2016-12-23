
import unittest
from libgraph import graphs

class Tests(unittest.TestCase):
    def test_creation(self):
        g = graphs.Graph()

    def test_nodes_and_edges(self):
        g = graphs.Graph()
        nodes = [1,2,3,4]
        g.add_nodes(*nodes)
        g.add_edges((1,2), (2,3), (3,4), (4,5))

        for k in nodes:
            n = g.nodes[k]
            self.assertTrue(k in g.nodes)
        self.assertTrue(5 in g.nodes)

        self.assertTrue(isinstance(g.get_edge(1, 2), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(2, 3), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(3, 4), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(4, 5), graphs.Edge))

        self.assertTrue(isinstance(g.get_edge(2, 1), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(3, 2), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(4, 3), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(5, 4), graphs.Edge))

        # Ensure a -> b and b -> a is the same edge instance
        self.assertEqual(id(g.get_edge(2, 1)), id(g.get_edge(1, 2)))
        self.assertEqual(id(g.get_edge(3, 2)), id(g.get_edge(2, 3)))
        self.assertEqual(id(g.get_edge(4, 3)), id(g.get_edge(3, 4)))
        self.assertEqual(id(g.get_edge(5, 4)), id(g.get_edge(4, 5)))

    def test_nodes_and_edges_directed(self):
        g = graphs.Graph(directed = True)
        nodes = [1,2,3,4]
        g.add_nodes(*nodes)
        g.add_edges((1,2), (2,3), (3,4), (4,5))

        for k in nodes:
            n = g.nodes[k]
            self.assertTrue(k in g.nodes)
        self.assertTrue(5 in g.nodes)

        self.assertTrue(isinstance(g.get_edge(1, 2), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(2, 3), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(3, 4), graphs.Edge))
        self.assertTrue(isinstance(g.get_edge(4, 5), graphs.Edge))

        self.assertEqual(g.get_edge(2, 1), None)
        self.assertEqual(g.get_edge(3, 2), None)
        self.assertEqual(g.get_edge(4, 3), None)
        self.assertEqual(g.get_edge(5, 4), None)

