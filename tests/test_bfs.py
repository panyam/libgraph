
import unittest
from libgraph import graphs, traversals, algorithms

class Tests(unittest.TestCase):
    def test_basic(self):
        g = graphs.Graph()
        g.add_edges((1,2), (1,3), (1,4), (2,5), (5, 6))

        tr = traversals.Traversal(g)
        traversals.bfs(1, tr)
