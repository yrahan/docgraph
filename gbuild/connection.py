import os
import pygraphviz as pgv

from config import inputpath, outputpath  # , db_names

# get list of files in input directory
filenames = [f for f in os.listdir(inputpath) if f.endswith("txt")]
filenames.remove("db.txt")
# getting the lines of the files
lines = {}
for name in filenames:
    with open(os.path.join(inputpath, name), 'r') as f:
        lines[name.replace('.txt', '')] = f.read().splitlines()
# loading informations into dictionnaries
filenames = [f.replace('.txt', '') for f in filenames]
procs = [n for n in filenames if 'proc' in n]
jobs = [n for n in filenames if 'job' in n]
apps = [n for n in filenames if 'app' in n]
print lines
# generating the dot file
G = pgv.AGraph(stric=False, directed=True)
# adding nodes
# entry point = proc52
child = 'proc52'
procs.remove(child)
G.add_node(child)
for p in procs:
    if any(child in line for line in lines[p]):


   G.add_node(p)
# setting layout
G.layout(prog='dot')
# saving dot file
G.write(os.path.join(outputpath, 'graph.dot'))
# drawing
# G.draw(os.path.join(outputpath, 'graph.png'))
G.draw(os.path.join(outputpath, 'graph.ps'))
G.draw(os.path.join(outputpath, 'graph.png'))
