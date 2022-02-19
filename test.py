import ctypes

class Issues(ctypes.Structure):
    _fields_ = [
        ("social", ctypes.c_uint),
        ("economic", ctypes.c_uint)
    ]

    # def __init__(self, socialIssues=None, economicIssues=None):
    #     if not socialIssues:
    #         self.socialIssues = socialIssues
    #     if not economicIssues:
    #         self.economicIssues = economicIssues

    #     super(Issues, self).__init__(socialIssues, economicIssues)

class Voter(ctypes.Structure):
    _fields_ = [
        ("tag", ctypes.c_longlong),
        ("age", ctypes.c_uint),
        ("issues", Issues)
    ]

lib = ctypes.CDLL("../build/sim_test.so")

issues = Issues()

lib.IssuesInit.argtypes = [ctypes.c_uint, ctypes.c_uint]
lib.IssuesInit.restype = (Issues)

issues = lib.IssuesInit(1,2)

assert((issues.social == 1) and (issues.economic == 2))
