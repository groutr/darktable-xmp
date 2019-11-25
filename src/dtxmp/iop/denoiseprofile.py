from ctypes import Structure, c_int, c_float, c_uint32
from enum import Enum

class denoiseprofile_params1(Structure):
    _operation = 'denoiseprofile'
    _version = 1
    DENOISE_PROFILE_V8_BANDS = 5
    _fields_ = [('radius', c_float),
                ('strength', c_float),
                ('a', c_float * 3),
                ('b', c_float * 3),
                ('mode', c_int),
                ('x', c_float * 4 * DENOISE_PROFILE_V8_BANDS),
                ('y', c_float * 4 * DENOISE_PROFILE_V8_BANDS)]
                
