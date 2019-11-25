from ctypes import Structure, Union, c_int32, c_uint16
from enum import Enum


class rawprepare_params(Structure):
    _operation = 'rawprepare'
    _version = 1
    class crop(Union):
        class named(Structure):
            _fields_ = [('x', c_int32),
                        ('y', c_int32),
                        ('width', c_int32),
                        ('height', c_int32)]
        _fields_ = [('array', c_int32 * 4)]
    _fields_ = [('raw_black_level_separate', c_uint16 * 4),
                ('raw_white_point', c_uint16)]
