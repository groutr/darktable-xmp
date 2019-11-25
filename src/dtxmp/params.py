import binascii
import base64
import zlib

dt_exif_decode = binascii.unhexlify
dt_exif_encode = binascii.hexlify

def dt_exif_compress(source):
    rv = zlib.compress(source)
    factor = min(len(source)//len(rv)+1, 99)
    output = bytearray(map(ord, f'gz{factor//10}{factor%10}'))
    output.extend(base64.standard_b64encode(rv))
    return bytes(output)

def dt_exif_decompress(source):
    return zlib.decompress(base64.standard_b64decode(source))

def dt_exif_from_xmp(source):
    if source.startswith(b'gz'):
        return dt_exif_decompress(source[4:])
    else:
        return dt_exif_decode(source)

def dt_exif_to_xmp(source, compress_threshold=100):
    if len(source) > compress_threshold:
        return dt_exif_compress(source)
    else:
        return dt_exif_encode(source)

def dt_exif_debug_fields(struct):
    return {k[0]: getattr(struct, k[0]) for k in struct._fields_}