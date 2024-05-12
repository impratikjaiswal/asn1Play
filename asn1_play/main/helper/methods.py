from asn1_play.main.helper.formats import Formats


class Methods:
    INDEX_FROM = 0
    INDEX_TO = 1

    # --------------------------------------------------------------------------#
    # internal attributes access
    # --------------------------------------------------------------------------#
    PYCRATE_INTERNAL_ATTRIBUTE_ACCESS = {
        Formats.GET_INTERNALS: 'get_internals',
        Formats.GET_TYPEREF: 'get_typeref',
        Formats.GET_TYPEREF_LIST: 'get_typeref_list',
        Formats.GET_TYPE_LIST: 'get_type_list',
        Formats.GET_CONST: 'get_const',
        Formats.GET_PROTO: 'get_proto',
        Formats.GET_COMPLEXITY: 'get_complexity',
        Formats.GET_ROOT: 'get_root',
        Formats.GET_ROOT_PATH: 'get_root_path',
        Formats.GET_AT: 'get_at',
    }

    # --------------------------------------------------------------------------#
    # Pycrate; internal value access
    # --------------------------------------------------------------------------#
    PYCRATE_VALUE_ACCESS = {
        Formats.GET_VAL: 'get_val',
        Formats.GET_VAL_PATHS: 'get_val_paths',
        Formats.GET_VAL_JER_PATHS: 'get_val_jer_paths',
    }

    # --------------------------------------------------------------------------#
    # Pycrate; encoding / decoding,
    # --------------------------------------------------------------------------#
    PYCRATE_ENCODING_DECODING = {
        ###
        # conversion between internal value and ASN.1 syntax
        ###
        Formats.ASN1: ('from_asn1', 'to_asn1'),
        ###
        # conversion between internal value and ASN.1 PER encoding
        ###
        Formats.UPER: ('from_uper', 'to_uper'),
        Formats.UPER_WS: ('from_uper_ws', 'to_uper_ws'),
        Formats.APER: ('from_aper', 'to_aper'),
        Formats.APER_WS: ('from_aper_ws', 'to_aper_ws'),
        ###
        # conversion between internal value and ASN.1 BER encoding
        ###
        Formats.BER: ('from_ber', 'to_ber'),
        Formats.BER_WS: ('from_ber_ws', 'to_ber_ws'),
        ###
        # conversion between internal value and ASN.1 CER encoding
        ###
        Formats.CER: ('from_cer', 'to_cer'),
        Formats.CER_WS: ('from_cer_ws', 'to_cer_ws'),
        ###
        # conversion between internal value and ASN.1 DER encoding
        ###
        Formats.DER: ('from_der', 'to_der'),
        Formats.DER_WS: ('from_der_ws', 'to_der_ws'),
        ###
        # conversion between internal value and ASN.1 GSER encoding
        ###
        Formats.GSER: ('from_gser', 'to_gser'),
        ###
        # conversion between internal value and ASN.1 JER encoding
        ###
        Formats.JER: ('from_jer', 'to_jer'),
        Formats.JSON: ('from_json', 'to_json'),
        ###
        # conversion between internal value and ASN.1 OER encoding
        ###
        Formats.OER: ('from_oer', 'to_oer'),
        Formats.OER_WS: ('from_oer_ws', 'to_oer_ws'),
        ###
        # conversion between internal value and ASN.1 COER encoding
        ###
        Formats.COER: ('from_coer', 'to_coer'),
        Formats.COER_WS: ('from_coer_ws', 'to_coer_ws'),
    }

    # --------------------------------------------------------------------------#
    # Asn1Play; conversion,
    # --------------------------------------------------------------------------#
    ASN1PLAY_CONVERSION = {
        ###
        # conversion between internal value and Base 64 syntax
        ###
        Formats.DER_64: PYCRATE_ENCODING_DECODING.get(Formats.DER),
        ###
        # conversion between internal value and Byte Arry syntax
        ###
        Formats.DER_BYTE_ARRAY: PYCRATE_ENCODING_DECODING.get(Formats.DER),
        Formats.DER_BYTE_ARRAY_SIGNED: PYCRATE_ENCODING_DECODING.get(Formats.DER),
        ###
        # conversion between internal value and HEX syntax
        ###
        Formats.HEX: PYCRATE_ENCODING_DECODING.get(Formats.DER),
        ###
        # conversion between internal value and Ascii/Text syntax
        ###
        Formats.TXT: PYCRATE_ENCODING_DECODING.get(Formats.DER),
        Formats.ASCII: PYCRATE_ENCODING_DECODING.get(Formats.DER),
    }

    # --------------------------------------------------------------------------#
    # Custom datatype, utilizing available data types
    # --------------------------------------------------------------------------#
    ALL_MAPPING = {
        **PYCRATE_INTERNAL_ATTRIBUTE_ACCESS,
        **PYCRATE_VALUE_ACCESS,
        **PYCRATE_ENCODING_DECODING,
        **ASN1PLAY_CONVERSION,
    }
