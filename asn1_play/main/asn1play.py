import sys
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_modules import PhModules
from python_helpers.ph_time import PhTime
from python_helpers.ph_util import PhUtil
from tlv_play.main.helper.constants_config import ConfigConst as tlvConfigConst

from asn1_play.generated_code.asn1.GSMA.SGP_22.compile_time_version import version as sgp_22_compile
from asn1_play.generated_code.asn1.GSMA.SGP_32.compile_time_version import version as sgp_32_compile
from asn1_play.generated_code.asn1.TCA.eUICC_Profile_Package.compile_time_version import version as epp_compile
from asn1_play.main.convert.converter import handle_web_request
from asn1_play.main.data_type.any_data import AnyData
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.data_type.dev import Dev
from asn1_play.main.data_type.known_issues import KnownIssues
from asn1_play.main.data_type.profile_element import ProfileElement
from asn1_play.main.data_type.sample import Sample
from asn1_play.main.data_type.store_metadata_request import StoreMetaData
from asn1_play.main.data_type.store_metadata_request_bulk import StoreMetaDataBulk
from asn1_play.main.data_type.unit_testing import UnitTesting
from asn1_play.main.data_type.update_metadata_request import UpdateMetadataRequest
from asn1_play.main.data_type.user_data import UserData
from asn1_play.main.helper.constants_config import ConfigConst
from asn1_play.main.helper.defaults import Defaults
from asn1_play.test.test import Test

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

"""
Global Variables
"""
data_cli = None
execution_mode = None
error_handling_mode = None
sgp_22_version = None
sgp_32_version = None
epp_version = None


def process_data():
    """

    :return:
    """
    global execution_mode, error_handling_mode, data_cli
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
    data_type_known_issues = [
        #####
        # class for known issues
        #####
        KnownIssues(),
    ]
    data_types_sample_generic = [
        #####
        # Sample With Plenty vivid Examples; Single as well as Bulk
        #####
        AnyData(),
    ]
    data_types_samples = [
        #####
        # Sample With Plenty vivid Examples; Single as well as Bulk
        #####
        Sample(),
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
    data_type_unit_testing_external = [
        #####
        # Unit Testing External
        #####
        Test(),
    ]

    data_types_pool = {
        PhExecutionModes.USER: data_type_user,
        PhExecutionModes.SAMPLES_LIST: data_types_samples,
        PhExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        PhExecutionModes.SAMPLE_SPECIFIC: data_types_sample_specific,
        PhExecutionModes.UNIT_TESTING: data_type_unit_testing,
        PhExecutionModes.UNIT_TESTING_EXTERNAL: data_type_unit_testing_external,
        PhExecutionModes.DEV: data_type_dev,
        PhExecutionModes.KNOWN_ISSUES: data_type_known_issues,
        PhExecutionModes.ALL: data_type_user
                              + data_types_samples
                              + data_types_sample_generic
                              + data_types_sample_specific
                              + data_type_unit_testing
                              + data_type_unit_testing_external
        # + data_type_dev
        # + data_type_known_issues
        ,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    if data_cli:
        _data_type = DataTypeMaster()
        _data_type.set_data_pool(data_pool=[data_cli])
        data_types = [_data_type]
    for data_type in data_types:
        PhUtil.print_heading(str_heading=f'Data Class: {str(data_type.__class__.__name__)}')
        # if isinstance(data_type, UnitTesting):
        #     error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
        # if isinstance(data_type, Dev):
        #     error_handling_mode = PhErrorHandlingModes.STOP_ON_ERROR
        if isinstance(data_type, Test):
            Test.test_all()
            continue
        if isinstance(data_type, Sample):
            # Validate & Print Sample Data For Web
            PhUtil.print_iter(Sample().get_sample_data_pool_for_web(), header='Sample Data')
        if not data_cli:
            data_type.set_print_input()
            data_type.set_print_output()
            data_type.set_print_info()
            data_type.set_quiet_mode()
            data_type.set_remarks()
            data_type.set_encoding()
            data_type.set_encoding_errors()
            data_type.set_output_path()
            data_type.set_output_file_name_keyword()
            data_type.set_archive_output()
            data_type.set_archive_output_format()
            #
            data_type.set_input_format()
            data_type.set_output_format()
            data_type.set_asn1_element()
            data_type.set_tlv_parsing_of_output()
            data_type.set_re_parse_output()
            #
            data_type.set_data_pool()
        DataTypeMaster.process_safe(data_type, error_handling_mode)


def handle_cli_request(**kwargs):
    """

    :param kwargs:
    :return:
    """
    global data_cli
    data_cli = handle_web_request(kwargs)


def print_configurations():
    # Print Versions
    version_parameters_pool = [
        {'tool_name': ConfigConst.TOOL_NAME, 'tool_version': ConfigConst.TOOL_VERSION},
        # TODO: Fetch & Store this version; Use Stored version throughout as this is not gonna be changed
        {'tool_name': PhModules.PYCRATE, 'fetch_tool_version': True},
        {'tool_name': tlvConfigConst.TOOL_NAME, 'tool_version': tlvConfigConst.TOOL_VERSION},
        {'tool_name': ' '.join([PhKeys.SGP22, PhKeys.COMPILE_TIME]), 'tool_version': sgp_22_version},
        {'tool_name': ' '.join([PhKeys.SGP32, PhKeys.COMPILE_TIME]), 'tool_version': sgp_32_version},
        {'tool_name': ' '.join([PhKeys.EUICC_PROFILE_PACKAGE, PhKeys.COMPILE_TIME]), 'tool_version': epp_version},
    ]
    PhUtil.print_version(parameters_pool=version_parameters_pool)


def set_configurations():
    """

    :return:
    """
    global execution_mode, error_handling_mode, sgp_22_version, sgp_32_version, epp_version
    """
    Set Execution Mode, First time users can try #PhExecutionModes.SAMPLE_GENERIC
    """
    execution_mode = PhExecutionModes.USER
    error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
    """
    Set/Change Default Target Version of SGP22, SGP32, eUICC Profile Package (if needed)
    """
    sgp_22_version = sgp_22_compile
    epp_version = epp_compile
    sgp_32_version = sgp_32_compile


def main():
    """

    :return:
    """
    """
    Time Object
    """
    ph_time_obj = PhTime()
    ph_time_obj.start()
    """
    Handle Args
    """
    if len(sys.argv) > 1:
        standalone_mode = False
        # callback is not received for '--help', so handle differently
        if sys.argv[1] == '--help':
            # Print Configurations
            print_configurations()
            standalone_mode = True
        handle_cli_request(standalone_mode=standalone_mode)
    """
    Configurations
    """
    # Do Configurations, as per your Need
    set_configurations()
    # Print Configurations
    print_configurations()
    """
    Process
    """
    process_data()
    """
    Wrap up, All Done
    """
    ph_time_obj.stop()
    ph_time_obj.print()
    PhUtil.print_done()


if __name__ == '__main__':
    main()
