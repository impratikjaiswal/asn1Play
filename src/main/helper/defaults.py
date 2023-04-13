from src.main.helper.file_extensions import FileExtensions
from src.main.helper.formats import Formats
from src.main.helper.modes_error_handling import ErrorHandlingModes
from src.main.helper.modes_execution import ExecutionModes


class Defaults:
    RE_PARSE_OUTPUT = False
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    FORMAT_INPUT = Formats.DER
    FORMAT_OUTPUT = Formats.ASN1
    EXECUTION_MODE = ExecutionModes.USER
    ERROR_HANDLING_MODE = ErrorHandlingModes.CONTINUE_ON_ERROR
    OUTPUT_FILE_EXTENSION = FileExtensions.TXT
