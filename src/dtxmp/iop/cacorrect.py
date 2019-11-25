from ctypes import Structure, c_int

class cacorrect_params(Structure):
    _operation = 'cacorrect'
    _version = 1
    _fields_ = [('keep', c_int)]
