import os

# directory of input files
inputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'input'))
# directory of input files
outputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'output'))
# create database list
db_names = []
for i in range(10):
    db_names.append("{}{}".format("db", i))
