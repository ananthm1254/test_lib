import ctypes

from libs.constants import NUMBER_OF_PARTIES

'''
Base Structures 
'''
class Issues(ctypes.Structure):
    _fields_ = [
        ("social", ctypes.c_uint32),
        ("economic", ctypes.c_uint32)
    ]

    def convert_to_dict(self):
        dict = {
            "social" : self.social,
            "economic" : self.economic
        }
        return dict

class Voter(ctypes.Structure):
    _fields_ = [
        ("tag", ctypes.c_uint64),
        ("age", ctypes.c_uint32),
        ("issues", Issues)
    ]

    def convert_to_dict(self):
        dict = {
            "tag" : self.tag,
            "age" : self.age,
            "issues" : self.issues.convert_to_dict()
        }
        return dict

class Party(ctypes.Structure):
    _fields_ = [
        ("tag", ctypes.c_uint64),
        ("issues", Issues)
    ]

    def convert_to_dict(self):
        dict = {
            "tag" : self.tag,
            "issues" : self.issues.convert_to_dict()
        }
        return dict

'''
Cmd Payload Structures
'''

# FE_TASK_INIT_BE
class BeInitInputPayload(ctypes.Structure):
    _fields_ = [
        ("numberOfParties", ctypes.c_uint32),
        ("voter", Voter),
        ("partylist", (NUMBER_OF_PARTIES*Party))
    ]

class BeInitOutputPayload(ctypes.Structure):
    _fields_ = [
        ("status", ctypes.c_uint32),
        ("vote_received", Party)
    ]

# FE_TASK_INTEGRITY_CHECK
class BeIntgrInputPayload(ctypes.Structure):
    _fields_ = [
        ("num", ctypes.c_uint32),
        ("voter", Voter),
        ("partylist", (NUMBER_OF_PARTIES*Party))
    ]

class BeIntgrOutputPayload(ctypes.Structure):
    _fields_ = [
        ("status", ctypes.c_uint32),
        ("vote_received", Party)
    ]


# FE_TASK_VOTE_CMD
class VoteCmdInputPayload(ctypes.Structure):
    _fields_ = [
        ("numberOfParties", ctypes.c_uint32),
        ("voter", Voter),
        ("partylist", (NUMBER_OF_PARTIES*Party))
    ]

    def convert_to_dict(self):
        dict = {
            "numberOfParties" : self.numberOfParties,
            "voter" : self.voter.convert_to_dict(),
        }
        for i in range(0, self.numberOfParties):
            dict["party{}".format(i+1)] = self.partylist[i].convert_to_dict()
        return dict

class VoteCmdOutputPayload(ctypes.Structure):
    _fields_ = [
        ("status", ctypes.c_uint32),
        ("voteReceived", Party)
    ]

    def convert_to_dict(self):
        dict = {
            "status" : self.numberOfParties,
            "voteReceived" : self.voteReceived.convert_to_dict(),
        }
        return dict