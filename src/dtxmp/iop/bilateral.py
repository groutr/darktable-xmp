from ctypes import Structure, c_float

class bilateral_params(Structure):
    _operation = 'bilateral'
    _verison = 1
    _fields_ = [('sigma', c_float * 5)]
