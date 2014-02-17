import os


def erase_folder_s_files(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception, e:
            print e


def create_file_set(size, inputpath, name_base, extention):
    x = size[0]
    y = size[1]
    for i in range(y):
        for j in range(x):
            name = "{}{}{}{}{}".format(name_base, i, j, '.', extention)
            filename = os.path.join(inputpath, name)
            with open(filename, 'w') as f:
                f.write('# ' + name)


def create_3_type_of_file_sets():
    # defining procedure test pack
    size = (6, 6)
    name_base = 'proc'
    extention = file_type['proc']
    create_file_set(size, inputpath, name_base, extention)
    # defining procedure test pack
    size = (6, 2)
    name_base = 'job'
    extention = file_type['job']
    create_file_set(size, inputpath, name_base, extention)
    # defining job test pack
    size = (6, 1)
    name_base = 'app'
    extention = file_type['app']
    create_file_set(size, inputpath, name_base, extention)


# directory of input files
inputpath = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'input'))
# cleaning input directory
erase_folder_s_files(inputpath)
# define file types extensions
file_type = {'app': 'jcl', 'job': 'jcl', 'proc': 'sql', }
# create database list
db_names = []
for i in range(10):
    db_names.append("{}{}".format("db", i))
# write list into a text file
with open(os.path.join(inputpath, 'db.txt'), 'w') as f:
    for db in db_names:
        f.write(db + '\n')

# create app, job and proc file sets
create_3_type_of_file_sets()
# make valid conection


def connect_proc_to_db():
    pass


def connect_proc_to_proc(proc1, proc2):
    pass


def connect_proc_to_job():
    pass


def connect_job_to_job():
    pass


def connect_job_to_app():
    pass
