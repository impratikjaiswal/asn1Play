from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    RE_PARSE_OUTPUT = False
    FORMAT_INPUT = Formats.DER
    FORMAT_OUTPUT = Formats.ASN1
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    OUTPUT_FILE_EXTENSION = PhFileExtensions.TXT
    ASN1_SCHEMA = Asn1Versions.GSMA_SGP_22_v3_0_0
    ASN1_OBJECT = 'StoreMetadataRequest'
