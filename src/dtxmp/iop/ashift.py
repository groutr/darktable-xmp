from ctypes import Structure, c_int, c_float
from enum import Enum

class ashift_params1(Structure):
    _operation = 'ashift'
    _version = 1
    _fields_ = [('rotation', c_float),
                ('lensshift_v', c_float),
                ('lensshift_h', c_float),
                ('toggle', c_int)]

class ashift_mode(Enum):
    ASHIFT_MODE_GENERIC = 0
    ASHIFT_MODE_SPECIFIC = 1

class ashift_params2(Structure):
    _operation = 'ashift'
    _version = 2
    _fields_ = [('rotation', c_float),
                ('lensshift_v', c_float),
                ('lensshift_h', c_float),
                ('f_length', c_float),
                ('cropfactor', c_float),
                ('orthocorr', c_float),
                ('aspect', c_float),
                ('mode', c_int)  # enum
                ('toggle', c_int)]

class ashift_cropmode(Enum):
    ASHIFT_CROP_OFF = 0
    ASHIFT_CROP_LARGEST = 1
    ASHIFT_CROP_ASPECT = 2

class ashift_params3(Structure):
    _operation = 'ashift'
    _version = 3
    _fields_ = [('rotation', c_float),
                ('lensshift_v', c_float),
                ('lensshift_h', c_float),
                ('f_length', c_float),
                ('crop_factor', c_float),
                ('orthocorr', c_float),
                ('aspect', c_float),
                ('mode', c_int),   # enum
                ('toggle', c_int),
                ('cropmode', c_int),  # enum
                ('cl', c_float),
                ('cr', c_float),
                ('ct', c_float),
                ('cb', c_float)]

class ashift_params4(Structure):
    _operation = 'ashift'
    _version = 4
    _fields_ = [('rotation', c_float),
            ('lensshift_v', c_float),
            ('lensshift_h', c_float),
            ('shear', c_float),
            ('f_length', c_float),
            ('crop_factor', c_float),
            ('orthocorr', c_float),
            ('aspect', c_float),
            ('mode', c_int),   # enum
            ('toggle', c_int),
            ('cropmode', c_int),  # enum
            ('cl', c_float),
            ('cr', c_float),
            ('ct', c_float),
            ('cb', c_float)]    
  
