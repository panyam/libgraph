
import base
import itertools

class Node(object):
    def __init__(self, key, **properties):
        self._key = key
        self._properties = properties
        self._neighbours = {}

    def __repr__(self):
        return repr(self._key)

    @property
    def neighbours(self):
        """
        A list of neighbour nodes.
        """
        return self._neighbours

    def iter_neighbours(self, reverse = False):
        """
        A list of neighbour nodes.
        """
        if reverse:
            return reversed(self._neighbours.items())
        else:
            return self._neighbours.iteritems()

    def ensure_neighbour(self, node, default_data):
        if node not in self._neighbours:
            self._neighbours[node] = default_data
        return self._neighbours[node]

    def add_neighbour(self, node, data):
        self._neighbours[node] = data

    def del_neighbour(self, node):
        if node in self._neighbours:
            del self._neighbours[node]

    @property
    def key(self):
        return self._key

    @property
    def properites(self):
        return self._properties

    def __hash__(self):
        return hash(self._key)

    def __cmp__(self, another):
        if hasattr(another, "key"):
            return cmp(self._key, another._key)
        else:
            return cmp(self._key, another)

class Graph(base.GraphBase):
    """
    Implementation of an undirected graph.
    """
    def __init__(self, multi = False, directed = False):
        base.GraphBase.__init__(self, multi, directed)
        self.nodes = {}

    def add_node(self, node):
        """
        Adds or update a node in the graph.  A node is any hashable object (or even a Node object).
        """
        if node not in self.nodes:
            # All the edges of the given node
            if not isinstance(node, Node):
                node = Node(node)
            self.nodes[node] = node
        return self.nodes[node]

    def get_edge(self, source, target):
        if source not in self.nodes:
            return None
        return self.nodes[source].neighbours.get(target, None)

    def add_raw_edge(self, edge):
        """
        Add a new Edge object into the graph.  If the edge's source and target nodes do not exist
        then new nodes are added implicitly.  Returns an Edge object whose properties can be set.  
        Optionally the properties can be passed to this method and they will be set in the returned 
        Edge object.
        """
        source,target = edge.source, edge.target
        if self.is_multi:
            self.nodes[source].ensure_neighbour(target, []).append(edge)
            if not self.is_directed:
                self.nodes[target].ensure_neighbour(source, []).append(edge)
        else:
            self.nodes[source].add_neighbour(target, edge)
            if not self.is_directed:
                self.nodes[target].add_neighbour(source, edge)

    def iter_neighbours(self, node, reverse = False):
        return node.iter_neighbours(reverse = reverse)

    def iter_node_edges(self, nodekey):
        """
        Returns an iterator over all edges for a given node.  The ordering of edges is unspecified.
        """
        if self.is_multi:
            return itertools.chain(itertools.imap(iter, self.nodes[nodekey]))
        else:
            return self.nodes[nodekey].neighbours.itervalues()

    def iter_edges(self):
        """
        Returns an iterator over all edges in the graph.  The ordering of edges is unspecified.
        """
        for source in self.nodes.iterkeys():
            for target, edge in self.nodes[source].neighbours.iteritems():
                # Only yield the edge if it originates form here, 
                # this would take care of the case of both directed
                # and undirected edges
                if self.is_multi:
                    for e in edges:
                        if e.source == source:
                            yield e
                elif edge.source == source:
                    yield edge

    def del_node(self, node):
        """
        Delete a node in the graph.  This also removes all of the nodes incident edges.
        """
        targets = self.nodes[node][:]
        for t in targets:
            self.nodes[t].del_neighbour(node)
        del self.nodes[node]

    def del_edge(self, source, target):
        """
        Delete all edge between two nodes.
        """
        if source in self.nodes and target in self.nodes:
            self.nodes[source].del_neighbour(target)
            if not self.is_directed:
                self.nodes[target].del_neighbour(source)

