import ctypes

class AddressSpecific(ctypes.Structure):
    _fields_ = [
        ("block_address", ctypes.c_uint8),
        ("page_address", ctypes.c_uint8),
        ("offset", ctypes.c_uint8),
        ("Reserved", ctypes.c_uint8)
    ]


class Address(ctypes.Union):
    _fields_ = [
        ("address", ctypes.c_uint32),
        ("addressSpecific", AddressSpecific)
    ]
class EraseMsg(ctypes.Structure):
    _fields_ = [
        ("address", Address),
        ("respQId", ctypes.c_uint32)
    ]

class WriteMsg(ctypes.Structure):
    _fields_ = [
        ("address", Address),
        ("buffPtr", ctypes.POINTER(ctypes.c_uint8)),
        ("respQId", ctypes.c_uint32)
    ]

class ReadMsg(ctypes.Structure):
    _fields_ = [
        ("address", Address),
        ("buffPtr", ctypes.POINTER(ctypes.c_uint8)),   
        ("respQId", ctypes.c_uint32)
    ]

class CmdMsg(ctypes.Union):
    __fields_ = [
        ("eraseMsg", EraseMsg),
        ("writeMsg", WriteMsg),
        ("readMsg", ReadMsg)
    ]