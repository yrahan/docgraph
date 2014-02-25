from config import data_list


class Node(object):

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.used_data = []

    def is_child_of(self, node):
        return node.name in self.parents

    def is_parent_of(self, node):
        return node.name in self.children

    def is_connected(self):
        return self.name in (self.children + self.parents)

    def is_source(self):
        return self.name not in data_list

    def is_data(self):
        return self.name in data_list

    def connect_to_parent(self, node):
        if not(self.is_child_of(node)):
            node.children.append(self)
            self.parents.append(node)

    def connect_to_child(self, node):
        if not(self.is_parent_of(node)):
            node.parents.append(self)
            self.children.append(node)
