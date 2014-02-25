import os

from config import inputpath, data_list


# make valid conection
def connect_data_to_source(data_id, source_id, mode):
    data = 'data.' + data_id
    source = 'source.' + source_id
    with open(os.path.join(inputpath, source), 'a') as f:
        if mode == 'w':
            f.write('alter ' + data + '\n')
        else:
            f.write('use ' + data + '\n')


def connect_source_to_source(source1_id, source2_id):
    source1 = 'source.' + source1_id
    source2 = 'source.' + source2_id
    with open(os.path.join(inputpath, source2), 'a') as f:
        f.write('run ' + source1 + '\n')


# remove files in folder
def erase_folder_s_files(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception, e:
            print e


def create_file_set(size, inputpath, name_base):
    x = size[0]
    y = size[1]
    for i in range(y):
        for j in range(x):
            name = "{}.{}{}".format(name_base, i, j)
            filename = os.path.join(inputpath, name)
            with open(filename, 'w') as f:
                f.write('# ' + name + '\n')

# cleaning input directory
erase_folder_s_files(inputpath)
# write list into a text file
with open(os.path.join(inputpath, 'data_list.txt'), 'w') as f:
    for data in data_list:
        f.write(data + '\n')

# create app, job and source file sets
size = (6, 6)
name_base = 'source'
create_file_set(size, inputpath, name_base)


# make valid conection
# data -> source
connect_data_to_source('3', '52', 'r')
connect_data_to_source('3', '15', 'w')
connect_data_to_source('2', '33', 'w')
connect_data_to_source('9', '32', 'r')
# source -> source
connect_source_to_source('52', '41')
connect_source_to_source('52', '43')
connect_source_to_source('43', '33')
connect_source_to_source('33', '15')
connect_source_to_source('43', '15')
