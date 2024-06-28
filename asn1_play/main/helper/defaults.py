from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

# from asn1_play.generated_code.asn1.GSMA.SGP_22 import CompileTimeVersion as sgp_22_version
from asn1_play.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from asn1_play.generated_code.asn1.GSMA.SGP_32 import version as sgp_32_version
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    QUITE_MODE = False
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    RE_PARSE_OUTPUT = False
    FORMAT_INPUT = Formats.DER
    FORMAT_OUTPUT = Formats.ASN1
    OUTPUT_FILE_EXTENSION = PhFileExtensions.TXT
    ASN1_SCHEMA = Asn1Versions.GSMA_SGP_22_v3_1
    # TODO: Circular Import
    # ASN1_SCHEMA_COMPILE_TIME_GSMA_SGP_22 = sgp_22_version.v3_1
    ASN1_SCHEMA_COMPILE_TIME_GSMA_SGP_22 = sgp_22_version
    ASN1_SCHEMA_COMPILE_TIME_TCA_EPP = epp_version
    ASN1_SCHEMA_COMPILE_TIME_GSMA_SGP_32 = sgp_32_version
    ASN1_OBJECT = 'StoreMetadataRequest'
