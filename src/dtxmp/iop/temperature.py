from ctypes import Structure, c_float

class temperature_params3(Structure):
    _operation = 'temperature'
    _version = 3
    _fields_ = [('coeffs', c_float * 4)]

class temperature_params2(Structure):
    _operation = 'temperature'
    _version = 2
    _fields_ = [('temp_out', c_float), ('coeffs', c_float * 3)]


def v2_to_v3(v2):
    assert v2._version == 2
    v3 = temperature_params3()
    v3.coeffs[:-1] = v2.coeffs
    v3.coeffs[-1] = float('nan')
    return v3
