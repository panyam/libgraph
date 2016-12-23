
class Edge(object):
    def __init__(self, source, target, directed = False):
        self._source = source
        self._target = target
        self._directed = directed

    def __repr__(self):
        if self._directed:
            return "Edge<%s --> %s>" % (repr(self.source), repr(self.target))
        else:
            return "Edge<%s <-> %s>" % (repr(self.source), repr(self.target))

    @property
    def is_directed(self):
        return self._directed

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target

class GraphBase(object):
    """
    Interface of all graphs.  Inherit from this and override implementations to suit needs.
    """
    def __init__(self, multi = False, directed = False):
        self._is_directed = directed
        self._is_multi = multi

    @property
    def is_multi(self): return self._is_multi
    @property
    def is_directed(self): return self._is_directed

    def add_nodes(self, *nodes):
        return [self.add_node(node) for node in nodes]

    def add_edges(self, *source_target_pairs):
        for source, target in source_target_pairs:
            self.add_edge(source, target)

    def add_node(self, node):
        """
        Adds or update a node in the graph.  A node is any hashable object (or even a Node object).
        """
        assert False, "Not Implemented"

    def get_edge(self, source, target):
        assert False, "Not Implemented"

    def add_raw_edge(self, edge):
        assert False, "Not Implemented"

    def add_edge(self, source, target):
        """
        Add a new Edge object into the graph.  If the edge's source and target nodes do not exist
        then new nodes are added implicitly.  Returns an Edge object whose properties can be set.  
        Optionally the properties can be passed to this method and they will be set in the returned 
        Edge object.
        """
        source, target = self.add_nodes(source, target)
        newedge = Edge(source, target, directed = self.is_directed)
        return self.add_raw_edge(newedge)

    def iter_neighbours(self, node, reverse = False):
        assert False, "Not Implemented"

    def iter_node_edges(self, nodekey):
        """
        Returns an iterator over all edges for a given node.  The ordering of edges is unspecified.
        """
        assert False, "Not Implemented"

    def iter_edges(self):
        """
        Returns an iterator over all edges in the graph.  The ordering of edges is unspecified.
        """
        assert False, "Not Implemented"

    def del_node(self, node):
        """
        Delete a node in the graph.  This also removes all of the nodes incident edges.
        """
        assert False, "Not Implemented"

    def del_edge(self, source, target):
        """
        Delete all edge between two nodes.
        """
        assert False, "Not Implemented"


