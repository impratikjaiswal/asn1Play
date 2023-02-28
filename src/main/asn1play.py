from util_helpers.util import print_done, print_version, print_version_pkg

from src.generated_code.asn1.GSMA.SGP_22 import version as sgp_22_version
from src.generated_code.asn1.TCA.eUICC_Profile_Package import version as epp_version
from src.main.data_type.any_data import AnyData
from src.main.data_type.profile_element import ProfileElement
from src.main.data_type.store_metadata_request import StoreMetaData
from src.main.data_type.update_metadata_request import UpdateMetadataRequest
from src.main.helper.constants_config import ConfigConst
from src.main.helper.convert_data import ConvertData


def process_data():
    data_types = [
        # StoreMetaData(),
        # UpdateMetadataRequest(),
        # ProfileElement(),
        AnyData(),
    ]
    for data_type in data_types:
        data_type.set_data_pool()
        data_type.set_asn_element()
        data_type.set_print_input()
        data_type.set_print_info()
        data_type.set_re_parse_output()
        ConvertData.parse(data_type)


def main():
    """

    :return:
    """
    print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)
    print_version_pkg(with_python_version=False)
    """
    Set Target Version of SGP22, eUICC Profile Package 
    """
    print_version('SGP22', sgp_22_version, with_python_version=False)
    print_version('eUICC_Profile_Package', epp_version, with_python_version=False)
    process_data()
    print_done()


if __name__ == '__main__':
    main()
