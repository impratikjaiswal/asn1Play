from python_helpers.ph_util import PhUtil

from src.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.data_type.any_data import AnyData
from src.main.data_type.dev import Dev
from src.main.data_type.profile_element import ProfileElement
from src.main.data_type.store_metadata_request import StoreMetaData
from src.main.data_type.unit_testing import UnitTesting
from src.main.data_type.update_metadata_request import UpdateMetadataRequest
from src.main.data_type.user_data import UserData
from src.main.helper.constants_config import ConfigConst
from src.main.helper.convert_data import ConvertData
from src.main.helper.defaults import Defaults
from src.main.helper.keys import Keys
from src.main.helper.modes_error_handling import ErrorHandlingModes
from src.main.helper.modes_execution import ExecutionModes


def process_data(execution_mode, error_handling_mode):
    """

    :param error_handling_mode:
    :param execution_mode:
    :return:
    """
    data_type_user = [
        #####
        # Empty class for user usage
        ####
        UserData(),
    ]
    data_type_dev = [
        #####
        # class for dev
        #####
        Dev(),
    ]
    data_types_sample_generic = [
        #####
        # Sample With Plenty vivid Examples
        #####
        AnyData(),
    ]
    data_types_sample_specific = [
        #####
        # Sample Store Meta Data Request
        #####
        StoreMetaData(),
        #####
        # Sample Update Meta Data Request
        #####
        UpdateMetadataRequest(),
        #####
        # Sample Profile Elements
        #####
        ProfileElement(),
    ]
    data_type_unit_testing = [
        #####
        # Unit Testing
        #####
        UnitTesting(),
    ]
    data_types_pool = {
        ExecutionModes.USER: data_type_user,
        ExecutionModes.DEV: data_type_dev,
        ExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        ExecutionModes.SAMPLE_SPECIFIC: data_types_sample_specific,
        ExecutionModes.UNIT_TESTING: data_type_unit_testing,
        ExecutionModes.ALL: data_types_sample_generic + data_types_sample_specific + data_type_unit_testing,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    for data_type in data_types:
        PhUtil.print_heading(str_heading=str(data_type.__class__.__name__))
        data_type.set_print_input()
        data_type.set_print_output()
        data_type.set_print_info()
        data_type.set_re_parse_output()
        data_type.set_output_file()
        data_type.set_output_file_name_keyword()
        data_type.set_remarks_list()
        data_type.set_output_format()
        data_type.set_input_format()
        data_type.set_asn1_element()
        data_type.set_data_pool()
        ConvertData.parse(data_type, ErrorHandlingModes.CONTINUE_ON_ERROR if isinstance(data_type,
                                                                                        UnitTesting) else error_handling_mode)


def main():
    """

    :return:
    """
    """
    Set Execution Mode, If you are a first time user then try #ExecutionModes.SAMPLE_GENERIC
    """
    execution_mode = ExecutionModes.ALL
    error_handling_mode = ErrorHandlingModes.CONTINUE_ON_ERROR
    # Print Versions
    PhUtil.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION, with_libs=True, with_user_info=True)
    """
    Set Target Version of SGP22, eUICC Profile Package 
    """
    PhUtil.print_version(Keys.SGP22, sgp_22_version)
    PhUtil.print_version(Keys.EUICC_PROFILE_PACKAGE, epp_version)
    # Process Data
    process_data(execution_mode, error_handling_mode)
    PhUtil.print_done()


if __name__ == '__main__':
    main()
