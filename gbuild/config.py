import os

# directory of input files
inputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'input'))
# directory of input files
outputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'output'))
# create datanamesbase list
datanames = []
for i in range(10):
    datanames.append("{}.{}".format("data", i))
