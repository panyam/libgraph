
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

        self.curr_time, self.entry_times, self.exit_times = 0, {}, {}

        # Set this flag to true if you want the traversal to stop
        self.terminated = False

    def should_process_node(self, node): return True
    def node_processed(self, node): return True
    def process_edge(self, source, target, edge_data): return True
    def select_children(self, node, reverse = False): return self.graph.iter_neighbors(node, reverse = reverse)

def dfs(node, traversal):
    """
    Recursive DFS traversal of a graph.
    
    Traversal object contains the following:

        should_process_node(node):
            This method is called before a node is processed.  If this method
            returns a False then the node is not processed (and not marked as processed).
            If this method returns False, the success nodes of this node will also not be 
            visited.

        node_processed(node):
            Called after a node and all its children have been recursed into.   This can 
            be overridden to make the the node available again to be processed.

        process_edge(source, target, edge_data):
            When a node is reached, process_edge is called on the edge that lead to
            the node.   If this method is returned False, then the node is no longer 
            traversed.

        select_children(node, reverse = False):
            Called to select the children of the node that are up for traversal from the given node
            along with the order the children are to be traversed.

            By default returns all the children in no particular order.
            Returns an iterator of tuples - (node, edge_data)

        parents[node -> node]       -   A map in which the parent nodes of a node are stored.
        node_state[node -> int]     -   A map storing the discovery/processing state of a node.
        entry_times[Node -> int]    -   Contains the entry time of a particular node.
        exit_times[Node -> int]     -   Contains the exit time of a particular node (ie when all of 
                                        a node's children have also been processed).
    """
    if traversal.terminated: return

    g = traversal.graph
    node_key = g.key_func(node)
    traversal.node_state[node_key] = DISCOVERED
    traversal.entry_times[node_key] = traversal.curr_time
    traversal.curr_time += 1

    if traversal.should_process_node(node) is not False:
        # Now go through all children
        children = list(traversal.select_children(node, reverse = True))
        # print "Node, Children: ", g.key_func(node), children
        for n,edge in children:
            child_key = g.key_func(n)
            if traversal.node_state[child_key] != None:
                traversal.process_edge(node, n, edge)
            else:   # Node has not even been discovered yet
                traversal.parents[child_key] = node
                traversal.process_edge(node, n, edge)
                dfs(n, traversal)

        traversal.node_state[node_key] = PROCESSED
        traversal.curr_time += 1
        traversal.exit_times[node_key] = traversal.curr_time
        traversal.node_processed(node)

