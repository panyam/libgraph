
import ipdb
import dfs, bfs

def connected_components(graph):
    """
    Given a graph (directed or undirected) return its connected components.

    Input: A graph object.
    Output: A dictionary with the nodes as keys and the component index for 
            that node as the value.
    """

    class CCTraversal(bfs.Traversal):
        def __init__(self, graph):
            bfs.Traversal.__init__(self, graph)
            self.components = {}
            self.curr_component = 0

        def children_queued(self, node):
            self.components[node] = self.curr_component

    traversal = CCTraversal(graph)
    for node in graph.nodes:
        if node not in traversal.components:
            # Node has already been assigned a component so dont bother with this
            bfs.bfs(node, traversal)
            traversal.curr_component += 1

    return traversal.components

def topo_sort(graph):
    """
    Given a directed graph, return an ordering of nodes ordered by when they can be processed.
    None if cycles exist or if graph is undirected.

    After a node is processed, push it onto a stack, and if at any time we have a BACK edge
    then terminate the process.  Note that the graph can be unconnected so run a DFS from
    all undiscovered nodes.
    """

    class TSTraversal(dfs.Traversal):
        def __init__(self, graph):
            dfs.Traversal.__init__(self, graph)
            self.stack = []

        def node_processed(self, node):
            self.stack.append(node)

        def process_edge(self, source, target, edge):
            """
            When processing an edge ensure we have no back edges.
            """
            if target in self.node_state and self.node_state[target] == dfs.DISCOVERED:
                self.terminated = True

    traversal = TSTraversal(graph)
    for node in graph.nodes:
        if node not in traversal.node_state:
            dfs.dfs(node, traversal)
            if traversal.terminated:
                return False, None

    return True, traversal.stack
