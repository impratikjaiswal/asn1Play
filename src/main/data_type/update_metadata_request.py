from src.generated_code.asn1.GSMA import SGP_22
from src.generated_code.asn1.GSMA.SGP_22 import version, Version
from src.main.helper.convert_data import ConvertData
from src.main.helper.data import Data
from src.main.helper.formats import Formats


class UpdateMetadataRequest(ConvertData):

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
        asn1_element = SGP_22.RSPDefinitions.UpdateMetadataRequest
        super().set_asn_element(asn1_element)

    def set_data_pool(self):
        data_pool_direct_input = [
            #
            Data(raw_data='bf2a0499020520'),
            #
            Data
                (
                raw_data="""{
                profilePolicyRules {ppr2}
                }""",
                input_format=Formats.ASN1,
                output_format=Formats.DER
            ),
        ]

        data_pool_files_input_2_4 = [
            #
            Data(raw_data=r'..\..\SampleData\GSMA\SGP_22\v2_4\UpdateMetadataRequest.asn1'),
            #
            Data(raw_data=r'..\..\SampleData\GSMA\SGP_22\v2_4\UpdateMetadataRequest_ppr.asn1'),
            #
            Data(raw_data=r'..\..\SampleData\GSMA\SGP_22\v2_4\UpdateMetadataRequest.hex'),
            #
        ]
        data_pool_files_input_3_0_0 = [
            #
            Data(raw_data=r'..\..\SampleData\GSMA\SGP_22\v3_0_0\UpdateMetadataRequest.asn1'),
            #
            Data(raw_data=r'..\..\SampleData\GSMA\SGP_22\v3_0_0\UpdateMetadataRequest_ppr.asn1'),
            #
            Data(raw_data=r'..\..\SampleData\GSMA\SGP_22\v3_0_0\UpdateMetadataRequest.hex'),
            #
        ]
        data_pool = data_pool_direct_input
        if version == Version.v2_4:
            data_pool = data_pool + data_pool_files_input_2_4
        if version == Version.v3_0_0:
            data_pool = data_pool + data_pool_files_input_3_0_0
        super().set_data_pool(data_pool)
