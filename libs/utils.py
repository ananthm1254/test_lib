import ctypes
import random
from libs.constants import SHARED_OBJECT_FILE
import os
from libs import structures


def initiliaze_shared_library(lib_file=None):
    """
    Initializes the shared library module from the project
    """
    if lib_file:
        path = lib_file
        lib = ctypes.CDLL(lib_file)
    else:
        path = os.path.dirname(os.path.realpath(__file__)) + "/../../"
        lib = ctypes.CDLL(path + SHARED_OBJECT_FILE)
    return lib


def erase_direct(lib, args):
    if args is None:
        raise Exception("Nonetype args are not allowed")
    else:
        erase_msg = structures.EraseMsg()
        erase_msg.Address.AddressSpecific.BlockAddress = args["block_address"]
        erase_msg.Address.AddressSpecific.PageAddress = args["page_address"]
        erase_msg.Address.AddressSpecific.Offset = 0
        erase_msg.RespQid = args["resp_qid"]
        return lib.FileErase(ctypes.byref(erase_msg))


def write_direct(lib, args):
    if args is None:
        raise Exception("Nonetype args are not allowed")
    else:
        write_msg = structures.WriteMsg()
        write_msg.Address.AddressSpecific.BlockAddress = args["block_address"]
        write_msg.Address.AddressSpecific.PageAddress = args["page_address"]
        write_msg.Address.AddressSpecific.Offset = 0
        write_msg.RespQid = args["resp_qid"]
        write_msg.BuffPtr = args["buff_ptr"]
        return lib.FileWrite(ctypes.byref(write_msg))


def read_direct(lib, args):
    if args is None:
        raise Exception("Nonetype args are not allowed")
    else:
        read_msg = structures.ReadMsg()
        read_msg.Address.AddressSpecific.BlockAddress = args["block_address"]
        read_msg.Address.AddressSpecific.PageAddress = args["page_address"]
        read_msg.Address.AddressSpecific.Offset = args["offset"]
        read_msg.RespQid = args["resp_qid"]
        read_msg.BuffPtr = args["buff_ptr"]
        return lib.FileRead(ctypes.byref(read_msg)), read_msg.BuffPtr


def generate_write_buffer(length, seed=None):
    if seed is not None:
        random.seed(seed)
    temp = [random.randint(0, 255) for i in range(0, length)]
    buffer = (ctypes.c_uint8 * len(temp))(*temp)
    ctypes.cast(buffer, ctypes.POINTER(ctypes.c_uint8))
    return buffer


def generate_read_buffer(length):
    temp = [0 for i in range(0, length)]
    buffer = (ctypes.c_uint8 * len(temp))(*temp)
    ctypes.cast(buffer, ctypes.POINTER(ctypes.c_uint8))
    return buffer


def send_payload(lib, cmd=None, input_dict=None, verbose=False):
    pass
