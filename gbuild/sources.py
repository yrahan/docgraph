class Source(object):

    def __init__(self, name):
        self.name = name
        self.launchers = []
        self.launches = []
        self.dbs = []

    def is_launched_by(self, source):
        pass

    def is_launcher_of(self, source):
        pass


class App(Source):

    def __init__(self, name):
        super(App).__init__(self, name)


class Job(Source):

    def __init__(self, name):
        super(Job).__init__(self, name)


class Proc(Source):

    def __init__(self, name):
        super(Proc).__init__(self, name)


class db(object):

    def __init__(self, name):
        self.name = name
        self.users = []

    def used_by(self, source):
        pass
