import ctypes

class Issues(ctypes.Structure):
    _fields_ = [
        ("social", ctypes.c_uint32),
        ("economic", ctypes.c_uint32)
    ]

    def __init__(self, social=None, economic=None):
        if not social:
            self.social = social
        if not economic:
            self.economic = economic

        super(Issues, self).__init__(social, economic)

    def print_struct(self):
        print("social : {} and economic : {}".format(self.social, self.economic))

class Voter(ctypes.Structure):
    _fields_ = [
        ("tag", ctypes.c_uint64),
        ("age", ctypes.c_uint32),
        ("issues", Issues)
    ]

    def __init__(self, tag=None, age=None, issues=None):
        if not tag:
            self.tag = tag
        if not age:
            self.age = age
        if not issues:
            self.issues = issues

        super(Voter, self).__init__(tag, age, issues)
    
    def print_struct(self):
        print("tag : {} and age : {}".format(self.tag, self.age))
        self.issues.print_struct()

class Party(ctypes.Structure):
    _fields_ = [
        ("tag", ctypes.c_uint64),
        ("issues", Issues)
    ]

    def __init__(self, tag=None, issues=None):
        if not tag:
            self.tag = tag
        if not issues:
            self.issues = issues

        super(Party, self).__init__(tag, issues)
    
    def print_struct(self):
        print("tag : {}".format(self.tag))
        self.issues.print_struct()