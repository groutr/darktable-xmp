from ctypes import Structure, c_int, c_float

class rawdenoise_params(Structure):
    _operation = 'rawdenoise'
    _version = 2
    RAWDENOISE_BANDS = 5
    _fields_ = [('threshold', c_float),
                ('x', c_float * 4 * RAWDENOISE_BANDS),
                ('y', c_float * 4 * RAWDENOISE_BANDS)]
