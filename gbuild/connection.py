# import sys
import os
import pygraphviz as pgv

from config import inputpath, outputpath
from config import patterns
from config import NodeType
from sources import Node

# initialize list of sources and ressources
node_list = []
data_list = []


def getFileList(inputpath):
    return [f for f in os.listdir(inputpath) if not(f.endswith(".txt"))]


def loadFiles(inputpath, filenames):
    lines = {}
    for name in filenames:
        with open(os.path.join(inputpath, name), 'r') as f:
            lines[name] = f.read().splitlines()
    return lines


def getNodeType(lines, filename):
    # check if file not empty
    if lines[filename]:
        firstLine = lines[filename][0]
        if patterns['fexBeginEndComments'].search(firstLine):
            return NodeType.fex
        elif patterns['jclLine1'].search(firstLine):
            return NodeType.jcl
        else:
            return NodeType.other
    else:
        return NodeType.other


def getJclRuns(content):
    runs = []
    for line in content:
        if patterns['jclRunFex'].search(line):
            runs.append(patterns['jclRunFex'].search(line).group(1))
    return runs


def getFexInputs(content):
    uses = []
    # to rewrite using iterator ? generator ?
    while True:
        try:
            i = iter(content)
            line = i.next()
            while (not patterns['fexInputTag'].search(line)):
                line = i.next()
            uses.append(patterns['fexInputTag'].search(line).group(1))
            line = i.next()
            while (patterns['fexAddIO'].search(line)):
                uses.append(patterns['fexAddIO'].search(line).group(1))
                line = i.next()
            raise StopIteration
        except StopIteration:
            return uses


def getFexOutputs(content):
    alters = []
    # to rewrite using iterator ? generator ?
    while True:
        try:
            i = iter(content)
            line = i.next()
            while (not patterns['fexOutputTag'].search(line)):
                line = i.next()
            alters.append(patterns['fexOutputTag'].search(line).group(1))
            line = i.next()
            while (patterns['fexAddIO'].search(line)):
                alters.append(patterns['fexAddIO'].search(line).group(1))
                line = i.next()
            raise StopIteration
        except StopIteration:
            return alters


def connect(lines, s):
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
    runs = []
    uses = []
    alters = []
    # get content of source file s
    content = lines[s.name]
    # get file type
    if s.ftype == NodeType.jcl:
        runs = getJclRuns(content)
    elif s.ftype == NodeType.fex:
        uses = getFexInputs(content)
        alters = getFexOutputs(content)
    else:
        return None
    print runs, uses, alters
    # create data node if not exists
    for dataname in (uses + alters):
        if not dataname in data_list:
            data_list.append(dataname)
            node_list.append(Node(dataname, NodeType.data))
    # define nodes to be children
    children = [next(node for node in node_list if node.name == child)
                for child in runs + alters]
    # define node to be parents
    parents = [next(node for node in node_list if node.name == parent)
               for parent in uses]
    # make connections
    for child in children:
        child.connect_to_parent(s)
    for parent in parents:
        parent.connect_to_child(s)


# get list of sources in input directory
filenames = getFileList(inputpath)
# read files' lines
lines = loadFiles(inputpath, filenames)
# build Nodes for jcl and fex files
node_list = [Node(f, getNodeType(lines, f)) for f in filenames]
# connect the nodes by updating the attributes
for source in node_list:
    print source.name
    if source.name not in data_list:
        connect(lines, source)

#sys.exit()
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
