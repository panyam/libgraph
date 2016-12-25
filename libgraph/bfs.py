
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

    def should_process_node(self, node): return True
    def children_queued(self, node): return True
    def process_edge(self, source, target, edge_data): return True
    def select_children(self, node, reverse = False): return self.graph.iter_neighbors(node, reverse = reverse)

def bfs(start_node, traversal):
    """
    Performs a breadth first traversal of a graph.
    
    Traversal object contains the following:

        should_process_node(node):
            This method is called before a node is processed.  If this method
            returns a False then the node is not processed (and not marked as processed).
            If this method returns False, the success nodes of this node will also not be 
            visited.

        children_queued(node):
            Called when all the children of a node have been queued.

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
        nodekey = g.key_func(node)
        traversal.node_state[nodekey] = DISCOVERED
        if traversal.should_process_node(node) is False: continue

        traversal.node_state[nodekey] = PROCESSED
        for n,edge in traversal.select_children(node):
            childkey = g.key_func(n)
            if traversal.node_state[childkey] != PROCESSED:
                traversal.parents[childkey] = node
                queue.append((node,n))

        # Called after all children are added to be processed
        traversal.children_queued(node)

