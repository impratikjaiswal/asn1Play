from python_helpers.ph_file_extensions import PhFileExtensions

from asn1_play.main.helper.formats import Formats


class FormatsGroup:
    # --------------------------------------------------------------------------#
    # internal attributes access
    # --------------------------------------------------------------------------#
    PYCRATE_INTERNAL_ATTRIBUTE_ACCESS = [
        Formats.GET_INTERNALS,
        Formats.GET_TYPEREF,
        Formats.GET_TYPEREF_LIST,
        Formats.GET_TYPE_LIST,
        Formats.GET_CONST,
        Formats.GET_PROTO,
        Formats.GET_COMPLEXITY,
        Formats.GET_ROOT,
        Formats.GET_ROOT_PATH,
        # TODO: TypeError: get_at() missing 1 required positional argument: 'path'
        # Formats.GET_AT,
    ]

    # --------------------------------------------------------------------------#
    # Pycrate; internal value access
    # --------------------------------------------------------------------------#
    PYCRATE_VALUE_ACCESS = [
        Formats.GET_VAL,
        Formats.GET_VAL_PATHS,
        Formats.GET_VAL_JER_PATHS,
    ]

    # --------------------------------------------------------------------------#
    # Pycrate; encoding / decoding,
    # --------------------------------------------------------------------------#
    PYCRATE_ENCODING_DECODING = [
        ###
        # conversion between internal value and ASN.1 syntax
        ###
        Formats.ASN1,
        ###
        # conversion between internal value and ASN.1 PER encoding
        ###
        Formats.UPER,
        Formats.UPER_WS,
        Formats.APER,
        Formats.APER_WS,
        ###
        # conversion between internal value and ASN.1 BER encoding
        ###
        Formats.BER,
        Formats.BER_WS,
        ###
        # conversion between internal value and ASN.1 CER encoding
        ###
        Formats.CER,
        Formats.CER_WS,
        ###
        # conversion between internal value and ASN.1 DER encoding
        ###
        Formats.DER,
        Formats.DER_WS,
        ###
        # conversion between internal value and ASN.1 GSER encoding
        # TODO: to_gser() missing 1 required positional argument: 'buf'
        ###
        # Formats.GSER,
        ###
        # conversion between internal value and ASN.1 JER encoding
        ###
        Formats.JER,
        Formats.JSON,
        ###
        # conversion between internal value and ASN.1 OER encoding
        ###
        Formats.OER,
        Formats.OER_WS,
        ###
        # conversion between internal value and ASN.1 COER encoding
        ###
        Formats.COER,
        Formats.COER_WS,
    ]

    # --------------------------------------------------------------------------#
    # Asn1Play; conversion,
    # --------------------------------------------------------------------------#
    ASN1PLAY_CONVERSION = [
        ###
        # conversion between internal value and Base 64 syntax
        ###
        Formats.DER_64,
        ###
        # conversion between internal value and Byte Arry syntax
        ###
        Formats.DER_BYTE_ARRAY,
        Formats.DER_BYTE_ARRAY_SIGNED,
        ###
        # conversion between internal value and HEX syntax
        ###
        Formats.HEX,
        ###
        # conversion between internal value and Ascii/Text syntax
        ###
        Formats.TXT,
        Formats.ASCII,
    ]

    # --------------------------------------------------------------------------#
    # Custom datatype, utilizing available data types
    # --------------------------------------------------------------------------#

    BASE64_FORMATS = [Formats.DER_64]

    HEX_FORMATS = [Formats.DER, Formats.BER]

    ASCII_FORMATS = [Formats.ASCII, Formats.TXT]

    BYTE_ARRAY_FORMATS = [Formats.DER_BYTE_ARRAY, Formats.DER_BYTE_ARRAY_SIGNED]

    INPUT_FORMATS_HEX = [Formats.DER, Formats.DER_64, Formats.HEX] + BYTE_ARRAY_FORMATS

    INPUT_FORMATS_DER = [Formats.DER, Formats.HEX]

    INPUT_FORMATS_ASN = [Formats.ASN1]

    INPUT_FORMATS_JSON = [Formats.JSON, Formats.JER]

    INPUT_FORMATS_YML = [Formats.YML]

    INPUT_FORMATS_ASCII = [Formats.ASCII, Formats.TXT]

    TXT_FORMATS = INPUT_FORMATS_ASN + INPUT_FORMATS_JSON + [Formats.GET_VAL, Formats.GET_VAL_PATHS]

    NON_TXT_FORMATS = INPUT_FORMATS_HEX + INPUT_FORMATS_ASCII

    INPUT_FILE_FORMATS_HEX = [PhFileExtensions.HEX]

    INPUT_FILE_FORMATS_BASE_64 = [PhFileExtensions.BASE_64]

    INPUT_FILE_FORMATS_ASN = [PhFileExtensions.ASN1, PhFileExtensions.ASN]

    INPUT_FILE_FORMATS_YML = [PhFileExtensions.YAML, PhFileExtensions.YML]

    INPUT_FILE_FORMATS = INPUT_FILE_FORMATS_HEX + INPUT_FILE_FORMATS_BASE_64 + INPUT_FILE_FORMATS_ASN + INPUT_FILE_FORMATS_YML

    # Not able to use python list comprehension
    # NameError: name 'TXT_FORMATS' is not defined
    # INPUT_FORMATS_SUPPORTED_HEX = [x for x in INPUT_FORMATS_SUPPORTED if x not in TXT_FORMATS]
    # INPUT_FORMATS_SUPPORTED_TXT = [x for x in INPUT_FORMATS_SUPPORTED if x in TXT_FORMATS]

    # TODO: https://pratikj.atlassian.net/browse/SML-447
    # INPUT_FORMATS_SUPPORTED = PYCRATE_ENCODING_DECODING + ASN1PLAY_CONVERSION
    INPUT_FORMATS_SUPPORTED = INPUT_FORMATS_HEX + INPUT_FORMATS_ASN + INPUT_FORMATS_ASCII + INPUT_FORMATS_JSON

    OUTPUT_FORMATS_SUPPORTED = PYCRATE_INTERNAL_ATTRIBUTE_ACCESS + PYCRATE_VALUE_ACCESS + PYCRATE_ENCODING_DECODING + ASN1PLAY_CONVERSION
