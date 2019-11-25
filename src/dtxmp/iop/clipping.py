from ctypes import Structure, c_float, c_int


class clipping_params(Structure):
    _operation = 'clipping'
    _version = 5
    _fields_ = [('angle', c_float),
                ('cx', c_float), ('cy', c_float), ('cw', c_float), ('ch', c_float),
                ('k_h', c_float), ('k_v', c_float), ('kxa', c_float), ('kya', c_float),
                ('kxb', c_float), ('kyb', c_float), ('kxc', c_float), ('kyc', c_float),
                ('kxd', c_float), ('kyd', c_float),
                ('k_type', c_int), ('k_sym', c_int),
                ('k_apply', c_int), ('crop_auto', c_int),
                ('ratio_n', c_int), ('ratio_d', c_int)]
