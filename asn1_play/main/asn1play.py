from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_util import PhUtil
from tlv_play.main.helper.constants_config import ConfigConst as tlvConfigConst

from asn1_play.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from asn1_play.main.data_type.any_data import AnyData
from asn1_play.main.data_type.any_data_bulk import AnyDataBulk
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.data_type.dev import Dev
from asn1_play.main.data_type.profile_element import ProfileElement
from asn1_play.main.data_type.store_metadata_request import StoreMetaData
from asn1_play.main.data_type.store_metadata_request_bulk import StoreMetaDataBulk
from asn1_play.main.data_type.unit_testing import UnitTesting
from asn1_play.main.data_type.update_metadata_request import UpdateMetadataRequest
from asn1_play.main.data_type.user_data import UserData
from asn1_play.main.helper.constants_config import ConfigConst
from asn1_play.main.helper.defaults import Defaults


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
        #####
        # Sample With Plenty vivid Examples, Bulk
        #####
        AnyDataBulk(),
    ]
    data_types_sample_specific = [
        #####
        # Sample Store Meta Data Request; Bulk Mode
        #####
        StoreMetaDataBulk(),
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
        PhExecutionModes.USER: data_type_user,
        PhExecutionModes.DEV: data_type_dev,
        PhExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        PhExecutionModes.SAMPLE_SPECIFIC: data_types_sample_specific,
        PhExecutionModes.UNIT_TESTING: data_type_unit_testing,
        PhExecutionModes.ALL: data_types_sample_generic + data_types_sample_specific + data_type_unit_testing + data_type_user,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    for data_type in data_types:
        PhUtil.print_heading(str_heading=str(data_type.__class__.__name__))
        data_type.set_print_input()
        data_type.set_print_output()
        data_type.set_print_info()
        data_type.set_output_file()
        data_type.set_remarks_list()
        data_type.set_re_parse_output()
        data_type.set_output_file_name_keyword()
        data_type.set_output_format()
        data_type.set_input_format()
        data_type.set_asn1_element()
        data_type.set_data_pool()
        if isinstance(data_type, UnitTesting):
            error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
        if isinstance(data_type, Dev):
            error_handling_mode = PhErrorHandlingModes.STOP_ON_ERROR
        DataTypeMaster.parse_safe(data_type, error_handling_mode)


def main():
    """

    :return:
    """
    """
    Set Execution Mode, If you are a first time user then try #ExecutionModes.SAMPLE_GENERIC
    """
    execution_mode = PhExecutionModes.USER
    error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
    # Print Versions
    PhUtil.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)
    PhUtil.print_version(tlvConfigConst.TOOL_NAME, tlvConfigConst.TOOL_VERSION, no_additional_info=True)
    """
    Set Target Version of SGP22, eUICC Profile Package 
    """
    PhUtil.print_version(PhKeys.SGP22, sgp_22_version, no_additional_info=True)
    PhUtil.print_version(PhKeys.EUICC_PROFILE_PACKAGE, epp_version, no_additional_info=True)
    # Process Data
    process_data(execution_mode, error_handling_mode)
    PhUtil.print_done()


if __name__ == '__main__':
    main()
