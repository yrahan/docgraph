class Node(object):
    """Class for nodes of a graph.

    Instances of this class can be code source or ressources (data)
    """

    def __init__(self, name, ftype):
        self.name = name
        self.parents = []
        self.children = []
        self.ftype = ftype

    def is_child_of(self, node):
        return node.name in self.parents

    def is_parent_of(self, node):
        return node.name in self.children

    def is_connected(self):
        return self.name in (self.children + self.parents)

    def connect_to_parent(self, node):
        if not(self.is_child_of(node)):
            node.children.append(self)
            self.parents.append(node)

    def connect_to_child(self, node):
        if not(self.is_parent_of(node)):
            node.parents.append(self)
            self.children.append(node)
