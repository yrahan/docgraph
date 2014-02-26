import os

# directory of input files
inputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'input'))
# directory of input files
outputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'output'))
# create data_listbase list
with open(os.path.join(inputpath, 'data_list.txt'), 'r') as f:
    data_list = f.read().splitlines()
