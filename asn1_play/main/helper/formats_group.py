from python_helpers.ph_file_extensions import PhFileExtensions

from asn1_play.main.helper.formats import Formats


class FormatsGroup:
    TXT_FORMATS = [Formats.ASN1, Formats.GET_VAL, Formats.GET_VAL_PATHS]

    BASE64_FORMATS = [Formats.DER_64, Formats.BER_64]

    HEX_FORMATS = [Formats.DER, Formats.BER]

    ASCII_FORMATS = [Formats.ASCII]

    INPUT_FORMATS_HEX = [Formats.DER, Formats.DER_64, Formats.HEX, Formats.BYTE_ARRAY, Formats.BYTE_ARRAY_SIGNED]

    INPUT_FORMATS_DER = [Formats.DER, Formats.HEX]

    INPUT_FORMATS_DER_BASE_64 = [Formats.DER_64]

    INPUT_FORMATS_ASN = [Formats.ASN1]

    INPUT_FORMATS_YML = [Formats.YML]

    INPUT_FORMATS_ASCII = [Formats.ASCII]

    INPUT_FORMATS_BYTE_ARRAY = [Formats.BYTE_ARRAY, Formats.BYTE_ARRAY_SIGNED]

    INPUT_FORMATS_NON_TXT = INPUT_FORMATS_HEX + INPUT_FORMATS_ASCII

    INPUT_FORMATS = INPUT_FORMATS_HEX + INPUT_FORMATS_ASN + INPUT_FORMATS_ASCII

    INPUT_FILE_FORMATS_HEX = [PhFileExtensions.HEX]

    INPUT_FILE_FORMATS_BASE_64 = [PhFileExtensions.BASE_64]

    INPUT_FILE_FORMATS_ASN = [PhFileExtensions.ASN1, PhFileExtensions.ASN]

    INPUT_FILE_FORMATS_YML = [PhFileExtensions.YAML, PhFileExtensions.YML]

    INPUT_FILE_FORMATS = INPUT_FILE_FORMATS_HEX + INPUT_FILE_FORMATS_BASE_64 + INPUT_FILE_FORMATS_ASN + INPUT_FILE_FORMATS_YML

    # Not able to use python list comprehension
    # NameError: name 'TXT_FORMATS' is not defined
    # INPUT_FORMATS_SUPPORTED_HEX = [x for x in INPUT_FORMATS_SUPPORTED if x not in TXT_FORMATS]
    # INPUT_FORMATS_SUPPORTED_TXT = [x for x in INPUT_FORMATS_SUPPORTED if x in TXT_FORMATS]
