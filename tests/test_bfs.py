
import ipdb
import unittest
from libgraph import graphs, traversals, algorithms

class Tests(unittest.TestCase):
    def test_basic(self):
        g = graphs.Graph()
        g.add_edges((1,2), (1,3), (1,4), (2,5), (5, 6))

        tr = traversals.Traversal(g)
        traversals.bfs(g.nodes[1], tr)
        self.assertEqual(tr.node_state[1], 1)
        self.assertEqual(tr.node_state[2], 1)
        self.assertEqual(tr.node_state[3], 1)
        self.assertEqual(tr.node_state[4], 1)
        self.assertEqual(tr.node_state[5], 1)
        self.assertEqual(tr.node_state[6], 1)

        self.assertTrue(1 not in tr.parents)
        self.assertEqual(tr.parents[2], 1)
        self.assertEqual(tr.parents[3], 1)
        self.assertEqual(tr.parents[4], 1)
        self.assertEqual(tr.parents[5], 2)
        self.assertEqual(tr.parents[6], 5)
