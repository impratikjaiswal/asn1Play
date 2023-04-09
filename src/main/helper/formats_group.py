from src.main.helper.file_extensions import FileExtensions
from src.main.helper.formats import Formats


class FormatsGroup:
    TXT_FORMATS = [Formats.ASN1, Formats.GET_VAL, Formats.GET_VAL_PATHS]

    BASE64_FORMATS = [Formats.DER_64, Formats.BER_64]

    HEX_FORMATS = [Formats.DER, Formats.BER]

    ASCII_FORMATS = [Formats.ASCII]

    INPUT_FORMATS_HEX = [Formats.DER, Formats.DER_64, Formats.HEX]

    INPUT_FORMATS_DER = [Formats.DER, Formats.HEX]

    INPUT_FORMATS_DER_BASE_64 = [Formats.DER_64]

    INPUT_FORMATS_ASN = [Formats.ASN1]

    INPUT_FORMATS_YML = [Formats.YML]

    INPUT_FORMATS_ASCII = [Formats.ASCII]

    INPUT_FORMATS_NON_TXT = INPUT_FORMATS_HEX + INPUT_FORMATS_ASCII

    INPUT_FORMATS = INPUT_FORMATS_HEX + INPUT_FORMATS_ASN + INPUT_FORMATS_ASCII

    INPUT_FILE_FORMATS_HEX = [FileExtensions.HEX]

    INPUT_FILE_FORMATS_BASE_64 = [FileExtensions.BASE_64]

    INPUT_FILE_FORMATS_ASN = [FileExtensions.ASN1, FileExtensions.ASN]

    INPUT_FILE_FORMATS_YML = [FileExtensions.YAML, FileExtensions.YML]

    INPUT_FILE_FORMATS = INPUT_FILE_FORMATS_HEX + INPUT_FILE_FORMATS_BASE_64 + INPUT_FILE_FORMATS_ASN + INPUT_FILE_FORMATS_YML

    # Not able to use python list comprehension
    # NameError: name 'TXT_FORMATS' is not defined
    # INPUT_FORMATS_SUPPORTED_HEX = [x for x in INPUT_FORMATS_SUPPORTED if x not in TXT_FORMATS]
    # INPUT_FORMATS_SUPPORTED_TXT = [x for x in INPUT_FORMATS_SUPPORTED if x in TXT_FORMATS]