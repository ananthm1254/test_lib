from libs.structures import *
from ctypes import *
from libs.constants import *
import os

def initiliaze_shared_library():
    '''
    Initializes the shared library module from the project
    '''
    path = os.path.dirname(os.path.realpath(__file__)) + "/../../../"
    lib = ctypes.CDLL(path + SHARED_OBJECT_FILE)
    return lib

def initialize_be_init_payload(input_dict):
    input_payload = Voter()
    input_payload.tag = input_dict["tag"]
    input_payload.age = input_dict["age"]
    input_payload.issues.social = input_dict["issues"]["social"]
    input_payload.issues.economic = input_dict["issues"]["economic"]
    return input_payload

def initialize_be_integrity_payload():
    return None

def initialize_vote_cmd_payload(input_dict):
    input_payload  = VoteCmdInputPayload()
    input_payload.numberOfParties = input_dict["numberOfParties"]
    input_payload.voter.tag = input_dict["voter"]["tag"]
    input_payload.voter.age = input_dict["voter"]["age"]
    input_payload.voter.issues.social = input_dict["voter"]["issues"]["social"]
    input_payload.voter.issues.economic = input_dict["voter"]["issues"]["economic"]
    for i in range(0,input_dict["numberOfParties"]):
        input_payload.partylist[i].tag = input_dict["partylist"]["party{}".format(i+1)]["tag"]
        input_payload.partylist[i].issues.social = input_dict["partylist"]["party{}".format(i+1)]["issues"]["social"]
        input_payload.partylist[i].issues.economic = input_dict["partylist"]["party{}".format(i+1)]["issues"]["economic"]

    return input_payload

    
def send_payload(lib, cmd=FE_TASK_INIT_BE, input_dict=None, verbose=False):
    if cmd == FE_TASK_FE_INIT:
        lib.FeCmdHandler.argtypes = [c_uint32, c_void_p, POINTER(c_uint32)]
        input_payload = c_void_p()
        output_payload = c_uint32()
    if cmd == FE_TASK_INIT_BE:
        lib.FeCmdHandler.argtypes = [c_uint32, POINTER(Voter), POINTER(Voter)]
        input_payload = initialize_be_init_payload(input_dict)
        output_payload = Voter()
    lib.FeCmdHandler(cmd, byref(input_payload), byref(output_payload))
    print(output_payload)
    return output_payload
    