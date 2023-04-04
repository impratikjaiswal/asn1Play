from src.generated_code.asn1.GSMA import SGP_22
from src.generated_code.asn1.GSMA.SGP_22 import version, Version
from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data
from src.main.helper.formats import Formats
from src.main.helper.formatsGroup import FormatsGroup


class Dev(ConvertData):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_re_parse_output(self):
        re_parse_output = None
        super().set_re_parse_output(re_parse_output)

    def set_asn_element(self):
        pass

    def set_data_pool(self):
        data_pool_experiment = [
            # Input Data From Directory (Only Yaml Files)
            Data(
                raw_data=r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest" if version == Version.v3_0_0
                else r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest",
                input_format=Formats.YML
            ),
        ]
        super().set_data_pool(data_pool_experiment)
