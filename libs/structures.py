import ctypes


class AddressSpecific(ctypes.Structure):
    _fields_ = [
        ("BlockAddress", ctypes.c_uint8),
        ("PageAddress", ctypes.c_uint8),
        ("Offset", ctypes.c_uint8),
        ("Reserved", ctypes.c_uint8)
    ]


class Address(ctypes.Union):
    _fields_ = [
        ("Address", ctypes.c_uint32),
        ("AddressSpecific", AddressSpecific)
    ]


class EraseMsg(ctypes.Structure):
    _fields_ = [
        ("Address", Address),
        ("RespQId", ctypes.c_uint32)
    ]


class WriteMsg(ctypes.Structure):
    _fields_ = [
        ("Address", Address),
        ("BuffPtr", ctypes.POINTER(ctypes.c_uint8)),
        ("RespQId", ctypes.c_uint32)
    ]


class ReadMsg(ctypes.Structure):
    _fields_ = [
        ("Address", Address),
        ("BuffPtr", ctypes.POINTER(ctypes.c_uint8)),
        ("RespQId", ctypes.c_uint32)
    ]


class CmdMsg(ctypes.Union):
    __fields_ = [
        ("EraseMsg", EraseMsg),
        ("WriteMsg", WriteMsg),
        ("ReadMsg", ReadMsg)
    ]
