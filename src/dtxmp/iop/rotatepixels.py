from ctypes import Structure, c_float, c_uint32

class rotatepixels_params(Structure):
    _operation = 'rotatepixels'
    _version = 1
    _fields_ = [('rx', c_uint32),
                ('ry', c_uint32),
                ('angle', c_float)]
