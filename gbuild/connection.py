import os
import pygraphviz as pgv

from config import inputpath, outputpath
from sources import Node

# initialize list of sources and ressources
node_list = []
data_list = []


def connect(s):
    """
    Connect source node s to source nodes and data nodes.

    A line containing :
        - run source, makes source node as child
        - use data, makes data node as child
        - alter data, makes data node as parent
        - fill in the data_list
    """
    global node_list
    global data_list
    # get content of source file s
    content = lines[s.name]
    # get informations about s launching another source file
    runs = [line.split() for line in content if "run" in line]
    # get informations about s reading a data
    uses = [line.split() for line in content if "use" in line]
    # get information about s modifying a data
    alters = [line.split() for line in content if "alter" in line]
    print content, runs, uses, alters
    # create data node if not exists
    for words in (uses + alters):
        dataname = words[1]
        if not dataname in data_list:
            data_list.append(dataname)
            node_list.append(Node(dataname, True))
    # define nodes to be children
    children = [next(node for node in node_list if node.name == word[1])
                for word in runs + alters]
    # define node to be parents
    parents = [next(node for node in node_list if node.name == word[1])
               for word in uses]
    # make connections
    for child in children:
        child.connect_to_parent(s)
    for parent in parents:
        parent.connect_to_child(s)

# get list of sources in input directory
filenames = [f for f in os.listdir(inputpath) if not(f.endswith(".txt"))]

# read files' lines
lines = {}
for name in filenames:
    with open(os.path.join(inputpath, name), 'r') as f:
        lines[name] = f.read().splitlines()

node_list = [Node(f, False) for f in filenames]
# connect the nodes by updating the attributes
for s in node_list:
    if s.is_source:
        connect(s)
# create the graph
G = pgv.AGraph(stric=False, directed=True)

# name graph
G.graph_attr['label'] = "Test pack automatic documentation"

# copy the node and their connections to the graph
# add data nodes to the graph
for data in data_list:
    G.add_node(data, color='green', shape='circle')
# add source nodes to the graph
for source in filenames:
    G.add_node(source, color='red', shape='box')
# make the edges
for n in node_list:
    node = G.get_node(n.name)
    for c in n.children:
        child = G.get_node(c.name)
        G.add_edge(node, child)
# save data_list as file
with open(os.path.join(outputpath, 'data_connected.txt'), 'w') as f:
    for dataname in data_list:
        f.write(dataname + '\n')
# setting layout
G.layout(prog='dot')

# saving dot file
G.write(os.path.join(outputpath, 'graph.dot'))

# drawing
G.draw(os.path.join(outputpath, 'graph.ps'))
G.draw(os.path.join(outputpath, 'graph.png'))
