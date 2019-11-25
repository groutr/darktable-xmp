from ctypes import Structure, c_int, c_float, c_char
from enum import Enum

class lens_target_geom(Enum):
    # From lensfun.h
    LF_UNKNOWN = 0
    LF_RECTILINEAR = 1
    LF_FISHEYE = 2
    LF_PANORAMIC = 3
    LF_EQUIRECTANGULAR = 4
    LF_FISHEYE_ORTHOGRAPHIC = 5
    LF_FISHEYE_STEREOGRAPHIC = 6
    LF_FISHEYE_EQUISOLID = 7
    LF_FISHEYE_THOBY = 8


class lens_params(Structure):
    _operation = 'lens'
    _version = 5
    _fields_ = [('modify_flags', c_int),
                ('inverse', c_int),
                ('scale', c_float),
                ('crop', c_float),
                ('focal', c_float),
                ('aperture', c_float),
                ('distance', c_float),
                ('target_geom', c_int),  # enum
                ('camera', c_char * 128),
                ('lens', c_char * 128),
                ('tca_override', c_int),
                ('tca_r', c_float),
                ('tca_b', c_float),
                ('modified', c_int)]
