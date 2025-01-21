from python_helpers.ph_defaults import PhDefaults, PhDefaultTypesInclude, PhDefaultTypesExclude
from python_helpers.ph_file_extensions import PhFileExtensions

from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.helper.formats import Formats


class Defaults:
    #############
    # Generic Objects
    #############
    EXECUTION_MODE = PhDefaults.EXECUTION_MODE
    ERROR_HANDLING_MODE = PhDefaults.ERROR_HANDLING_MODE
    OUTPUT_FILE_EXT = PhFileExtensions.TXT
    #############
    # Data Objects
    #############
    # Common Objects
    # INPUT_DATA
    PRINT_INPUT = PhDefaults.PRINT_INPUT
    PRINT_OUTPUT = PhDefaults.PRINT_OUTPUT
    PRINT_INFO = PhDefaults.PRINT_INFO
    QUITE_MODE = PhDefaults.QUITE_MODE
    # REMARKS
    ENCODING = PhDefaults.CHAR_ENCODING
    ENCODING_ERRORS = PhDefaults.ENCODING_ERRORS
    OUTPUT_PATH = PhDefaults.OUTPUT_PATH
    OUTPUT_FILE_NAME_KEYWORD = PhDefaults.OUTPUT_FILE_NAME_KEYWORD
    ARCHIVE_OUTPUT = PhDefaults.ARCHIVE_OUTPUT
    ARCHIVE_OUTPUT_FORMAT = PhDefaults.ARCHIVE_OUTPUT_FORMAT
    # Specific Objects
    INPUT_FORMAT = Formats.DER
    OUTPUT_FORMAT = Formats.ASN1
    # ASN1_ELEMENT
    TLV_PARSING_OF_OUTPUT = False
    RE_PARSE_OUTPUT = False
    # ASN1_ELEMENT Sub Object
    ASN1_SCHEMA = Asn1Versions.GSMA_SGP_22_v3_1
    ASN1_OBJECT = 'StoreMetadataRequest'
    ASN1_OBJECT_ALTERNATE = ''
    FETCH_ASN1_OBJECTS_LIST = False


class DefaultTypesInclude:
    # Common Objects
    # INPUT_DATA
    PRINT_INPUT = PhDefaultTypesInclude.PRINT_INPUT
    PRINT_OUTPUT = PhDefaultTypesInclude.PRINT_OUTPUT
    PRINT_INFO = PhDefaultTypesInclude.PRINT_INFO
    QUITE_MODE = PhDefaultTypesInclude.QUITE_MODE
    # REMARKS
    ENCODING = PhDefaultTypesInclude.ENCODING
    ENCODING_ERRORS = PhDefaultTypesInclude.ENCODING_ERRORS
    OUTPUT_PATH = PhDefaultTypesInclude.OUTPUT_PATH
    ARCHIVE_OUTPUT = PhDefaultTypesInclude.ARCHIVE_OUTPUT
    ARCHIVE_OUTPUT_FORMAT = PhDefaultTypesInclude.ARCHIVE_OUTPUT_FORMAT
    # Specific Objects
    INPUT_FORMAT = str
    OUTPUT_FORMAT = str
    # ASN1_ELEMENT
    TLV_PARSING_OF_OUTPUT = bool
    RE_PARSE_OUTPUT = bool
    # ASN1_ELEMENT Sub Object
    ASN1_OBJECT_ALTERNATE = str
    FETCH_ASN1_OBJECTS_LIST = bool


class DefaultTypesExclude:
    # Common Objects
    INPUT_DATA: PhDefaultTypesExclude.INPUT_DATA
