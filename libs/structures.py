import ctypes

class AddressSpecific(ctypes.Structure):
    _fields_ = [
        ("block_address", ctypes.c_uint16),
        ("page_address", ctypes.c_uint16),
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