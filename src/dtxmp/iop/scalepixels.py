from ctypes import Structure, c_float

class scalepixels(Structure):
    _operation = 'scalepixels'
    _version = 1
    _fields_ = [('pixel_aspect_ratio', c_float)]
