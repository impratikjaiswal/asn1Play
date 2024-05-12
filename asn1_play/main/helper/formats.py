class Formats:
    # --------------------------------------------------------------------------#
    # internal attributes access
    # --------------------------------------------------------------------------#
    GET_INTERNALS = 'get_internals'
    GET_TYPEREF = 'get_typeref'
    GET_TYPEREF_LIST = 'get_typeref_list'
    GET_TYPE_LIST = 'get_type_list'
    GET_CONST = 'get_const'
    GET_PROTO = 'get_proto'
    GET_COMPLEXITY = 'get_complexity'
    GET_ROOT = 'get_root'
    GET_ROOT_PATH = 'get_root_path'
    GET_AT = 'get_at'

    # --------------------------------------------------------------------------#
    # Pycrate; internal value access
    # --------------------------------------------------------------------------#
    GET_VAL = 'get_val'
    GET_VAL_PATHS = 'get_val_paths'
    GET_VAL_JER_PATHS = 'get_val_jet_paths'

    # --------------------------------------------------------------------------#
    # Pycrate; encoding / decoding,
    # --------------------------------------------------------------------------#
    ###
    # conversion between internal value and ASN.1 syntax
    ###
    ASN1 = 'asn1'
    ###
    # conversion between internal value and ASN.1 PER encoding
    ###
    UPER = 'uper'
    UPER_WS = 'uper_ws'
    APER = 'aper'
    APER_WS = 'aper_ws'
    ###
    # conversion between internal value and ASN.1 BER encoding
    ###
    BER = 'ber'
    BER_WS = 'ber_ws'
    ###
    # conversion between internal value and ASN.1 CER encoding
    ###
    CER = 'cer'
    CER_WS = 'cer_ws'
    ###
    # conversion between internal value and ASN.1 DER encoding
    ###
    DER = 'der'
    DER_WS = 'der_ws'
    ###
    # conversion between internal value and ASN.1 GSER encoding
    ###
    GSER = 'gser'
    ###
    # conversion between internal value and ASN.1 JER encoding
    ###
    JER = 'jer'
    JSON = 'json'
    ###
    # conversion between internal value and ASN.1 OER encoding
    ###
    OER = 'oer'
    OER_WS = 'oer_ws'
    ###
    # conversion between internal value and ASN.1 COER encoding
    ###
    COER = 'coer'
    COER_WS = 'coer_ws'

    # --------------------------------------------------------------------------#
    # Asn1Play; conversion,
    # --------------------------------------------------------------------------#
    ###
    # conversion between internal value and Base 64 syntax
    ###
    DER_64 = 'der_as_base64'
    ###
    # conversion between internal value and Byte Array syntax
    ###
    DER_BYTE_ARRAY = 'der_as_byte_array'
    DER_BYTE_ARRAY_SIGNED = 'der_as_byte_array_signed'
    ###
    # conversion between internal value and HEX syntax
    ###
    HEX = 'hex'
    ###
    # conversion between internal value and Ascii/Text syntax
    ###
    TXT = 'txt'
    ASCII = 'ascii'

    # --------------------------------------------------------------------------#
    # Asn1Play; YML
    # --------------------------------------------------------------------------#
    ###
    # conversion between internal value and Yml syntax
    ###
    YML = 'yml'

    # --------------------------------------------------------------------------#
    # Custom datatype, utilizing available data types
    # --------------------------------------------------------------------------#
