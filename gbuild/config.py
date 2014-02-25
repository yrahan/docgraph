import os

# directory of input files
inputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'input'))
# directory of input files
outputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'output'))
# create data_listbase list
data_list = []
for i in range(10):
    data_list.append("{}.{}".format("data", i))
