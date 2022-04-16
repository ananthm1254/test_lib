import ctypes
from libs.constants import *
import os

def initiliaze_shared_library():
    '''
    Initializes the shared library module from the project
    '''
    path = os.path.dirname(os.path.realpath(__file__)) + "/../../"
    lib = ctypes.CDLL(path + SHARED_OBJECT_FILE)
    return lib

    
def send_payload(lib, cmd=None, input_dict=None, verbose=False):
    pass
    