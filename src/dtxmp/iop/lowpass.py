from ctypes import Structure, c_int, c_float

class lowpass_params(Structure):
    _operation = 'lowpass'
    _version = 1
    _fields_ = [('order', c_int),
                ('radius', c_float),
                ('contrast', c_float),
                ('brightness', c_float),
                ('saturation', c_float),
                ('lowpass_algo', c_int),
                ('unbound', c_int)]
