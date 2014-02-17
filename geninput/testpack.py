import os


# make valid conection
def connect_db_to_proc(db_id, proc_id):
    db = 'db' + db_id
    proc = 'proc' + proc_id + '.txt'
    with open(os.path.join(inputpath, proc), 'a') as f:
        f.write('uses ' + db + '\n')


def connect_proc_to_proc(proc1_id, proc2_id):
    proc1 = 'proc' + proc1_id + '.txt'
    proc2 = 'proc' + proc2_id + '.txt'
    with open(os.path.join(inputpath, proc2), 'a') as f:
        f.write('execs ' + proc1 + '\n')


def connect_proc_to_job(proc_id, job_id):
    proc = 'proc' + proc_id + '.txt'
    job = 'job' + job_id + '.txt'
    with open(os.path.join(inputpath, job), 'a') as f:
        f.write('execs ' + proc + '\n')


def connect_job_to_job(job1_id, job2_id):
    job1 = 'job' + job1_id + '.txt'
    job2 = 'job' + job2_id + '.txt'
    with open(os.path.join(inputpath, job2), 'a') as f:
        f.write('execs ' + job1 + '\n')


def connect_job_to_app(job_id, app_id):
    job = 'job' + job_id + '.txt'
    app = 'app' + app_id + '.txt'
    with open(os.path.join(inputpath, app), 'a') as f:
        f.write('execs ' + job + '\n')


# remove files in folder
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
                f.write('# ' + name + '\n')


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
file_type = {'app': 'txt', 'job': 'txt', 'proc': 'txt', }
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
# job -> app
connect_job_to_app('10', '01')
connect_job_to_app('12', '01')
connect_job_to_app('14', '03')
connect_job_to_app('04', '04')
# job -> app
connect_job_to_job('14', '04')
# proc -> job
connect_proc_to_job('41', '10')
connect_proc_to_job('33', '12')
connect_proc_to_job('15', '14')
# proc -> proc
connect_proc_to_proc('52', '41')
connect_proc_to_proc('52', '43')
connect_proc_to_proc('43', '33')
connect_proc_to_proc('33', '15')
connect_proc_to_proc('43', '15')
