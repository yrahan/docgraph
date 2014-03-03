import os

from config import inputpath, outputpath


def prepare_io_folders(folders_list):
    """Create folder in folders_list."""
    for folder in folders_list:
        if not os.path.exists(folder):
            os.makedirs(folder)


def erase_folder_s_files(folder):
    """erase only files in folder """
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception, e:
            print e


def create_file_set(size, inputpath, name_base):
    """create size[0] x size[1] files in inputpath.

    Write the filename as the first line of each file.

    """
    x = size[0]
    y = size[1]
    for i in range(y):
        for j in range(x):
            name = "{}.{}{}".format(name_base, i, j)
            filename = os.path.join(inputpath, name)
            with open(filename, 'w') as f:
                f.write('# ' + name + '\n')


def create_data_list_file(data_list, inputpath, name_base):
    """Store data names in a file in inputpath directory. """
    with open(os.path.join(inputpath, name_base), 'w') as f:
        for data in data_list:
            f.write(data + '\n')


def connect_data_to_source(data_id, source_id, mode):
    """Interaction between a source code
    and a ressource data.

    If mode is 'w', source alters data, else source only
    uses data.
    """
    data = 'data.' + data_id
    source = 'source.' + source_id
    with open(os.path.join(inputpath, source), 'a') as f:
        if mode == 'w':
            f.write('alter ' + data + '\n')
        else:
            f.write('use ' + data + '\n')


def connect_source_to_source(source1_id, source2_id):
    """Make source2 launch source2."""
    source1 = 'source.' + source1_id
    source2 = 'source.' + source2_id
    with open(os.path.join(inputpath, source2), 'a') as f:
        f.write('run ' + source1 + '\n')


# create input and output folders
prepare_io_folders([inputpath, outputpath])
# clean up input directory
erase_folder_s_files(inputpath)

# save ressource names.
data_list = ["data.{}".format(i) for i in range(3)]
name_base = 'data_list.txt'
create_data_list_file(data_list, inputpath, name_base)

# create sources
size = (4, 4)
name_base = 'source'
create_file_set(size, inputpath, name_base)

# connect data and sources
connect_data_to_source('1', '12', 'r')
connect_data_to_source('1', '22', 'w')
connect_data_to_source('2', '02', 'r')
connect_data_to_source('2', '11', 'w')
# connect sources
connect_source_to_source('03', '13')
connect_source_to_source('23', '32')
connect_source_to_source('12', '23')
connect_source_to_source('22', '31')
connect_source_to_source('20', '31')
connect_source_to_source('11', '22')
connect_source_to_source('11', '20')
connect_source_to_source('02', '12')
connect_source_to_source('02', '11')
