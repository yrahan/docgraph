import os
import pygraphviz as pgv

from config import inputpath, outputpath, data_list
from sources import Node


def connect(s):
    content = lines[s.name]
    runs = [line.split() for line in content if "run" in line]
    uses = [line.split() for line in content if "use" in line]
    alters = [line.split() for line in content if "alter" in line]
    print content, runs, uses, alters
    children = [next(node for node in node_list if node.name == word[1])
                for word in runs + alters]
    parents = [next(node for node in node_list if node.name == word[1])
               for word in uses]
    for child in children:
        child.connect_to_parent(s)
    for parent in parents:
        parent.connect_to_parent(s)
# get list of sources in input directory
filenames = [f for f in os.listdir(inputpath) if not(f.endswith(".txt"))]

# getting the lines of the files
lines = {}
for name in filenames:
    with open(os.path.join(inputpath, name), 'r') as f:
        lines[name] = f.read().splitlines()
#  creating instances of source and storing them into node_list

node_list = [Node(n) for n in filenames + data_list]

# adding nodes

#G.add_node(child)
for s in node_list:
    if not s.is_data():
        connect(s)

# generating the dot file
G = pgv.AGraph(stric=False, directed=True)

# Graph name
G.graph_attr['label'] = "Test pack automatic documentation"

# trasposing connections into the graph
for data in data_list:
    G.add_node(data, color='green', shape='circle')
for source in filenames:
    G.add_node(source, color='red', shape='box')

for n in node_list:
    node = G.get_node(n.name)
    for c in n.children:
        child = G.get_node(c.name)
        G.add_edge(node, child)
# setting layout
G.layout(prog='dot')

# saving dot file
G.write(os.path.join(outputpath, 'graph.dot'))

# drawing

# G.draw(os.path.join(outputpath, 'graph.png'))
G.draw(os.path.join(outputpath, 'graph.ps'))
G.draw(os.path.join(outputpath, 'graph.png'))
