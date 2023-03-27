from src.generated_code.asn1.GSMA import SGP_22
from src.generated_code.asn1.GSMA.SGP_22 import version, Version
from src.main.helper.convert_data import ConvertData


class StoreMetaData(ConvertData):

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
        asn1_element = SGP_22.RSPDefinitions.StoreMetadataRequest
        super().set_asn_element(asn1_element)

    def set_data_pool(self):
        data_pool_direct_input = [
            #
            "BF2581885A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031930101B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202",
        ]

        data_pool_files_input_2_4 = [
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest.hex",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest.base64",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_Generated.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon_Generated.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_ppr.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_Mandatory.hex",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_ppr.hex",
            #
        ]
        data_pool_files_input_3_0_0 = [
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v2_4\StoreMetadataRequest\StoreMetadataRequest_wo_icon_wo_serviceSpecific.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest.hex",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.hex",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest.base64",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon.base64",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_Generated.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_wo_icon_Generated.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_Mandatory.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_ppr.asn1",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_Mandatory.hex",
            #
            r"..\..\SampleData\GSMA\SGP_22\v3_0_0\StoreMetadataRequest\StoreMetadataRequest_ppr.hex",
            #
        ]
        data_pool = data_pool_direct_input
        if version == Version.v2_4:
            data_pool = data_pool + data_pool_files_input_2_4
        if version == Version.v3_0_0:
            data_pool = data_pool + data_pool_files_input_3_0_0
        super().set_data_pool(data_pool)
