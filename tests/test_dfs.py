
import ipdb
import unittest
from libgraph import graphs, dfs, algorithms

class Tests(unittest.TestCase):
    def test_basic(self):
        g = graphs.Graph()
        g.add_edges((1,2), (1,3), (1,4), (2,3), (2,5), (5, 6))

        tr = dfs.Traversal(g)
        dfs.dfs(1, tr)
        self.assertEqual(tr.node_state[1], 1)
        self.assertEqual(tr.node_state[2], 1)
        self.assertEqual(tr.node_state[3], 1)
        self.assertEqual(tr.node_state[4], 1)
        self.assertEqual(tr.node_state[5], 1)
        self.assertEqual(tr.node_state[6], 1)

        self.assertTrue(1 not in tr.parents)
        self.assertEqual(tr.parents[2], 3)
        self.assertEqual(tr.parents[3], 1)
        self.assertEqual(tr.parents[4], 1)
        self.assertEqual(tr.parents[5], 2)
        self.assertEqual(tr.parents[6], 5)

    def test_cloning(self):
        """
        Leetcode - https://leetcode.com/problems/clone-graph/
        Complicated case with self-loop and multi edges
        """
        class UndirectedGraphNode:
            def __init__(self, x, neighs = None):
                self.label = x
                self.neighbors = []

        nodes = {}
        for n in [0,1,2,3,4,5]:
            nodes[n] = UndirectedGraphNode(n)

        nodes[0].neighbors = [nodes[1], nodes[5]]
        nodes[1].neighbors = [nodes[2], nodes[5]]
        nodes[2].neighbors = [nodes[3]]
        nodes[3].neighbors = [nodes[4], nodes[4]]
        nodes[4].neighbors = [nodes[5], nodes[5]]
        g = graphs.Graph(multi = True, 
                         key_func = (lambda node: node.label), 
                         neighbors_func = (lambda node: [(n,None) for n in node.neighbors]))

        class MyTraversal(dfs.Traversal):
            def __init__(self, graph):
                dfs.Traversal.__init__(self, graph)
                self.copiedNodes = {}

            def should_process_children(self, node):
                if node.label not in self.copiedNodes:
                    print "Processing Node: ", node.label
                    self.copiedNodes[node.label] = UndirectedGraphNode(node.label)

            def process_edge(self, source, target, edge_data): 
                print "Processing Edge: ", source.label, target.label
                self.should_process_children(source)
                self.should_process_children(target)
                self.copiedNodes[source.label].neighbors.append(self.copiedNodes[target.label])
                # self.copiedNodes[target.label].neighbors.append(self.copiedNodes[source.label])

        mt = MyTraversal(g)
        dfs.dfs(nodes[0], mt)
        self.assertEqual(sorted([n.label for n in mt.copiedNodes[0].neighbors]), [1,5])
        self.assertEqual(sorted([n.label for n in mt.copiedNodes[1].neighbors]), [2,5])
        self.assertEqual(sorted([n.label for n in mt.copiedNodes[2].neighbors]), [3])
        self.assertEqual(sorted([n.label for n in mt.copiedNodes[3].neighbors]), [4,4])
        self.assertEqual(sorted([n.label for n in mt.copiedNodes[4].neighbors]), [5,5])
        self.assertEqual(sorted([n.label for n in mt.copiedNodes[5].neighbors]), [])
