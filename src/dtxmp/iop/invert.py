from ctypes import Structure, c_int, c_float
from enum import Enum

class invert_params2(Structure):
    _operation = 'invert'
    _version = 2
    _fields_ = [('color', c_float * 4)]

class invert_params1(Structure):
    _operation = 'invert'
    _version = 1
    _fields_ = [('color', c_float * 3)]


def v1_to_v2(v1):
    assert v1._version == 1
    v2 = invert_params2([*v1.color])
    v2.color[3] = float('nan')
    return v2
