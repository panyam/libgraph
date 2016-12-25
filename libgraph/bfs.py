
import itertools
from collections import deque, defaultdict

DISCOVERED = 0
PROCESSED = 1

class Traversal(object):
    """
    A class that provides delegate methods to assist in graph traversal.
    """
    def __init__(self, graph):
        self.graph = graph

        # The parent nodes for each of the nodes
        self.parents = defaultdict(lambda: None)

        # Marks a node's state - can be missing (undiscovered), discovered (0) and processed (1)
        self.node_state = defaultdict(lambda: None)

        # Set this flag to true if you want the traversal to stop
        self.terminated = False

    def should_process_children(self, node): return True
    def process_node(self, node): return True
    def process_edge(self, source, target, edge_data): return True
    def select_children(self, node, reverse = False): return self.graph.iter_neighbors(node, reverse = reverse)

def bfs(start_node, traversal):
    """
    Performs a breadth first traversal of a graph.
    
    Traversal object contains the following:

        should_process_children(node):
            This method is called before a node is processed.  If this method
            returns a False then the node is not processed (and not marked as processed).
            If this method returns False, the success nodes of this node will also not be 
            visited.

        process_node(node):
            This method is called when a node is ready to be processed (after it has been
            visited).  Only if this method returns True then the node is marked as "processed".

        process_edge(source, target, edge_data):
            When a node is reached, process_edge is called on the edge that lead to
            the node.   If this method is returned False, then the node is no longer 
            traversed.

        select_children(node, reverse = False):
            Called to select the children of the node that are up for traversal from the given node
            along with the order the children are to be traversed.

            By default returns all the children in no particular order.
            Returns an iterator of tuples - (node, edge_data)

        parents[node -> node]   -   A map in which the parent nodes of a node are stored.

        node_state[node -> int] -   A map storing the discovery/processing state of a node.
    """
    if not start_node: return
    queue = deque([(None, start_node)])
    g = traversal.graph

    while queue and not traversal.terminated:
        parent, node = queue.popleft()
        traversal.node_state[g.key_func(node)] = DISCOVERED
        if traversal.should_process_children(node) is False: continue

        traversal.node_state[g.key_func(node)] = PROCESSED
        for n,edge in traversal.select_children(node):
            if traversal.node_state[g.key_func(n)] != PROCESSED:
                queue.append((node,n))
                traversal.parents[g.key_func(n)] = node

        # Called after all children are added to be processed
        traversal.process_node(node)

