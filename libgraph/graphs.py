
class Edge(object):
    def __init__(self, source, target, data = None):
        self._source, self._target, self.data = source, target, data

    def __repr__(self):
        return "Edge<%s <-> %s>" % (repr(self.source), repr(self.target))

    @property
    def source(self): return self._source

    @property
    def target(self): return self._target

class Graph(object):
    def __init__(self, multi = False, directed = False, key_func = None, neighbors_func = None):
        self.nodes = {}
        self._is_directed = directed
        self._is_multi = multi
        self.neighbors_func = neighbors_func
        self.key_func = key_func or (lambda x: x)

    @property
    def is_directed(self): return self._is_directed
    @property
    def is_multi(self): return self._is_multi

    def get_edge(self, source, target):
        return self.nodes.get(self.key_func(source), {}).get(self.key_func(target), None)

    def add_nodes(self, *nodes):
        return [self.add_node(node) for node in nodes]

    def add_node(self, node):
        """
        Adds or update a node (any hashable) in the graph.
        """
        if node not in self.nodes: self.nodes[self.key_func(node)] = {}
        return self.nodes[self.key_func(node)]

    def neighbors(self, node):
        """Return the neighbors of a node."""
        if self.neighbors_func:
            return self.neighbors_func(node)
        else:
            return self.nodes.get(self.key_func(node), {})

    def iter_neighbors(self, node, reverse = False):
        """
        Return an iterator of neighbors (along with any edge data) for a particular node.
        Override this method for custom node storage and inspection strategies.
        """
        neighbors = self.neighbors(node)
        if type(neighbors) is dict:
            if reverse: return reversed(self.neighbors(node).items())
            else: return self.neighbors(node).iteritems()
        else:
            if reverse: return reversed(neighbors)
            else: return neighbors

    def add_raw_edge(self, edge):
        self.add_nodes(edge.source,edge.target)
        source,target = edge.source,edge.target
        source_key = self.key_func(source)
        target_key = self.key_func(target)
        self.nodes[source_key][target_key] = edge
        if not self.is_directed:
            self.nodes[target_key][source_key] = edge
        return edge

    def add_edge(self, source, target):
        return self.add_raw_edge(Edge(source, target))

    def add_edges(self, *edges):
        return [self.add_edge(*e) for e in edges]
