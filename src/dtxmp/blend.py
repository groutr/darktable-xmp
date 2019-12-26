from ctypes import Structure, c_int, c_float, c_char
from ctypes import c_uint32
from enum import Enum

class blend_mode(Enum):
    BLEND_MASK_FLAG = 128
    BLEND_DISABLED = 0
    BLEND_NORMAL = 1 # deprecated as it did clamping
    BLEND_LIGHTEN = 2
    BLEND_DARKEN = 3
    BLEND_MULTIPLY = 4
    BLEND_AVERAGE = 5
    BLEND_ADD = 6
    BLEND_SUBSTRACT = 7
    BLEND_DIFFERENCE = 8 # deprecated
    BLEND_SCREEN = 9
    BLEND_OVERLAY = 10
    BLEND_SOFTLIGHT = 11
    BLEND_HARDLIGHT = 12
    BLEND_VIVIDLIGHT = 13
    BLEND_LINEARLIGHT = 14
    BLEND_PINLIGHT = 15
    BLEND_LIGHTNESS = 16
    BLEND_CHROMA = 17
    BLEND_HUE = 18
    BLEND_COLOR = 19
    BLEND_INVERSE = 20   # deprecated
    BLEND_UNBOUNDED = 21 #  deprecated as new normal takes over
    BLEND_COLORADJUST = 22
    BLEND_DIFFERENCE2 = 23
    BLEND_NORMAL2 = 24
    BLEND_BOUNDED = 25
    BLEND_LAB_LIGHTNESS = 26
    BLEND_LAB_COLOR = 27
    BLEND_HSV_LIGHTNESS = 28
    BLEND_HSV_COLOR = 29
    BLEND_LAB_L = 30
    BLEND_LAB_A = 31
    BLEND_LAB_B = 32
    BLEND_RGB_R = 33
    BLEND_RGB_G = 34
    BLEND_RGB_B = 35

class mask_mode(Enum):
    MASK_DISABLED = 0
    MASK_ENABLED = 1
    MASK_MASK = 1 << 1  # drawn
    MASK_CONDITIONAL = 1 << 2  # parametric
    MASK_RASTER = 1 << 3  #raster
    MASK_MASK_CONDITIONAL = MASK_MASK | MASK_CONDITIONAL

class mask_combine(Enum):
    COMBINE_NORM = 0
    COMBINE_INV = 1
    COMBINE_EXCL = 0
    COMBINE_INCL = 2
    COMBINE_MASKS_POS = 4
    COMBINE_NORM_EXCL = (COMBINE_NORM | COMBINE_EXCL)
    COMBINE_NORM_INCL = (COMBINE_NORM | COMBINE_INCL)
    COMBINE_INV_EXCL = (COMBINE_INV | COMBINE_EXCL)
    COMBINE_INV_INCL = (COMBINE_INV | COMBINE_INCL)

class mask_feathering_guide(Enum):
    MASK_GUIDE_IN = 1
    MASK_GUIDE_OUT = 2

class blendif_channels(Enum):
    BLENDIF_L_in = 0
    BLENDIF_A_in = 1
    BLENDIF_B_in = 2

    BLENDIF_L_out = 4
    BLENDIF_A_out = 5
    BLENDIF_B_out = 6

    BLENDIF_GRAY_in = 0
    BLENDIF_RED_in = 1
    BLENDIF_GREEN_in = 2
    BLENDIF_BLUE_in = 3

    BLENDIF_GRAY_out = 4
    BLENDIF_RED_out = 5
    BLENDIF_GREEN_out = 6
    BLENDIF_BLUE_out = 7

    BLENDIF_C_in = 8
    BLENDIF_h_in = 9

    BLENDIF_C_out = 12
    BLENDIF_h_out = 13

    BLENDIF_H_in = 8
    BLENDIF_S_in = 9
    BLENDIF_l_in = 10

    BLENDIF_H_out = 12
    BLENDIF_S_out = 13
    BLENDIF_l_out = 14

    BLENDIF_MAX = 14
    BLENDIF_unused = 15

    BLENDIF_active = 31

    BLENDIF_SIZE = 16

    BLENDIF_Lab_MASK = 13175
    BLENDIF_RGB_MASK = 30719

class blend_params1(Structure):
    _operation = 'blendop'
    _version = 1
    _fields_ = [('mode', c_uint32),
                ('opacity', c_float),
                ('mask_id', c_uint32)]

class blend_params2(Structure):
    _operation = 'blendop'
    _version = 2
    _fields_ = [('mode', c_uint32),
                ('opacity', c_float),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('blendif_parameters', c_float * (4 * 8))]

class blend_params3(Structure):
    _operation = 'blendop'
    _version = 3
    _fields_ = [('mode', c_uint32),
                ('opacity', c_float),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('blendif_parameters', c_float * (4 * 16))]

class blend_params4(Structure):
    _operation = 'blendop'
    _version = 4
    _fields_ = [('mode', c_uint32),
                ('opacity', c_float),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('radius', c_float),
                ('blendif_parameters', c_float * (4 * 16))]

class blend_params5(Structure):
    _operation = 'blendop'
    _version = 5
    _fields_ = [('mask_mode', c_uint32),
                ('blend_mode', c_uint32),
                ('opacity', c_float),
                ('mask_combine', c_uint32),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('radius', c_float),
                ('reserved', c_uint32 * 4),
                ('blendif_parameters', c_float * (4 * 16))]

class blend_params6(Structure):
    _operation = 'blendop'
    _version = 6
    _fields_ = [('mask_mode', c_uint32),
                ('blend_mode', c_uint32),
                ('opacity', c_float),
                ('mask_combine', c_uint32),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('radius', c_float),
                ('reserved', c_uint32 * 4),
                ('blendif_parameters', c_float * (4 * 16))]

class blend_params7(Structure):
    _operation = 'blendop'
    _version = 7
    _fields_ = [('mask_mode', c_uint32),
                ('blend_mode', c_uint32),
                ('opacity', c_float),
                ('mask_combine', c_uint32),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('radius', c_float),
                ('reserved', c_uint32 * 4),
                ('blendif_parameters', c_float * (4 * 16))]

class blend_params8(Structure):
    _operation = 'blendop'
    _version = 8
    _fields_ = [('mask_mode', c_uint32),
                ('blend_mode', c_uint32),
                ('opacity', c_float),
                ('mask_combine', c_uint32),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('feathering_radius', c_float),
                ('feathering_guide', c_uint32),
                ('blur_radius', c_float),
                ('contrast', c_float),
                ('brightness', c_float),
                ('reserved', c_uint32 * 4),
                ('blendif_parameters', c_float * (4 * 16))]

class blend_params(Structure):
    _operation = 'blendop'
    _version = 9
    _fields_ = [('mask_mode', c_uint32),
                ('blend_mode', c_uint32),
                ('opacity', c_float),
                ('mask_combine', c_uint32),
                ('mask_id', c_uint32),
                ('blendif', c_uint32),
                ('feathering_radius', c_float),
                ('feathering_guide', c_uint32),
                ('blur_radius', c_float),
                ('contrast', c_float),
                ('brightness', c_float),
                ('reserved', c_uint32 * 4),
                ('blendif_parameters', c_float * (4 * 16)),
                ('raster_mask_source', c_char * 20),
                ('raster_mask_instance', c_int),
                ('raster_mask_id', c_int),
                ('raster_mask_invert', c_int)]
