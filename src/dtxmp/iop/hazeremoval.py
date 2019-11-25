from ctypes import Structure, c_float

class hazeremoval_params(Structure):
    _operation = 'hazeremoval'
    _version = 1
    _fields_ = [('strength', c_float),
                ('distance', c_float)]
