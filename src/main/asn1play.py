import time
from util_helpers import util

from src.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.data_type.any_data import AnyData
from src.main.data_type.profile_element import ProfileElement
from src.main.data_type.store_metadata_request import StoreMetaData
from src.main.data_type.unit_testing import UnitTesting
from src.main.data_type.update_metadata_request import UpdateMetadataRequest
from src.main.data_type.user_data import UserData
from src.main.helper.constants_config import ConfigConst
from src.main.helper.convert_data import ConvertData


def process_data():
    data_types = [
        # #####
        # # Sample Store Meta Data Request
        # #####
        # StoreMetaData(),
        # #####
        # # Sample Update Meta Data Request
        # #####
        # UpdateMetadataRequest(),
        # #####
        # # Sample Profile Elements
        # #####
        # ProfileElement(),
        # #####
        # # Sample With Unit Testing
        # #####
        # UnitTesting(),
        # #####
        # # Sample With Plenty vivid Examples
        # #####
        # AnyData(),
        #####
        # Empty class for user usage
        #####
        UserData(),
    ]
    for data_type in data_types:
        util.print_heading(str_heading=str(data_type.__class__.__name__))
        data_type.set_data_pool()
        data_type.set_asn_element()
        data_type.set_print_input()
        data_type.set_print_info()
        data_type.set_re_parse_output()
        if isinstance(data_type, UnitTesting):
            try:
                ConvertData.parse(data_type)
                time.sleep(0.25)
            except:
                pass
        else:
            ConvertData.parse(data_type)


def main():
    """

    :return:
    """
    util.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION, with_libs=True)
    """
    Set Target Version of SGP22, eUICC Profile Package 
    """
    util.print_version(ConfigConst.ASN_SGP_22_NAME, sgp_22_version)
    util.print_version(ConfigConst.ASN_EPP_NAME, epp_version)
    process_data()
    util.print_done()


if __name__ == '__main__':
    main()
