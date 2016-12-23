import itertools, ipdb

class Edge(object):
    def __init__(self, source, target):
        self._source, self._target = source, target

    @property
    def source(self): return self._source
    @property
    def target(self): return self._target

    def __repr__(self):
        return "Edge<%s <-> %s>" % (repr(self.source), repr(self.target))

class Graph(object):
    def __init__(self, multi = False, directed = False):
        self.nodes = {}
        self._is_directed = directed
        self._is_multi = multi

    @property
    def is_directed(self): return self._is_directed
    @property
    def is_multi(self): return self._is_multi

    def get_edge(self, source, target):
        return self.nodes.get(source, {}).get(target, None)

    def add_nodes(self, *nodes):
        return [self.add_node(node) for node in nodes]

    def add_node(self, node):
        """
        Adds or update a node (any hashable) in the graph.
        """
        if node not in self.nodes:
            self.nodes[node] = {}
        return self.nodes[node]

    def neighbours(self, node):
        """Return the neighbours of a node."""
        return self.nodes.get(node, {})

    def iter_edges(self, node, reverse = False):
        """ Return an iterator of edges from a given node. """
        if reverse: return reversed(self.neighbours(node).items())
        else: return self.neighbours(node).iteritems()

    def add_raw_edge(self, edge):
        self.add_nodes(edge.source,edge.target)
        source,target = edge.source,edge.target
        self.nodes[source][target] = edge
        if not self.is_directed:
            self.nodes[target][source] = edge
        return edge

    def add_edge(self, source, target):
        return self.add_raw_edge(Edge(source, target))

    def add_edges(self, *edges):
        return [self.add_edge(*e) for e in edges]
