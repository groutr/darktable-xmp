from ctypes import Structure, c_float

class velvia_params2(Structure):
    _operation = 'velvia'
    _version = 2
    _fields_ = [('strength', c_float),
                ('bias', c_float)]

class velvia_params1(Structure):
    _operation = 'velvia'
    _version = 1
    _fields_ = [('saturation', c_float),
                ('vibrance', c_float),
                ('luminance', c_float),
                ('clarity', c_float)]
