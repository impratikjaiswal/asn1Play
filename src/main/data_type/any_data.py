from src.generated_code.asn1.GSMA import SGP_22
from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data
from src.main.helper.formats import Formats


class AnyData(ConvertData):

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
        data_pool = [
            #
            Data(
                raw_data="bf2a0499020520",
                asn1_element=SGP_22.RSPDefinitions.UpdateMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                raw_data="BF25375A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D65203199020640",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER,
                output_format=Formats.ASN1
            ),
            #
            Data(
                raw_data=r"..\..\SampleData\StoreMetadataRequest_wo_icon.base64",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
            ),
            #
            Data(
                raw_data=r"..\..\SampleData\StoreMetadataRequest_wo_icon.base64",
                asn1_element=SGP_22.RSPDefinitions.StoreMetadataRequest,
                input_format=Formats.DER_64,
                output_format=Formats.ASN1,
                re_parse_output=True
            ),
            #
        ]
        super().set_data_pool(data_pool)
