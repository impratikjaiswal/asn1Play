import time
from util_helpers import util

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
from src.main.helper.modes_execution import ExecutionModes


def process_data(execution_mode):
    data_type_user = [
        #####
        # Empty class for user usage
        ####
        UserData(),
    ]
    data_types_sample_generic = [
        # Sample With Plenty vivid Examples
        #####
        AnyData(),
        ####
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
        # Sample With Unit Testing
        #####
        UnitTesting(),
    ]
    data_type_dev = [
        #####
        # class for dev
        #####
        Dev(),
    ]
    data_types_pool = {
        ExecutionModes.USER: data_type_user,
        ExecutionModes.DEV: data_type_dev,
        ExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        ExecutionModes.SAMPLE_SPECIFIC: data_types_sample_specific,
        ExecutionModes.UNIT_TESTING: data_type_unit_testing,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    for data_type in data_types:
        util.print_heading(str_heading=str(data_type.__class__.__name__))
        data_type.set_data_pool()
        data_type.set_asn_element()
        data_type.set_print_input()
        data_type.set_print_info()
        data_type.set_re_parse_output()
        try:
            ConvertData.parse(data_type)
            time.sleep(0.25)
        except:
            pass


def main():
    """

    :return:
    """
    """
    Set Execution Mode, If you are a first time user then try #ExecutionModes.SAMPLE_GENERIC
    """
    execution_mode = ExecutionModes.USER
    # Print Versions
    util.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION, with_libs=True)
    """
    Set Target Version of SGP22, eUICC Profile Package 
    """
    util.print_version(Keys.SGP22, sgp_22_version)
    util.print_version(Keys.EUICC_PROFILE_PACKAGE, epp_version)
    # Process Data
    process_data(execution_mode)
    util.print_done()


if __name__ == '__main__':
    main()
