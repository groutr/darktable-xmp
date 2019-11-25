from ctypes import Structure, c_int, c_float
from enum import Enum

class highlights_mode(Enum):
    DT_IOP_HIGHLIGHTS_CLIP = 0
    DT_IOP_HIGHLIGHTS_LCH = 1
    DT_IOP_HIGHLIGHTS_INPAINT = 2
    
class highlights_params(Structure):
    _operation = 'highlights'
    _version = 2
    _fields_ = [('mode', c_int),
                ('blendL', c_float),
                ('blendC', c_float),
                ('blendh', c_float),
                ('clip', c_float)]
    
