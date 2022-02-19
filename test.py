import ctypes
from libs.structures import Voter, Party, Issues

class PartyList(ctypes.Structure):
    _fields_ = [
        ("num", ctypes.c_uint32),
        ("voter", Voter),
        ("partylist", (2*Party))
    ]

    def __init__(self, num, voter, partylist):
        self.num = num
        self.voter = voter

        for i in range(0, num):
            self.partylist[i] = partylist[i]
        super(PartyList, self).__init__(num, voter, partylist)

lib = ctypes.CDLL("../build/sim_test.so")

print(ctypes.sizeof(Issues), ctypes.sizeof(Voter), ctypes.sizeof(Party), ctypes.sizeof(PartyList))
issues = Issues(1,3)
voter = Voter(1, 25, issues)

partylist = (2*Party)()
partylist[0] = Party(1, Issues(1,2))
partylist[1] = Party(2, Issues(4,3))

partylist_type = PartyList(2, voter, partylist)
partylist_type.partylist[0].print_struct()
partylist_type.partylist[1].print_struct()

lib.FeCmdHandler.argtypes = [ctypes.c_uint32, ctypes.POINTER(PartyList), ctypes.POINTER(Party)]

party = Party(0, Issues(0,0))

lib.FeCmdHandler(ctypes.c_uint(2), ctypes.byref(partylist_type), ctypes.byref(party))
party.print_struct()
