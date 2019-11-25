from ctypes import Structure, c_int, c_float, c_uint32
from enum import Enum

class demosaic_method(Enum):
    DEMOSAIC_XTRANS = 1024
    DT_IOP_DEMOSAIC_PPG = 0
    DT_IOP_DEMOSAIC_AMAZE = 1
    DT_IOP_DEMOSAIC_VNG4 = 2
    DT_IOP_DEMOSAIC_PASSTHROUGH_MONOCRHOME = 3
    DT_IOP_DEMOSAIC_VNG = DEMOSAIC_XTRANS | 0
    DT_IOP_DEMOSAIC_MARKESTEIJN = DEMOSAIC_XTRANS | 1
    DT_IOP_DEMOSAIC_MARKESTEIJN_3 = DEMOSAIC_XTRANS | 2
    DT_IOP_DEMOSAIC_FDC = DEMOSAIC_XTRANS | 4
    
class demosaic_greeneq(Enum):
    DT_IOP_GREEN_EQ_NO = 0
    DT_IOP_GREEN_EQ_LOCAL = 1
    DT_IOP_GREEN_EQ_FULL = 2
    DT_IOP_GREEN_EQ_BOTH = 3
    
class demosaic_params(Structure):
    _operation = 'demosaic'
    _version = 3
    _fields_ = [('green_eq', c_int),
                ('median_thrs', c_float),
                ('color_smoothing', c_uint32),
                ('demosaicing_method', c_int),
                ('yet_unused_data_specific_to_demosaicing_method', c_uint32)]
    
