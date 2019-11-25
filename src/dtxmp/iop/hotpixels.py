from ctypes import Structure, c_int, c_float

class hotpixels_params(Structure):
    _operation = 'hotpixels'
    _version = 1
    _fields_ = [('strength', c_float),
                ('threshold', c_float),
                ('markfixed', c_int), 
                ('permissive', c_int)]
