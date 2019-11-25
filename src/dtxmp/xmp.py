from lxml import etree as ET

from .params import dt_exif_to_xmp

ns = {'darktable': 'http://darktable.sf.net/',
     'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}

def qnamify(tag):
    npart, lpart = tag.split(':')
    return ET.QName(ns[npart], lpart)

parse_document = ET.parse
tostring = ET.tostring

def get_dt_history(document):
    dt_desc = next(document.iterfind('./rdf:RDF/rdf:Description', namespaces=ns))
    dt_history = next(dt_desc.iterfind('./darktable:history', namespaces=ns))
    dt_history_seq = dt_history[0]
    return dt_history_seq

def append_history_element(document, element):
    dt_desc = next(document.iterfind('./rdf:RDF/rdf:Description', namespaces=ns))
    dt_history = next(dt_desc.iterfind('./darktable:history', namespaces=ns))
    dt_history_seq = dt_history[0]
    element.attrib[qnamify('darktable:num')] = hist_end = str(len(dt_history_seq))
    dt_history_seq.append(element)
    # update the history_end attribute
    dt_desc.attrib[qnamify('darktable:history_end')] = hist_end
    return document

def define_history_list(document, history):
    """Replace the history with a given history list"""

    dt_desc = next(document.iterfind('./rdf:RDF/rdf:Description', namespaces=ns))
    dt_history = next(dt_desc.iterfind('./darktable:history', namespaces=ns))
    dt_history_seq = dt_history[0]
    dt_history_seq.clear()
    for i, h in enumerate(history):
        h.attrib[qnamify('darktable:num')] = str(i)
        dt_history_seq.append(h)
    dt_desc.attrib[qnamify('darktable:history_end')] = str(len(history))
    return document


def make_iop(params=None, struct=None):
    if params is None:
        params = {}

    # We use default blendop
    params['blendop_version'] = 9
    params['blendop_params'] = b"gz11eJxjYGBgkGAAgRNODGiAEV0AJ2iwh+CRyscOAAdeGQQ="

    params['multi_name'] = ""
    params['multi_priority'] = 0

    if struct is not None:
        # Pull elements from struct
        params['params'] = dt_exif_to_xmp(bytes(struct))
        params['modversion'] = struct._version
        params['operation'] = struct._operation
        params['enabled'] = 1

    # assert elements
    assert 'operation' in params
    assert 'enabled' in params
    assert 'params' in params

    params = {}
    for k, v in params.items():
        if not isinstance(v, (str, bytes)):
            params[qnamify(f'darktable:{k}')] = str(v)
        else:
            params[qnamify(f'darktable:{k}')] = v
    li = ET.Element(qnamify('rdf:li'), params)
    return li
